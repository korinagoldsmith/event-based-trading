import os

def save_to_csv(data, filename):
    filepath = os.path.join("data", "processed", filename)
    data.to_csv(filepath)