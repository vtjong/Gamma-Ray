import matplotlib as mpl
import matplotlib.pyplot as plt

def prettyplot():
    """
    prettyplot()——some aesthetically pleasing settings. 
    """
    plt.style.use('seaborn')
    mpl.rcParams['lines.linewidth'] = 1.5
    plt.rcParams['figure.dpi'] = 200

def visualize(ln_I, mu_pred, geom, sheet_name):
    plt.clf()
    plt.plot(ln_I[:,0], mu_pred*ln_I[:,0], c = '#A9561E', 
    label = "fit, mu= " + str(round(mu_pred,3)))
    plt.plot(ln_I[:,0], ln_I[:,1], '-o', c = '#580F41', label = "raw")

    plt.xlabel('Absorber Thickness (cm)')
    plt.ylabel('|ln((I-Ib)/I0)|')
    dir = '/Users/valenetjong/Desktop/PHYS 3310/GammaRay/plots'
    plt.title(sheet_name + ' Orientation '+ str(geom))
    plt.legend(loc="upper right",frameon= True, facecolor="white", framealpha = 0.75)
    plt.savefig(dir + "/" + sheet_name + "/" + str(geom)+ '.png')   

