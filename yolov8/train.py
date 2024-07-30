import torch
from ultralytics import YOLO
import multiprocessing

if __name__ == '__main__':
    #multiprocessing.freeze_support()
    model = YOLO("yolov8x.yaml")
    model.to(torch.device('cuda'))
    results = model.train(data="C:/Users/Lenovo/Desktop/yolov8n/config.yaml", epochs=100, imgsz=320,lr0=0.0005,batch=14) 
    metrics = model.val()

    print(f"Mean Average Precision @.5:.95 : {metrics.box.map}")    
    print(f"Mean Average Precision @ .50   : {metrics.box.map50}") 
    print(f"Mean Average Precision @ .70   : {metrics.box.map75}")