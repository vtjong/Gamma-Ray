import sys
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
from plotter import prettyplot, visualize

def process(file, sheet_name, print_flag=True):
    df = pd.read_excel(file, sheet_name=sheet_name, 
        usecols=['Orientation (1/2)', 'Absorber Thickness (cm)','ln(I)','δ_tot'])
    data = np.array(df)
    y_dat, err_dat = data[:,:3], data[1:,3]
    ln_I_0 = y_dat[0,2]
    geoms = set(y_dat[:,0])

    # Get rid of ln(I_0) row
    y_dat = y_dat[1:]     
    
    # Iterate through all orientations
    for geom in list(geoms):
        ln_I = y_dat[np.where(y_dat[:,0]==geom)][:,1:]
        ln_I[:,1] = np.abs(ln_I[:,1]-ln_I_0)
        mu, cv = mu_fit(ln_I)
        save_it_up(sheet_name, mu, cv, geom, filename='stats.csv')
        if geom==1.0:
            err_dat[:4]
        else:
            err_dat[4:]
        if print_flag:
            visualize(ln_I, err_dat, mu, geom, sheet_name)

def f_mu (x,mu): return mu*x

def mu_fit(ln_I):
    xs = ln_I[:,0]
    ys = ln_I[:,1]
    p0 = (1.0) # start with values near those we expect
    mu, cv = curve_fit(f_mu, xs, ys, p0)   # linear least squares
    return mu.item(), cv

def stat_err(cv): return np.sqrt(np.diag(cv)).item()

def save_it_up(sheet_name, mu, cv, geom, filename='stats.csv'):
    file = open(filename, "a", encoding="utf-8")
    file.write(sheet_name + " " + str(geom) + " : " + str(mu) + "\n" + 
            "stat error: " + str(stat_err(cv)) + "\n")

def main():
    prettyplot()
    file = '/Users/valenetjong/Desktop/PHYS 3310/GammaRay/data/dat.xlsx'
    sheets = ['Al', 'Cu','Pb']
    for sheet_name in sheets: 
        process(file, sheet_name)

main()