from huggingface_hub import InferenceClient
import os
from load_dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HUGGING_FACE_API_KEY")
print(API_KEY)
client = InferenceClient(
    provider="together",
    api_key=API_KEY,
)

video = client.text_to_image(
	"A young man walking on the street",
	model="black-forest-labs/FLUX.1-dev",
)
print(video)