import os
import shutil
import sys
import socketserver as SocketServer
from datetime import datetime

from fabric.api import *
import fabric.contrib.project as project
from pelican.server import ComplexHTTPRequestHandler

# Local path configuration (can be absolute or relative to fabfile)
env.deploy_path = 'output'
DEPLOY_PATH = env.deploy_path

# Remote server configuration
production = 'root@localhost:22'
dest_path = '/var/www'

# Rackspace Cloud Files configuration settings
# env.cloudfiles_username = 'my_rackspace_username'
# env.cloudfiles_api_key = 'my_rackspace_api_key'
# env.cloudfiles_container = 'my_cloudfiles_container'

# Github Pages configuration
env.github_pages_branch = "gh-pages"

# Port for `serve`
PORT = 8585

def clean():
    """Remove generated files"""
    if os.path.isdir(DEPLOY_PATH):
        shutil.rmtree(DEPLOY_PATH)
        os.makedirs(DEPLOY_PATH)

# def build():
#     """Build local version of site"""
#     local('pelican -s baseconf.py')

def rebuild():
    """`build` with the delete switch"""
    local('pelican -d -s baseconf.py')

def regenerate():
    """Automatically regenerate site upon file modification"""
    local('pelican -r -s baseconf.py')

def serve():
    """Serve site at http://localhost:8000/"""
    os.chdir(env.deploy_path)

    class AddressReuseTCPServer(SocketServer.TCPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(('', PORT), ComplexHTTPRequestHandler)

    sys.stderr.write('Serving on port {0} ...\n'.format(PORT))
    server.serve_forever()

def reserve():
    """`build`, then `serve`"""
    build()
    serve()

# def preview():
#     """Build production version of site"""
#     local('pelican -s prodconf.py')

# def cf_upload():
#     """Publish to Rackspace Cloud Files"""
#     rebuild()
#     with lcd(DEPLOY_PATH):
#         local('swift -v -A https://auth.api.rackspacecloud.com/v1.0 '
#               '-U {cloudfiles_username} '
#               '-K {cloudfiles_api_key} '
#               'upload -c {cloudfiles_container} .'.format(**env))

# @hosts(production)
# def publish():
#     """Publish to production via rsync"""
#     local('pelican -s prodconf.py')
#     project.rsync_project(
#         remote_dir=dest_path,
#         exclude=".DS_Store",
#         local_dir=DEPLOY_PATH.rstrip('/') + '/',
#         delete=True,
#         extra_opts='-c',
#     )

# def gh_pages():
#     """Publish to GitHub Pages"""
#     rebuild()
#     local("ghp-import -b {github_pages_branch} {deploy_path} -p".format(**env))




TEMPLATE = """
{title}
{hashes}

:date: {year}-{month}-{day} {hour}:{minute:02d}
:tags:
:category:
:slug: {slug}
:summary:
:status: draft


"""

def make_entry(title):
    today = datetime.today()
    slug = title.lower().strip().replace(' ', '-')
    f_create = "content/{}_{:0>2}_{:0>2}_{}.rst".format(
        today.year, today.month, today.day, slug)
    t = TEMPLATE.strip().format(title=title,
                                hashes='#' * len(title),
                                year=today.year,
                                month=today.month,
                                day=today.day,
                                hour=today.hour,
                                minute=today.minute,
                                slug=slug)
    with open(f_create, 'w') as w:
        w.write(t)
    print("File created -> " + f_create)

import livereload

def _live_build(mode, port=8585):
    local('make clean')
    if mode == 'prod':
        local('make publish')
        conf = 'publishconf'
    elif mode == 'dev':
        local('make html')
        conf = 'pelicanconf'
    else:
        raise ValueError(f"Invalid conf: {conf}")
    os.chdir('output')
    server = livereload.Server()
    server.watch('../content/*.rst',
        livereload.shell(f'pelican -s ../{conf}.py -o ../output'))
    server.watch('*.html')
    server.watch('*.css')

    server.serve(liveport=35729, host='0.0.0.0', port=port)

def build_dev(*args, **kwargs):
    return _live_build('dev', *args, **kwargs)


def build_prod(*args, **kwargs):
    return _live_build('prod', *args, **kwargs)

import fabric
