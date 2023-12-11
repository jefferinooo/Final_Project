# Import necessary packages and functions from module

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys

from analysis_functions import filter_dataset
from analysis_functions import find_PRA
from analysis_functions import filter_by_season


df = pd.read_csv('Final_Project/modules/per_game_stats.csv')

# Test filter_dataset function
def test_filter_dataset():
    # Definining datasets
    lebron = filter_dataset('Lebron James')
    kobe = filter_dataset('Kobe Bryant')
    jordan = filter_dataset('Michael Jordan')
    
    assert lebron.shape == (29, 6)
    assert kobe.shape == (35, 6)
    assert jordan.shape == (28, 6)
    
# Test find_PRA function
def test_find_PRA():
    lebron_reg = find_PRA('Lebron James', 'Regular Season')
    kobe_reg = find_PRA('Kobe Bryant', 'Regular Season')
    jordan_reg = find_PRA('Michael Jordan', 'Regular Season')
    
    lebron_playoffs = find_PRA('Lebron James', 'Playoffs')
    kobe_playoffs = find_PRA('Kobe Bryant', 'Playoffs')
    jordan_playoffs = find_PRA('Michael Jordan', 'Playoffs')
    
    assert lebron_reg.shape == (16,6)
    assert kobe_reg.shape == (20, 6)
    assert jordan_reg.shape == (15, 6)
    assert lebron_playoffs.shape == (13, 6)
    assert kobe_playoffs.shape == (15, 6)
    assert jordan_playoffs.shape == (13, 6)

def test_filter_by_season():
    assert filter_by_season('Regular Season').shape == (51, 6)
    assert filter_by_season('Playoffs').shape == (41, 6)

print('Tests complete')
