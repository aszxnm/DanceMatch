import os
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms as T
import json
import numpy as np


class DanceDataloader(Dataset):

    def __init__(self, root, args, transforms=None, train=True, test=False):
        self.test = test

        with open(root, "r+") as fhandle:
            data = json.load(fhandle)

        data_com_1 = []
        data_com_2 = []
        for _, (data_input, data_target) in data.items():
            data_com_1.append(data_input)
            data_com_2.append(data_target)

        data = data_com_1
        data = np.array(data)
        data = data.reshape((-1, (24 + args.num_node*3) * args.len_seg))
        data_num = len(data)

        data_com_2 = np.array(data_com_2)
        data_com_2 = data_com_2.flatten()

        self.label = data_com_2
        if self.test:
            self.data = data
        elif train:
            self.data = data[:int(0.8 * data_num), :]
        else:
            self.data = data[int(0.8 * data_num):, :]

    def __getitem__(self, index):

        label = self.label[index]
        data = self.data[index]

        return data, label

    def __len__(self):
        return len(self.data)

