import pandas as pd
import logging

def get_training_data():
    logging.info("Loading training data...")
    return pd.read_csv("/kaggle/input/facial-keypoints-detection/training.zip")
