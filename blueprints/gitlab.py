
import requests
import flask

ACCESS_TOKEN = 'm82eo7QN7HE2f1X7iUXa'

PROJECTS_URL = 'http://localhost:8000/api/v4/projects?private_token={}'.format(ACCESS_TOKEN)

r = requests.get(PROJECTS_URL)

#print(r.json())
#print('Id: ', r.id[0])

COMMITS_URL = 'http://localhost:8000/api/v4/projects/1/repository/commits?private_token={}'.format(ACCESS_TOKEN)

blueprint = flask.Blueprint('gitlab', __name__)

@blueprint.route('/gitlab', methods=[ 'GET' ])
def get_gitlab():

    #projects = requests.get(PROJECTS_URL).json()

    context = {
        'page': 'gitlab',
        'projects': requests.get(PROJECTS_URL).json(),
        'commits': requests.get(COMMITS_URL).json()
    }

    return flask.render_template('gitlab.html', context=context)

@blueprint.route('/gitlab', methods=[ 'POST' ])
def post_gitlab():

    #projects = requests.get(PROJECTS_URL).json()

    context = {
        'page': 'gitlab',
        #'projects': requests.get(PROJECTS_URL).json(),
        #'commits': requests.get(COMMITS_URL).json()
    }

    return flask.render_template('gitlab.html', context=context)