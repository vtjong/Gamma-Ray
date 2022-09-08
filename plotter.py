import matplotlib as mpl
import matplotlib.pyplot as plt

def prettyplot():
    """
    prettyplot()——some aesthetically pleasing settings. 
    """
    plt.style.use('seaborn')
    mpl.rcParams['lines.linewidth'] = 1.5
    plt.rcParams['figure.dpi'] = 200

def visualize(ln_I, fit, angle, sheet_name):
    coeff, y_int = fit[0], fit[1]
    plt.clf()
    plt.plot(ln_I[:,0], coeff*ln_I[:,0] + y_int, c = '#A9561E', 
    label = "fit, alpha= " + str(round(coeff,3)))
    plt.plot(ln_I[:,0], ln_I[:,1], '-o', c = '#580F41', label = "raw")
    plt.xlabel('Absorber Thickness (cm)')
    plt.ylabel('ln(I)')
    dir = '/Users/valenetjong/Desktop/PHYS 3310/GammaRay/plots'
    plt.title(sheet_name + ' '+ str(angle) + ' deg')
    plt.legend(loc="upper right",frameon= True, facecolor="white", framealpha = 0.75)
    plt.savefig(dir + "/" + sheet_name + "/" + str(angle)+ '.png')   
