import torch
import torch.nn as nn
import torchvision
from torchvision import transforms
print("Is GPU used (bool):-",torch.cuda.is_available())

class LeNet5(nn.Module):
  def __init__(self,input_channels=1,classes=10): #input_channels=1 for grey scale img , 3 for RGB
    super().__init__()
    self.c1 = nn.Conv2d(in_channels=input_channels,out_channels=6,kernel_size=5,stride=1,padding=2)
    self.conv2 = nn.Conv2d(in_channels=6,out_channels=16,kernel_size=5,stride=1,padding=0)
    self.conv3 = nn.Conv2d(in_channels=16,out_channels=120,kernel_size=5,stride=1,padding=0)
    self.relu = nn.ReLU()
    self.maxpool = nn.MaxPool2d(kernel_size=2,stride=2)
    self.fc1=nn.Linear(in_features=120,out_features=84)
    self.fc2=nn.Linear(in_features=84,out_features=classes)

  # forward pass
  def forward(self,img):
    # img Shape:[batch,1,28,28]
    x = self.c1(img)
    # x shape :[batch,6,28,28]
    x = self.relu(self.maxpool(x)) # SubSampling 1
    # x Shape:[batch,6,14,14]
    x = self.conv2(x)
    # x shape :[batch,6,10,10]
    x = self.relu(self.maxpool(x)) # SubSampling 2
    # x shape :[batch,16,5,5]
    x = self.relu(self.conv3(x))
    # x shape : [batch,120,1,1]
    x = torch.flatten(x,1)
    # x shape :[batch,120]
    x = self.relu(self.fc1(x))
    # x shape : [batch,84]
    x = self.fc2(x)
    # x shape : [batch,10]
    return x

# Model Summary
model = LeNet5()
model(torch.randn(16,1,28,28)).shape
# Output Must be [batch,10]