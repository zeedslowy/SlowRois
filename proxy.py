# Setting up Proxies with the requests Library
import requests

proxy_servers = {
   'http': 'http://proxy.sample.com:8080',
   'https': 'http://secureproxy.sample.com:8080',
}

response = requests.get('sample.abc', proxies=proxy_servers)
