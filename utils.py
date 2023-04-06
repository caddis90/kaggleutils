import pandas as pd

def get_training_data():
    print("Getting training data")
    print("Updated")
    return pd.read_csv("/kaggle/input/facial-keypoints-detection/training.zip")
