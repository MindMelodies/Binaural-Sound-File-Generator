# Binaural Sound Generator

This program generates binaural sound files. It creates a stereo audio file with a sine wave on the left channel and another sine wave on the right channel. The user can specify the frequencies of the left and right channel, the duration of the sound, and the duration of the silence. 

## Features

- Generates binaural sound files in stereo format
- User can specify the frequency of the left and right channel
- User can specify the duration of the sound and silence
- Generates PCM 16-bit audio files

## Usage

```python
import soundfile as sf
import numpy as np

def generate_sound(left_frequency, right_frequency, file_duration, file_name, sound_duration=None, silence_duration=None):
    """
    Generates a binaural sound file with specified parameters
    :param left_frequency: frequency of the left channel
    :param right_frequency: frequency of the right channel
    :param file_duration: duration of the audio file in seconds
    :param file_name: name of the output file
    :param sound_duration: duration of the sound in seconds, defaults to file_duration if not specified
    :param silence_duration: duration of the silence in seconds, defaults to 0 if not specified
    """
    # If sound duration is not specified, set it to file duration
    if not sound_duration:
        sound_duration = file_duration
        
    # If silence duration is not specified, set it to 0
    if not silence_duration:
        silence_duration = 0

    # Number of samples per second
    samples_per_sec = 96000
    
    # Total duration of sound and silence
    total_duration = sound_duration + silence_duration

    # Number of repetitions of the total duration in the audio file
    num_repetitions = int(file_duration / total_duration)

    # Create an array of times for each sample
    t = np.arange(0, sound_duration, 1/samples_per_sec)

    # Calculate the waveform for the left and right channel
    left_channel = 0.5 * np.sin(2 * np.pi * left_frequency * t)
    right_channel = 0.5 * np.sin(2 * np.pi * right_frequency * t)

    # Create an array of silence with specified duration
    silence = np.zeros(int(samples_per_sec * silence_duration))

    # Concatenate the waveform of the left and right channel with silence
    left_with_silence = np.concatenate([left_channel, silence])
    right_with_silence = np.concatenate([right_channel, silence])

    # Create a stereo audio file repeating the total duration of sound for specified number of repetitions
    stereo_sound = np.column_stack((np.tile(left_with_silence, num_repetitions), np.tile(right_with_silence, num_repetitions)))

    # Write the audio data to the specified file with PCM 16-bit format
    sf.write(file_name, stereo_sound, samples_per_sec, 'PCM_16')
```

## Requirements


This program requires the following packages to be installed:

*   `numpy`
*   `soundfile`

You can install these packages by running the following command in your terminal:

## You can Install requirements using

```sh
pip install numpy soundfile
```

## Or

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
from binaural_generator import generate_sound  generate_sound(left_frequency=300, right_frequency=305, file_duration=30, file_name='test.wav')
```

## Output

The output of the program will be a binaural sound file in WAV format, with a sample rate of 96000Hz and 16-bit PCM encoding. The file will contain the specified sound repeated as many times as required to fill the specified duration, with the specified silence in between repetitions.
