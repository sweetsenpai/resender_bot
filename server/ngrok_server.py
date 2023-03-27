
from pyngrok import ngrok
ngrok_token = '2NQOzATCmjSDbEajxjTVZB1mA8k_3kP8VK7eHG1Pvs2ksPhHd'


def get_https():
    ngrok.set_auth_token(ngrok_token)
    http_tunnel = ngrok.connect(70, bind_tls=True)
    return http_tunnel.data['public_url']
