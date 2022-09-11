import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

def prettyplot():
    """
    prettyplot()——some aesthetically pleasing settings. 
    """
    plt.style.use('seaborn')
    mpl.rcParams['lines.linewidth'] = 1.5
    plt.rcParams['figure.dpi'] = 200

def visualize(ln_I, err_dat, mu_pred, geom, sheet_name):
    plt.clf()
    xs, ys = ln_I[:,0], ln_I[:,1]
    plt.plot(xs, mu_pred*xs, c = '#A9561E', 
    label = "fit, mu= " + str(round(mu_pred,3)))
    plt.plot(xs, ys, '-o', c = '#580F41', label = "raw")
    
    # Create error bars
    y_ebars = [(y_i-err_i, y_i+err_i) for y_i,err_i in zip(list(ys), list(err_dat))]
    for i in range(len(y_ebars)):
        plt.vlines(x=xs[i], ymin=y_ebars[i][0], ymax=y_ebars[i][1], colors = "grey")

    plt.xlabel('Absorber Thickness (cm)')
    plt.ylabel('|ln((I-Ib)/I0)|')
    dir = '/Users/valenetjong/Desktop/PHYS 3310/GammaRay/plots'
    plt.title(sheet_name + ' Orientation '+ str(geom))
    plt.legend(loc="upper right",frameon= True, facecolor="white", framealpha = 0.75)
    plt.savefig(dir + "/" + sheet_name + "/" + str(geom)+ '.png')   

