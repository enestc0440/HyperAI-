import torch
import torch.nn as nn
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split

class HyperMind(nn.Module):
    def __init__(self):
        super(HyperMind, self).__init__()
        self.fc1 = nn.Linear(10, 64)
        self.fc2 = nn.Linear(64, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

    def train_model(self, epochs=100):
        data = load_diabetes()
        X, y = data.data, data.target
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        X_train = torch.FloatTensor(X_train)
        y_train = torch.FloatTensor(y_train).view(-1, 1)

        criterion = nn.MSELoss()
        optimizer = torch.optim.Adam(self.parameters(), lr=0.01)

        for epoch in range(epochs):
            optimizer.zero_grad()
            outputs = self(X_train)
            loss = criterion(outputs, y_train)
            loss.backward()
            optimizer.step()

        return f"Eğitim Tamamlandı! Son Kayıp: {loss.item():.4f}"
