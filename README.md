# video-audio-conv

This Python script uses the MoviePy library to extract audio from a video file and convert it into an MP3 audio file. The script also utilizes the tkinter.filedialog module to prompt the user to select a video file. Here's a breakdown of the code's functionality:

Importing Required Libraries:
The script begins by importing the necessary libraries. moviepy.editor is imported as mp to work with video and audio clips, and askopenfilename is imported from tkinter.filedialog to open a file dialog for selecting a video file.

Prompting for Video File:
The variable vid_path is assigned the value returned by the askopenfilename() function. This function opens a file dialog that allows the user to select a video file. The chosen file's path is stored in the vid_path variable.

Loading Video:
The script uses the VideoFileClip class from MoviePy to load the video from the selected file path (vid_path). The video object represents the video clip.

Extracting Audio:
The script extracts the audio from the loaded video clip using the audio attribute of the video object.

Writing Audio to MP3 File:
The extracted audio is written to an MP3 audio file named "demo.mp3" using the write_audiofile method. This creates a standalone MP3 audio file from the extracted audio.

Print Success Message:
After the audio conversion process is complete, the script prints the message "MP3 conversion successful" to the console.

In summary, this script allows the user to select a video file using a file dialog, then extracts the audio from the video and converts it to an MP3 audio file using the MoviePy library. The resulting MP3 file is named "demo.mp3". This script could be useful when you want to separate the audio from a video file, such as extracting music or spoken content.
