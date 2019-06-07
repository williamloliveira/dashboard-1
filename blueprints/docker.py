
import flask
import docker

import services.auth

#connection = docker.DockerClient('tcp://0.0.0.0:2376')
connection = docker.DockerClient()

blueprint = flask.Blueprint('docker', __name__)

@blueprint.route('/docker', methods=[ 'GET' ])
@services.auth.login_required
def get_docker():

    if not flask.session.get('email'):
        return flask.redirect('/sign-in')

    context = {
        'page': 'docker',
        'containers': connection.containers.list(all=True)
    }

    return flask.render_template('docker.html', context=context)

@blueprint.route('/docker/start/<string:containerid>', methods=[ 'GET' ])
def start_container(containerid):

    container = connection.container.get(containerid)

    if container:
        container.start()

    return flask.redirect('/docker')

@blueprint.route('/docker/stop/<string:containerid>', methods=[ 'GET' ])
def stop_container(containerid):

    container = connection.container.get(containerid)

    if container:
        container.stop()
        
    return flask.redirect('/docker')