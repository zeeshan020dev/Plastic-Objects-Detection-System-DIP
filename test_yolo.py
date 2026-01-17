from ultralytics import YOLO

# Load your local model
model = YOLO("best.pt")

# Run prediction on an image
results = model.predict("test.jpeg", save=True, conf=0.5)

print("Prediction complete! Output saved.")
