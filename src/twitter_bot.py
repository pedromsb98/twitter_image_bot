import time
import tweepy
import yaml
from twitter_api import twitConnection, twitConnection_v1
from image_generator import generate_image, download_image
from utils import generate_funny_message

# Conectar a las APIs de Twitter
client = twitConnection()
client_v1 = twitConnection_v1()
client_bear = client.bearer_client

# Obtener el nombre de usuario desde el archivo config.yaml
user = client_v1.verify_credentials()
username = user.screen_name

# Lista de tweets respondidos
answered_tweets = set()
query = f"draw me @{username} OR @{username} draw me"

# Bucle infinito para revisar nuevos tweets
while True:
    try:
        response = client_bear.search_recent_tweets(query=query, max_results=10, tweet_fields=["author_id"], expansions="author_id", user_fields=["username"])

        if response.data:
            users = {user["id"]: user for user in response.includes["users"]}

            for tweet in response.data:
                user = users.get(tweet.author_id)
                tweet_id = tweet.id

                if tweet_id not in answered_tweets:
                    print(f"@{user.username} dijo: {tweet.text}")

                    image_url = generate_image(user.username)

                    if image_url:
                        print(f"Imagen generada: {image_url}")

                        image_path = download_image(image_url)
                        media = client_v1.media_upload(filename=image_path)
                        media_id = media.media_id
                        print("media uploaded")

                        msg = f"@{user.username} {generate_funny_message(user.username)}"
                        client.create_tweet(text=msg, media_ids=[media_id], in_reply_to_tweet_id=tweet_id)
                        answered_tweets.add(tweet_id)
                        print("twit answered")
                    else:
                        print(f"Error generando imagen para @{user.username}.")
                else:
                    print(f"Tweet {tweet_id} ya respondido.")

        else:
            print("No hay tweets nuevos. Esperando 5 minutos...")

        time.sleep(300)

    except tweepy.TooManyRequests:
        print("Límite de solicitudes alcanzado. Esperando 15 minutos...")
        time.sleep(900)

    except Exception as e:
        print(f"Error: {e}")
        print("Reintentando en 5 minutos...")
        time.sleep(300)
