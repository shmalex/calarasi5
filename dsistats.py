import numpy as np
import pandas as pd
import math as m


def RSS(y, y_hat):
    return np.sum((y - y_hat)**2)


def RSE(y, y_hat):
    return m.sqrt(RSS(y, y_hat) / (len(y) - 2))


def TSS(y):

    return np.sum((y - np.mean(y))**2)


def Rsquere(y, y_hat):
    rss = RSS(y, y_hat)
    tss = TSS(y_hat)
    return (tss-rss)/tss


def yn_to_bool(df, col, yes='Yes', no='No'):
    df.loc[df[col] == yes, col] = 1
    df.loc[df[col] == no, col] = 0
