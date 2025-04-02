import pyaudio
import wave
from pydub import AudioSegment
import os

def record_audio(filename, duration=5, sample_rate=44100, channels=1, chunk=1024):
    # Initialize PyAudio
    p = pyaudio.PyAudio()
    
    # Open audio stream
    stream = p.open(
        format=pyaudio.paInt16,
        channels=channels,
        rate=sample_rate,
        input=True,
        frames_per_buffer=chunk
    )
    
    print(f"Recording for {duration} seconds...")
    
    # Record audio
    frames = []
    for i in range(0, int(sample_rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)
    
    print("Recording finished.")
    
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    # Save as WAV file
    wav_filename = f"{filename}.wav"
    wf = wave.open(wav_filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()
    print(f"Created WAV file: {wav_filename}")
    
    return wav_filename

# def convert_to_mp3(wav_filename, output_mp3=None):
#     """
#     Convert WAV file to MP3 format.
    
#     Args:
#         wav_filename: Input WAV filename
#         output_mp3: Output MP3 filename (if None, will use the same name with .mp3 extension)
    
#     Returns:
#         Path to the created MP3 file
#     """
#     if output_mp3 is None:
#         output_mp3 = os.path.splitext(wav_filename)[0] + ".mp3"
    
#     # Convert WAV to MP3
#     audio = AudioSegment.from_wav(wav_filename)
#     audio.export(output_mp3, format="mp3")
    
#     print(f"MP3 file saved: {output_mp3}")
#     return output_mp3

# def record_and_save_wav(filename="recording", duration=5):
#     """
#     Record audio and save directly as MP3.
    
#     Args:
#         filename: Base filename without extension
#         duration: Recording duration in seconds
    
#     Returns:
#         Path to the created MP3 file
#     """
#     # Record audio to WAV
#     wav_file = record_audio(filename, duration)
    
#     # Convert to MP3
#     # mp3_file = convert_to_mp3(wav_file)
    
#     # Optionally remove the temporary WAV file
#     # os.remove(wav_file)
    
#     return wav_file

# if __name__ == "__main__":
#     # Example usage
#     wav_file = record_audio("wav_recording", duration=10)
#     print(f"Created WAV file: {wav_file}")