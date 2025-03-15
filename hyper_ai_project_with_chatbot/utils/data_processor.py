import pandas as pd

class DataProcessor:
    def __init__(self, data):
        self.data = pd.DataFrame(data)

    def normalize(self):
        return (self.data - self.data.mean()) / self.data.std()
