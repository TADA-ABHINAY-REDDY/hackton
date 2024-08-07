import cv2
import numpy as np

def assess_light_condition(frame, threshold=50):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mean_intensity = np.mean(gray)
    return 'Low' if mean_intensity < threshold else 'Normal'
