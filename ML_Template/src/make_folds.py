import pandas as pd
from sklearn import model_selection
#import argparse
#perform k fold cross validation







if name =="__main__":
    df = pd.read_csv('inputs/train.csv')

    #df.sample() returns a RANDOM sample from df or a row of df. You can set frac=some fraction 
    #to return a sample of frac*100 % of the data. 
    #therefore, df.sample(frac=1), ruturns a sample of size 100% of the data, i.e. it just shuffles the df
    #Doing "reset_index(drop=True)" returns the indeces to their original ones
    df = df.sample(frac=1).reset_index(drop=True)
    k_fold = model_selection.StratifiedKFold(n_splits=5, shuffle=False, random_state=22)
    
