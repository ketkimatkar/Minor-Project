from moviepy.editor import *
vid=VideoFileClip('C:/Users/Valkyrie/Desktop/Mobile Operator Identification Using Python.mp4')
start_time=float(input("Enter start time:"))*60
end_time=float(input("Enter end time:"))*60
trim_vid=vid.subclip(start_time,end_time)
trim_vid.write_videofile('C:/Users/Valkyrie/Desktop/trim1.mp4',codec='libx264')