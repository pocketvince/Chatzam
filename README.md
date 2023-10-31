![Alt text](https://raw.githubusercontent.com/pocketvince/Chatzam/main/chatzam_transparent.png?raw=true "logo")

# Chatzam
Chatzam is a decentralized command-line tool, akin to Shazam, designed to identify songs from their audio signatures. By leveraging unique audio signatures, Chatzam can accurately match and identify songs from a vast database. At this moment, the database have a collection of 21.662 songs, ranging from compilations between 1920 to 2018, as well as a lot of recent YouTube playlists. A standout feature of Chatzam is the ability for users to seamlessly integrate their personal songs into the system, expanding the recognition capabilities.

## Installation
```shell
root@pocketvince:~# pip3 install librosa numpy
```
## Usage
To identify a song, you can execute the command:
```shell
python3 chatzam.py song.mp3
```

If you want to record the signature of a song in data.txt, you can execute:

```shell
python3 signature.py song.mp3
```
Additionally, you can add the entirety of a folder:

```shell
python3 signature.py /folder/
```

## Contributing

Readme generator: https://www.makeareadme.com/

Logo: https://openai.com/dall-e-2

## Extra info
I had already explored Librosa to create MP3adcleaner
Here I simply tried to see if it was possible to create a "Shazam" in command-line and decentralized.
