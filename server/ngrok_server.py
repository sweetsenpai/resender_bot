
from pyngrok import conf, ngrok
import os
ngrok_token = os.environ['rsn_token']


def get_https():
    ngrok.set_auth_token(ngrok_token)
    http_tunnel = ngrok.connect(70, bind_tls=True)
    return http_tunnel.data['public_url']