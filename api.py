from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
import subprocess
import os
from pathlib import Path

app = FastAPI()

# Directory to save uploaded files
UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/run-inference/")
async def run_inference(
    model_file: UploadFile = File(...),
):
    """
    Endpoint to upload a single model file and run inference.
    
    Args:
        model_file (UploadFile): Complete model file containing weights and architecture.
    
    Returns:
        JSONResponse: Inference result or error message.
    """
    try:
        # Save uploaded file
        model_path = Path(UPLOAD_DIR) / model_file.filename
        
        with open(model_path, "wb") as mf:
            mf.write(await model_file.read())
        
        # Run the inference script
        result = subprocess.run(
            ["python3", "inference.py", "--model", str(model_path)],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            return JSONResponse(
                content={"error": "Inference script failed", "details": result.stderr},
                status_code=500,
            )
        
        return JSONResponse(content={"result": result.stdout}, status_code=200)
    
    except Exception as e:
        return JSONResponse(
            content={"error": "An error occurred", "details": str(e)},
            status_code=500,
        )
