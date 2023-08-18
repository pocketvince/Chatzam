import sys
import os
import librosa
import numpy as np

def extract_audio_signature(file_path):
    try:
        audio, sr = librosa.load(file_path)
        stft = np.abs(librosa.stft(audio))
        chroma = librosa.feature.chroma_stft(S=stft, sr=sr)
        signature = np.mean(chroma, axis=1)

        return signature.tolist()

    except Exception as e:
        print("Error while extracting audio signature:", str(e))
        return None

def find_matching_file(signature, data_file):
    if not os.path.isfile(data_file):
        return None

    with open(data_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if ":" in line:
                file_name, file_signature = line.split(":")
                file_signature = eval(file_signature)
                # ratio
                if np.allclose(signature, file_signature, atol=0.04):
                    return file_name

    return None

if len(sys.argv) < 2:
    print("Usage: python3 chatzam.py file.mp3")
    sys.exit(1)

file_path = sys.argv[1]

signature = extract_audio_signature(file_path)
if signature:
    matching_file = find_matching_file(signature, "data.txt")
    if matching_file:
        print(f"music identified: {matching_file}")
    else:
        print("No matching found in data.txt.")
