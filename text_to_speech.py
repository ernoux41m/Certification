import requests

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/EjtTWI2Y9BBilPwnIBhg"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": "57cc74798fe55a610d241efcbe8c6920"
}

data = {
  "text": "Jérémy tu pue la merde. Ton visage me fait mal aux yeux je preèfre regarder directement le soleil de qu regarder ton visage.",
  "model_id": "eleven_multilingual_v2",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
  }
}

response = requests.post(url, json=data, headers=headers)
with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)
