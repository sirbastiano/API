# FastAPI Inference API

This project provides a FastAPI-based API to upload a weight file and an architecture file, run an inference script (`inference.py`), and return the results.

## Features

- Accepts two file uploads via a `POST` request:
  - **Weight file** (e.g., `.pth` or similar).
  - **Architecture file** (e.g., model definition or pkl).
- Executes the `inference.py` script with the uploaded files.
- Returns the inference results or an error message.

## Requirements

- Python 3.10
- FastAPI
- Uvicorn
- Other dependencies as required by your `inference.py`.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sirbastiano/API.git
   cd API
   ```

2. Set up a virtual environment and activate it (or use miniconda):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the API

1. Start the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`.

### API Endpoint

#### `POST /run-inference/`

Uploads two files (weight and architecture) and runs inference.

- **Request**:
  - `weight_file`: File to be uploaded (e.g., `.weights` file).
  - `architecture_file`: File to be uploaded (e.g., model definition file).

  Example `cURL` command (from Client):
  ```bash
  curl -X POST "http://127.0.0.1:8000/run-inference/" \
       -F "weight_file=@path_to_weight_file" \
       -F "architecture_file=@path_to_architecture_file"
  ```

- **Response** (example):
  - On success:
    ```json
    {
      "result": "Inference output"
    }
    ```
  - On failure:
    ```json
    {
      "error": "Error message",
      "details": "Additional error details"
    }
    ```

## Example `inference.py`

The `inference.py` script should process the weight and architecture files. 

To be **tailored** to a specific edge device.

## Folder Structure

```
.
├── app.py                # FastAPI script
├── inference.py          # Inference logic script
├── uploaded_files/       # Directory for uploaded files
├── requirements.txt      # Python dependencies
└── README.md             # Documentation
```

## Dependencies

List of required packages (add to `requirements.txt`):
- `fastapi`
- `uvicorn`

Install them with:
```bash
pip install fastapi uvicorn
```

## Notes

- Ensure `inference.py` is in the project directory and executable.
- The uploaded files will be stored in the `uploaded_files/` directory. Clean this directory periodically if needed.
"""

# Save the content to a file
file_path = "/mnt/data/README.md"
with open(file_path, "w") as file:
    file.write(readme_content)

file_path