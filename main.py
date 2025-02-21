import os
import uvicorn

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Railway asigna el puerto automáticamente
    uvicorn.run(app, host="0.0.0.0", port=port)
