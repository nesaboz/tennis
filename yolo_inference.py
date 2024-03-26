from ultralytics import YOLO   # this takes time the first time it is run


model = YOLO('models/yolo5_last.pt')

result = model.predict('input_videos/input_video.mp4', conf=0.2, save=True)
# result = model.predict('input_videos/input_video.mp4', save=True)


