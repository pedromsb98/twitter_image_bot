import openai
import yaml

# Cargar configuración desde config.yaml
def load_config():
    with open("config/config.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config

# Obtener el nombre del proyecto desde el archivo config.yaml
config = load_config()
project_name = config["project"]["name"]

# Generar un mensaje divertido
def generate_funny_message(user_name):
    try:
        prompt = f"Generate a fun and short tweet (maximum 15 words) for a user named {user_name}. \
                    You are giving him a personalize portrait of him/her, The tweet should be lighthearted and engaging. Don't include the user name\
                    include always #{project_name}"
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": "You are a funny and creative assistant."},
                      {"role": "user", "content": prompt}],
            max_tokens=30
        )

        return response["choices"][0]["message"]["content"].strip()

    except Exception as e:
        print(f"Error generando el mensaje: {e}")
        return f"@{user_name} here is your portrait!"
