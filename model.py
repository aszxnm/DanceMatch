import torch
import torch.nn as nn
import torch.nn.parallel
import torch.nn.init as init
from torch.autograd import Variable
from utils.tgcn import ConvTemporalGraphical
from utils.graph import Graph
import torch.nn.functional as F

if torch.cuda.is_available():
    T = torch.cuda
else:
    T = torch

class DanceTransModel(nn.Module):
    def __init__(self, args, flag=0, in_channels=1, edge_importance_weighting=True):
        super(DanceTransModel, self).__init__()

    def forward(self, inputs):
        return 
