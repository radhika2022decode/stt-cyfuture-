# -*- coding: utf-8 -*-
"""stt_whisper.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CtTB1TyWiI5tfkpdGCdpmbkDg3LtJml2
"""

# Importing necessary libraries
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torch
import librosa

# Loading the Whisper model and processor from Hugging Face
model = "openai/whisper-base"
processor = WhisperProcessor.from_pretrained(model)
whisper = WhisperForConditionalGeneration.from_pretrained(model)

# Loading and preprocessing the audio file
audio_path = "/content/sample-2.mp3"
audio, sr = librosa.load(audio_path, sr=16000)

# Tokenize input and generate transcription
input_features = processor(audio, sampling_rate=16000, return_tensors="pt", language= 'en').input_features
with torch.no_grad():
    predicted_ids = whisper.generate(input_features)

# Decode and print the transcription
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)[0]
print("\n    Transcribed Text    \n")
print(transcription)

# Save as a txt file
with open('transcription.txt', 'w') as txt:
    txt.write(transcription)

