import moviepy.editor as mp
from tkinter.filedialog import askopenfilename

vid_path = askopenfilename()

video = mp.VideoFileClip(vid_path)

audio = video.audio

audio.write_audiofile("demo.mp3")

print("MP3 conversion successful")
