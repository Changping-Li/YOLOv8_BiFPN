
if __name__ == '__main__':
    """Train and optimize YOLO model given training data and device."""
    # model = cfg.model or 'yolov8n.pt'
    from ultralytics import RTDETR

    model = RTDETR(
        'G:/UAV/code/ultralytics-8940a27bdb26895f09a1554514a9a46312aa89c3/ultralytics/models/rt-detr/rt-detr-l.yaml')
    model._load("rtdetr-l.pt")
    model.train(
        **{'cfg': 'G:/UAV/code/ultralytics-8940a27bdb26895f09a1554514a9a46312aa89c3/ultralytics/yolo/cfg/default.yaml',
           'data': 'data.yaml'})