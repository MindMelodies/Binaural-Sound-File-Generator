import soundfile as sf
import numpy as np


def generate_sound(left_frequency, right_frequency, file_duration, file_name, sound_duration=None, silence_duration=None):
    """
    Generates a binaural sound file with specified frequencies for left and right channels, file duration, and file name.

    Parameters:
    - left_frequency (float): frequency for left channel
    - right_frequency (float): frequency for right channel
    - file_duration (float): duration of the file in seconds
    - file_name (str): name of the file to be generated
    - sound_duration (float, optional): duration of the sound in seconds, if not specified set to file_duration
    - silence_duration (float, optional): duration of silence in seconds, if not specified set to 0

    Returns:
    None
    """
    # Set sound_duration to file_duration if not specified
    if not sound_duration:
        sound_duration = file_duration

    # Set silence_duration to 0 if not specified
    if not silence_duration:
        silence_duration = 0

    # Number of samples per second
    samples_per_sec = 96000

    # Total duration of sound with silence
    total_duration = sound_duration + silence_duration

    # Number of repetitions of total duration in audio file
    num_repetitions = int(file_duration / total_duration)

    # Create an array of time for each sample
    t = np.arange(0, sound_duration, 1 / samples_per_sec)

    # Calculate the waveform for the left and right channel
    left_channel = 0.5 * np.sin(2 * np.pi * left_frequency * t)
    right_channel = 0.5 * np.sin(2 * np.pi * right_frequency * t)

    # Create an array of silence with specified duration
    silence = np.zeros(int(samples_per_sec * silence_duration))

    # Concatenate the waveform of left and right channel with silence
    left_with_silence = np.concatenate([left_channel, silence])
    right_with_silence = np.concatenate([right_channel, silence])

    # Create a stereo audio file by repeating the total duration of sound for the specified number of repetitions
    stereo_sound = np.column_stack(
        (np.tile(left_with_silence, num_repetitions), np.tile(right_with_silence, num_repetitions)))

    # Write the audio data to the specified file with PCM 16-bit format
    sf.write(file_name, stereo_sound, samples_per_sec, 'PCM_16')


# Execute the function only if this module is run as the main script
if __name__ == '__main__':
    generate_sound(left_frequency=300, right_frequency=305, file_duration=30, file_name='test.wav')
