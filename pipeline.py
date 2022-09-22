
import pandas as pd
import lightgbm as lgb

def train():
    print("train")
    ds = lgb.Dataset(data=[1, 2])
    print(ds)


def predict():
    print("predict")
    pass


train()