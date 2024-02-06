import requests

def shorten_url(long_url):
    api_url = 'https://tinyurl.com/api-create.php'
    params = {'url': long_url}
    response = requests.get(api_url, params=params)
    
    if response.status_code == 200:
        return response.text
    else:
        return None