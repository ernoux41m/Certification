import sounddevice as sd
from pydub import AudioSegment

# Définir les paramètres pour l'enregistrement audio
duration = 5  # Durée de l'enregistrement en secondes
fs = 44100  # Fréquence d'échantillonnage en Hz

print("Enregistrement en cours...")

# Enregistrer l'audio
audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()

print("Enregistrement terminé.")

# Convertir les données audio en objet AudioSegment
audio_segment = AudioSegment(
    audio_data.tobytes(),
    frame_rate=fs,
    sample_width=audio_data.dtype.itemsize,
    channels=1
)

# Sauvegarder l'audio au format MP3
audio_segment.export("enregistrement.mp3", format="mp3")

print("Audio enregistré avec succès sous 'enregistrement.mp3'.")
