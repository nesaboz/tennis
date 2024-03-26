from ultralytics import YOLO   # this takes time the first time it is run


model = YOLO('yolov8x')

result = model.predict('input_videos/input_video.mp4', save=True)


