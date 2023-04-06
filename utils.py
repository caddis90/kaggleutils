import pandas as pd

def get_training_data():
    print("Loading training data...")
    return pd.read_csv("/kaggle/input/facial-keypoints-detection/training.zip")
