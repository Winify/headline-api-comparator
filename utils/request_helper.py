import requests

api_host = "http://localhost:13731"


def get_api_score(api, phrase):
    response = requests.get(url=api_host + "/{}/getScore".format(api), params={'phrase': phrase})
    return response.content.decode()
