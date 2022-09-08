import pandas as pd
import numpy as np
from plotter import prettyplot, visualize

def process(file, sheet_name, print_flag=True):
    df = pd.read_excel(file, sheet_name=sheet_name, 
        usecols=['Angle (degrees)', 'Absorber Thickness (cm)','ln(I)'])
    data = np.array(df)
    ln_I_0 = data[0,2]
    angles = set(data[:,0])

    # Get rid of ln(I_0) row
    data = data[1:]     
    
    # Iterate through for three different angles
    for angle in list(angles):
        ln_I = data[np.where(data[:,0]==angle)][:,1:]
        ln_I[:,1] = np.abs(ln_I[:,1]-ln_I_0)
        fit = np.polyfit(ln_I[:,0], ln_I[:,1],1)
        visualize(ln_I, fit, angle, sheet_name)

def main():
    prettyplot()
    file = '/Users/valenetjong/Desktop/PHYS 3310/GammaRay/data/dat-14.xlsx'
    sheets = ['Al', 'Cu','Pb']
    for sheet_name in sheets: 
        process(file, sheet_name)

main()