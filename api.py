"""Github API request.


"""
import os
import requests

from bs4 import BeautifulSoup

API_TOKEN = os.getenv("API_TOKEN")
API_URL = os.getenv("API_URL")


def api():
    request = requests.get(API_URL, params=None, auth=API_TOKEN)


def user():
    """Get a single user.

    Example:
        >>>GET users/:username/stats/participation
        {
            "owner": [11, 12, 0, 34, 0]
        }

    """
    request = requests.get()


def project():
    """Get a single user.

    Example:
        >>>GET projects/:username
        {
          "owner_url": "https://api.github.com/repos/api-playground/projects-test",
          "url": "https://api.github.com/projects/1002604",
          "html_url": "https://github.com/api-playground/projects-test/projects/12",
          "columns_url": "https://api.github.com/projects/1002604/columns",
          "id": 1002604,
          "name": "Projects Documentation",
          "body": "Developer documentation project for the developer site.",
          "number": 1,
          "state": "open",
          "creator": {
            "login": "octocat",
            "id": 1,
            "avatar_url": "https://github.com/images/error/octocat_happy.gif",
            "gravatar_id": "",
            "url": "https://api.github.com/users/octocat",
            "html_url": "https://github.com/octocat",
            "followers_url": "https://api.github.com/users/octocat/followers",
            "following_url": "https://api.github.com/users/octocat/following{/other_user}",
            "gists_url": "https://api.github.com/users/octocat/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/octocat/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/octocat/subscriptions",
            "organizations_url": "https://api.github.com/users/octocat/orgs",
            "repos_url": "https://api.github.com/users/octocat/repos",
            "events_url": "https://api.github.com/users/octocat/events{/privacy}",
            "received_events_url": "https://api.github.com/users/octocat/received_events",
            "type": "User",
            "site_admin": false
          },
          "created_at": "2011-04-10T20:09:31Z",
          "updated_at": "2014-03-03T18:58:10Z"
        }

    """
    request = requests.get()


def weekly_commit_count():
    """Get the weekly commit count for the repository owner.

    Example:
        >>>GET repo/:owner/stats/participation
        {
            "owner": [11, 12, 0, 34, 0]
        }

    This returns the last week, we only need the last day.

    """
    request = requests.get()

    last_day_commit_count = request[-1]


def commit_graph():
    """Get the users commit graph to display.

    Data Graph URL:
        "data-graph-url="/users/ratchetwrench/contributions"
    
    XPath:
        #js-pjax-container >
            div > div.col-9.float-left.pl-2 >
                div.position-relative > div.mt-4 >
                    div.js-contribution-graph >
                        div.mb-5.border.border-gray-dark.rounded-1.py-2 >
                            div.js-calendar-graph.is-graph-loading.graph-canvas.calendar-graph.height-full

    :return: 
    """
    request = requests.get("/users/{username}/contributions")
