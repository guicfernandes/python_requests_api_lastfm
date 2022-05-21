import requests
import json

API_KEY = '55611cf831667522de3538cec4806bd3'
USER_AGENT = 'Dataquest'

def lastfm_get(payload):
    # define headers and URL
    headers = {'user-agent': USER_AGENT}
    url = 'http://ws.audioscrobbler.com/2.0/'

    # Add API key and format to the payload
    payload['api_key'] = API_KEY
    payload['format'] = 'json'

    response = requests.get(url, headers=headers, params=payload)
    return response

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def inicia_job():
    r = lastfm_get({
        'method': 'chart.gettopartists'
    })
    # jprint(r.json())
    jprint(r.json()['artists']['@attr'])


inicia_job()