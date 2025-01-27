import openai
import os
from dotenv import load_dotenv
import requests

# Cargar variables de entorno
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Generar imagen con OpenAI
def generate_image(user_name):
    try:
        description = f"Create an abstract portrait of a person based on the username {user_name}. The style should be surreal and colorful.\
                        try to make sure that the style of the painting is similar all the time and change compliments like hats or glasses \
                        in the image. make sure to keep the style clean and a bit abstract, with a 60s mood."
        
        response = openai.Image.create(
            prompt=description,
            n=1, 
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return image_url
    except Exception as e:
        print(f"Error generando la imagen: {e}")
        return None

# Descargar imagen generada
def download_image(image_url):
    response = requests.get(image_url)
    image_path = "assets/generated_image.png"
    with open(image_path, "wb") as file:
        file.write(response.content)
    return image_path