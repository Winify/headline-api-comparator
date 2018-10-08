import requests


def spamcheck_api_score(headline):
    content = {
        'email': headline,
        'options': 'short'
    }

    response = requests.post(url='https://spamcheck.postmarkapp.com/filter', json=content)
    return response.json().get('score')
