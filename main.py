from fastapi import FastAPI, UploadFile, File
import torch
import io
from PIL import Image
import uvicorn

# Inicializar FastAPI
app = FastAPI()

# Cargar el modelo YOLOv5
model = torch.hub.load("ultralytics/yolov5", "custom", path="best_model.pt", force_reload=True)

@app.get("/")
async def root():
    return {"message": "FastAPI está funcionando correctamente"}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Leer la imagen
    image = Image.open(io.BytesIO(await file.read()))

    # Realizar la detección
    results = model(image)

    # Convertir los resultados en formato JSON
    detections = []
    for *box, conf, cls in results.xyxy[0].tolist():
        detections.append({
            "bbox": box,
            "confidence": conf,
            "class": int(cls)
        })

    return {"detections": detections}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
