import whisper 

model = whisper.load_model("base")
result = model.transcribe("common_voice_fr_38025278.mp3")
print(result["text"])