from ultralytics import YOLO

if __name__ == '__main__':
    # 直接使用预训练模型创建模型.
    model = YOLO('yolov8s.pt')
    model.train(data='./data.yaml')