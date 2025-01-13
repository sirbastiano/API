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
    weight_file: UploadFile = File(...),
    architecture_file: UploadFile = File(...),
):
    """
    Endpoint to upload weight and architecture files, and run inference.
    
    Args:
        weight_file (UploadFile): Weight file for the model.
        architecture_file (UploadFile): Architecture file for the model.
    
    Returns:
        JSONResponse: Inference result or error message.
    """
    try:
        # Save uploaded files
        weight_path = Path(UPLOAD_DIR) / weight_file.filename
        architecture_path = Path(UPLOAD_DIR) / architecture_file.filename
        
        with open(weight_path, "wb") as wf:
            wf.write(await weight_file.read())
        
        with open(architecture_path, "wb") as af:
            af.write(await architecture_file.read())

        # Run the inference script
        result = subprocess.run(
            ["python3", "inference.py", "--weights", str(weight_path), "--architecture", str(architecture_path)],
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