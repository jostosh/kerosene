# -*- coding: utf-8 -*-
import fuel.datasets
from .dataset import Dataset
import os

class MNIST(Dataset):
    basename = "mnist"
    class_for_filename_patch = fuel.datasets.MNIST

    def build_data(self, sets, sources):
        return map(lambda s: fuel.datasets.MNIST(which_sets=[s], sources=sources), sets)

def load_data(sets=None, sources=None, fuel_dir=False, datadir=os.path.join(os.path.expanduser('~'), '.kerosene/datasets')):
    return MNIST().load_data(sets, sources, fuel_dir, datadir=datadir)
