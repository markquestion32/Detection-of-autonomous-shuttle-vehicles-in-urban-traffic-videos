import subprocess
import torch
def train_yolov10(epochs, batch_size, model_path, imgsz, data_path, plots=True, device=0):
    """Trains a YOLOv10 model using the provided parameters."""

    command = [
        "yolo", 
        "task=detect",
        "mode=train",
        f"epochs={epochs}",
        f"batch={batch_size}",
        f"plots={'True' if plots else 'False'}",
        f"model={model_path}",
        f"data={data_path}",
        f"device={device}",
        f"imgsz={imgsz}"
    ]

    # Run the command in the terminal and stream the output
    with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True,encoding='utf-8') as process:
        for line in process.stdout:
            print(line, end='')  # Print each line of output as it comes

    # Check if the training was successful (this will only be checked after the process completes)
    if process.returncode == 0:
        print("YOLOv10 training completed successfully!")
    else:
        print("Error during YOLOv10 training:")


# Set your training parameters
epochs = 50
imgsz = 416
batch_size = 16
model_path = 'C:/Users/Lenovo/Desktop/yolov10/yolov10x.pt'  # Adjust if needed
data_path = 'config.yaml'  # Make sure this is your YAML config file
device = 0  # GPU device (0 if you have a single GPU)

# Start the training
train_yolov10(epochs, batch_size, model_path, imgsz, data_path, device=device)
