
import requests
import flask

ACCESS_TOKEN = 'm82eo7QN7HE2f1X7iUXa'

PROJECTS_URL = 'http://localhost:8000/api/v4/projects?private_token={}'.format(ACCESS_TOKEN)

#COMMITS_URL = 'http://localhost:8000/api/v4/projects/1/repository/commits?private_token={}'.format(ACCESS_TOKEN)

CREATE_PROJECT_URL = 'http://localhost:8000/api/v4/projects/user'

blueprint = flask.Blueprint('gitlab', __name__)

@blueprint.route('/gitlab', methods=[ 'GET' ])
def get_gitlab():

    context = {
        'page': 'gitlab',
        'projects': requests.get(PROJECTS_URL).json()
    }

    return flask.render_template('gitlab.html', context=context)

@blueprint.route('/gitlab/commits/<string:pid>', methods=[ 'GET' ])
def get_commits_gitlab(pid):

    COMMITS_URL = 'http://localhost:8000/api/v4/projects/' + str(pid) +'/repository/commits?private_token={}'.format(ACCESS_TOKEN)

    context = {
        'page': 'gitlab/commits',
        'commits': requests.get(COMMITS_URL).json()
    }

    return flask.render_template('gitlab_commit.html', context=context)