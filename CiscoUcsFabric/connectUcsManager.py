import requests
from requests.auth import HTTPBasicAuth
import json

# UCS Manager details
ucs_ip = "192.168.1.10"
ucs_username = "admin"
ucs_password = "password"

# Disable SSL warnings (if using self-signed certificates)
requests.packages.urllib3.disable_warnings()

# Function to establish a session
def connect_to_ucs(ip, username, password):
    url = f"https://{ip}/nuova"
    session = requests.Session()
    session.auth = HTTPBasicAuth(username, password)
    session.verify = False  # Disable SSL verification if needed
    return session, url

# Create session
session, base_url = connect_to_ucs(ucs_ip, ucs_username, ucs_password)

