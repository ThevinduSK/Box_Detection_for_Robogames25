import subprocess

# Path to your data.yaml file
yaml_path = "C:\Repositories\Robogames_final-working-with-Kobuki-robot-\Box detection model\dataset\dataset\data.yaml"  # ⬅️ Replace this!

# Training command
command = [
    "python",
    "train.py",
    "--img",
    "416",
    "--batch",
    "16",
    "--epochs",
    "100",
    "--data",
    yaml_path,
    "--cfg",
    "models/yolov5n.yaml",
    "--weights",
    "yolov5n.pt",
    "--name",
    "cardboard-detector",
]

# Run training
subprocess.run(command)
