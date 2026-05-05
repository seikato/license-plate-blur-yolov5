import cv2
import argparse
import os
from yolov5 import load


def parse_args():
    """
    Parse command line arguments.
    """
    parser = argparse.ArgumentParser(description="License plate detection and blurring tool")
    
    parser.add_argument(
        "image_id",
        type=str,
        help="Image ID (e.g. 2918 for DSC02918.JPG)"
    )

    parser.add_argument(
        "--input_dir",
        type=str,
        default="/mnt/c/home/40_photo/2026-01-03",
        help="Directory containing input images"
    )

    parser.add_argument(
        "--model",
        type=str,
        default="best.pt",
        help="Path to YOLOv5 model file"
    )

    parser.add_argument(
        "--output_dir",
        type=str,
        default=None,
        help="Directory to save output images (default: same as input_dir)"
    )

    return parser.parse_args()


def build_paths(input_dir, output_dir, image_id):
    """
    Build input and output file paths.
    """
    if output_dir is None:
        output_dir = input_dir

    filename = f"DSC0{image_id}.JPG"
    input_path = os.path.join(input_dir, filename)
    output_path = os.path.join(output_dir, f"output_{image_id}.jpg")

    return input_path, output_path


def main():
    args = parse_args()

    # Build file paths
    input_path, output_path = build_paths(
        args.input_dir,
        args.output_dir,
        args.image_id
    )

    # Load YOLOv5 model
    model = load(args.model)

    # Read image
    img = cv2.imread(input_path)
    if img is None:
        raise FileNotFoundError(f"Image not found: {input_path}")

    # Run inference
    results = model(img)

    # Apply blur to detected bounding boxes
    for *box, conf, cls in results.xyxy[0]:
        x1, y1, x2, y2 = map(int, box)

        # Extract region of interest (ROI)
        roi = img[y1:y2, x1:x2]

        if roi.size == 0:
            continue

        # Apply Gaussian blur
        blurred = cv2.GaussianBlur(roi, (31, 31), 0)
        img[y1:y2, x1:x2] = blurred

    # Save result image
    cv2.imwrite(output_path, img)

    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
