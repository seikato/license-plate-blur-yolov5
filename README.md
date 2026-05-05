# license-plate-blur-yolov5
Automatic license plate detection and blurring using YOLOv5 and OpenCV.
PlateBlur is a Python tool that detects and blurs license plates in images using a YOLOv5-based object detection model.

It is designed to run locally and process images via a simple command-line interface.

---

## Features

- License plate detection using YOLOv5
- Automatic Gaussian blur applied to detected regions
- CLI-based execution (no GUI required)
- Configurable input/output directories
- Reproducible environment setup

---

## Example

Before / After images can be added here.

---

## Requirements

- Python 3.10
- Linux or WSL (recommended)
- CUDA optional (CPU works as well)

---

## Installation

### 1. Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/PlateBlur.git
cd PlateBlur

---

## 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
```

---

## 3. Install dependencies

```bash
pip install torch==2.5.1 torchvision==0.20.1
pip install opencv-python yolov5
```

---

## Important Notes

- Please avoid using PyTorch 2.6 or later, as it introduces breaking changes in model loading.
- Ensure that `torch` and `torchvision` versions are strictly compatible.

---

# Model Download

A pretrained YOLOv5 license plate detection model is required for inference.

## Download model

```bash
wget https://huggingface.co/keremberke/yolov5m-license-plate/resolve/main/best.pt
```

Place the downloaded file in the project root directory:

```text
PlateBlur/best.pt
```

---

# Usage

## Basic Usage

```bash
python3 blur.py 2918
```

### Input Image

```text
/mnt/c/home/40_photo/2026-01-03/DSC02918.JPG
```

### Output Image

```text
/mnt/c/home/40_photo/2026-01-03/output_2918.jpg
```

---

## Advanced Usage

### Specify input directory

```bash
python3 blur.py 2918 --input_dir /path/to/images
```

### Specify output directory

```bash
python3 blur.py 2918 --output_dir /path/to/output
```

### Specify model path

```bash
python3 blur.py 2918 --model best.pt
```

---

# How it Works

1. Load YOLOv5 model  
2. Read input image  
3. Detect license plates  
4. Extract bounding boxes  
5. Apply Gaussian blur to detected regions  
6. Save processed image  

---

# Troubleshooting

## PyTorch 2.6+ Compatibility Issue

### Error

```text
_pickle.UnpicklingError: Weights only load failed
```

### Solution

```bash
pip install torch==2.5.1 torchvision==0.20.1
```

---

## torchvision NMS Error

### Error

```text
RuntimeError: operator torchvision::nms does not exist
```

### Solution

Ensure version compatibility:

```bash
pip install torch==2.5.1 torchvision==0.20.1
```

---

## torch.hub Usage Issues (Not Recommended)

Avoid:

```python
torch.hub.load(...)
```

Recommended approach:

```python
from yolov5 import load
model = load("best.pt")
```

---

## Hugging Face Download Error (401 Unauthorized)

If download fails:

- Ensure the repository is public  
- Or authenticate using:

```bash
hf auth login
```

---

# Security Notice

This project loads `.pt` model files using PyTorch.

Please ensure that only trusted model files are used, as untrusted pickle-based models may pose security risks.

---

# Future Improvements

- Batch image processing  
- Video processing support  
- Face + license plate anonymization  
- Confidence threshold tuning  
- Web UI or API version  

---

# License

This project is released under the MIT License.

You are free to use, modify, and distribute it with proper attribution.

---

# Author

- X: https://x.com/seikato  
- LinkedIn: https://www.linkedin.com/in/seikato/

