# Binaural Sound Generator

This program generates binaural sound files. It creates a stereo audio file with a sine wave on the left channel and another sine wave on the right channel. The user can specify the frequencies of the left and right channel, the duration of the sound, and the duration of the silence. 

## Features

- Generates binaural sound files in stereo format
- User can specify the frequency of the left and right channel
- User can specify the duration of the sound and silence
- Generates PCM 16-bit audio files

## Requirements


This program requires the following packages to be installed:

*   `numpy`
*   `soundfile`

You can install these packages by running the following command in your terminal:

## You can Install requirements using

```sh
pip install numpy soundfile
```

### Or

```sh
pip install -r requirements.txt
```

## Usage

To use this program, you will need to import the `generate_sound` function and call it with the following parameters:

*   `left_frequency`: the frequency of the sound in the left channel
*   `right_frequency`: the frequency of the sound in the right channel
*   `file_duration`: the duration of the output file in seconds
*   `file_name`: the name of the output file, with its extension (e.g. `test.wav`)
*   `sound_duration` (optional): the duration of the sound in each repetition, default is equal to `file_duration`
*   `silence_duration` (optional): the duration of the silence in each repetition, default is 0

Here's an example of how to generate a binaural sound file with a duration of 30 seconds, and a frequency of 300Hz in the left channel and 305Hz in the right channel:

```python
from binaural_generator import generate_sound

generate_sound(left_frequency=300, right_frequency=305, file_duration=30, file_name='test.wav')
```

## Output

The output of the program will be a binaural sound file in WAV format, with a sample rate of 96000Hz and 16-bit PCM encoding. The file will contain the specified sound repeated as many times as required to fill the specified duration, with the specified silence in between repetitions.
