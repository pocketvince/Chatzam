import sys
import os
import glob
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

def signature_already_exists(signature, data_file):
    if not os.path.isfile(data_file):
        return False

    with open(data_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            if str(signature) in line:
                return True
    return False

if len(sys.argv) < 2:
    print("Usage: python3 signature.py file.mp3 or python3 signature.py /full_folder/")
    sys.exit(1)

file_path = sys.argv[1]

if os.path.isdir(file_path):
    mp3_files = glob.glob(os.path.join(file_path, "*.mp3"))

    if len(mp3_files) == 0:
        print("No MP3 files found in the directory.")
        sys.exit(1)

    for mp3_file in mp3_files:
        signature = extract_audio_signature(mp3_file)
        if signature:
            file_name = os.path.splitext(os.path.basename(mp3_file))[0]

            if signature_already_exists(signature, "data.txt"):
                print(f"Signature for {file_name} already exists in data.txt.")
            else:
                if not os.path.isfile("data.txt"):
                    open("data.txt", "w").close()

                with open("data.txt", "a") as file:
                    file.write(file_name + ":" + str(signature) + "\n")

                print(f"{file_name} is added to data.txt.")
else:
    signature = extract_audio_signature(file_path)
    if signature:
        file_name = os.path.splitext(os.path.basename(file_path))[0]

        if signature_already_exists(signature, "data.txt"):
            print(f"Signature for {file_name} already exists in data.txt.")
        else:
            if not os.path.isfile("data.txt"):
                open("data.txt", "w").close()

            with open("data.txt", "a") as file:
                file.write(file_name + ":" + str(signature) + "\n")

            print(f"{file_name} is added to data.txt.")
