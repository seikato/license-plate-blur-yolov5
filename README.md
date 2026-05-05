# license-plate-blur-yolov5

Automatic license plate detection and blurring using YOLOv5 and OpenCV.

This tool detects license plates in images and applies Gaussian blur to anonymize them.  
Designed for simple local execution via CLI.

---

## Features

- YOLOv5-based license plate detection
- Automatic Gaussian blur
- CLI-based workflow (no GUI required)
- Configurable input/output paths
- Lightweight and reproducible setup

---

## Quick Start

```bash
git clone https://github.com/seikato/license-plate-blur-yolov5.git
cd license-plate-blur-yolov5

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip

pip install torch==2.5.1 torchvision==0.20.1
pip install opencv-python yolov5
```

Download model:

```bash
wget https://huggingface.co/keremberke/yolov5m-license-plate/resolve/main/best.pt
```

Run:

```bash
python3 blur.py 2918
```

---

## Example

Input:
```
/mnt/c/home/DSC02918.JPG
```

Output:
```
/mnt/c/home/output_2918.jpg
```

(Add before/after images here for better clarity)

---

## Installation

### 1. Clone repository

```bash
git clone https://github.com/seikato/license-plate-blur-yolov5.git
cd license-plate-blur-yolov5
```

### 2. Create virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
```

### 3. Install dependencies

```bash
pip install torch==2.5.1 torchvision==0.20.1
pip install opencv-python yolov5
```

---

## Model Download

A pretrained YOLOv5 license plate detection model is required.

```bash
wget https://huggingface.co/keremberke/yolov5m-license-plate/resolve/main/best.pt
```

Place it in:

```
./best.pt
```

---

## Usage

### Basic

```bash
python3 blur.py 2918
```

### Advanced

```bash
# Specify input directory
python3 blur.py 2918 --input_dir /path/to/images

# Specify output directory
python3 blur.py 2918 --output_dir /path/to/output

# Specify model path
python3 blur.py 2918 --model best.pt
```

---

## How It Works

1. Load YOLOv5 model  
2. Read image  
3. Detect license plates  
4. Extract bounding boxes  
5. Apply Gaussian blur  
6. Save output  

---

## Requirements

- Python 3.10
- Linux / WSL recommended
- CUDA optional

---

## Important Notes

- Do NOT use PyTorch 2.6+ (breaking changes)
- Ensure torch / torchvision version compatibility

---

## Troubleshooting

### PyTorch 2.6+ Error

```
_pickle.UnpicklingError: Weights only load failed
```

Fix:

```bash
pip install torch==2.5.1 torchvision==0.20.1
```

---

### torchvision NMS Error

```
RuntimeError: operator torchvision::nms does not exist
```

Fix:

```bash
pip install torch==2.5.1 torchvision==0.20.1
```

---

### torch.hub Issue (avoid)

Use:

```python
from yolov5 import load
model = load("best.pt")
```

---

### Hugging Face 401 Error

```bash
hf auth login
```

---

## Security

This project loads `.pt` files via PyTorch.

Only use trusted models to avoid risks from malicious pickle data.

---

## Future Improvements

- Batch processing
- Video support
- Face + plate anonymization
- Confidence tuning
- Web UI / API

---

## License

MIT License

---

## Author

- X: https://x.com/seikato  
- LinkedIn: https://www.linkedin.com/in/seikato/