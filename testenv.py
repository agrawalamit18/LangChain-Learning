import os
from dotenv import load_dotenv,dotenv_values
load_dotenv(override=True)  # Load the environment variables    

config = dotenv_values(".env")  # Load the .env file

print(config['DATABASE_URL'])


print(os.getenv("MY_SECRET_KEY"))