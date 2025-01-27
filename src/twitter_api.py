import tweepy
import yaml

# Cargar credenciales desde config.yaml
def load_credentials():
    with open("config/config.yaml", "r") as file:
        creds = yaml.safe_load(file)
    return creds

# Cargar las credenciales una sola vez
creds = load_credentials()

# Conexión a la API v2
def twitConnection():
    creds = load_credentials()
    client = tweepy.Client(
        consumer_key=creds["twitter"]["consumer_key"],
        consumer_secret=creds["twitter"]["consumer_secret"],
        access_token=creds["twitter"]["access_token"],
        access_token_secret=creds["twitter"]["access_secret"],
    )
    client.bearer_client = tweepy.Client(
        bearer_token=creds["twitter"]["bearer_token"], wait_on_rate_limit=True
    )
    return client

# Conexión a la API v1 (para subir imágenes)
def twitConnection_v1():
    creds = load_credentials()
    auth = tweepy.OAuth1UserHandler(
        creds["twitter"]["consumer_key"], creds["twitter"]["consumer_secret"]
    )
    auth.set_access_token(creds["twitter"]["access_token"], creds["twitter"]["access_secret"])
    return tweepy.API(auth)