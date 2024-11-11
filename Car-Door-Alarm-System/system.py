import random

def detect_movement():
    movement_detected = random.choice([True, False])
    print(f"Movement Detected: {movement_detected}")
    return movement_detected

def detect_heat(threshold):
    temperature = random.uniform(20.0, 50.0)
    heat_detected = temperature > threshold
    print(f"Temperature Detected: {temperature:.2f}°C - Above Threshold: {heat_detected}")
    return heat_detected
