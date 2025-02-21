from fastapi import FastAPI, UploadFile, File
import torch
import cv2
import numpy as np
from PIL import Image
import io

app = FastAPI()

# Cargar el modelo YOLOv5 entrenado
model_path = "best_model.pt"  # Debes subirlo al repositorio
model = torch.hub.load("ultralytics/yolov5", "custom", path=model_path, force_reload=True)

class_names = ["helmet", "head", "person"]

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    results = model(image)

    detections = []
    for *box, conf, cls in results.xyxy[0].tolist():
        detections.append({
            "class": class_names[int(cls)],
            "confidence": conf,
            "bbox": [box[0], box[1], box[2], box[3]]
        })

    return {"detections": detections}
