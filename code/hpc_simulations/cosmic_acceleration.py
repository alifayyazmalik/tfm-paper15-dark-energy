import numpy as np
from astropy import units as u
from scipy.stats import levy_stable

def TFM_friedmann(z, alpha, beta, Gamma):
    """
    Solves TFM-modified Friedmann equation (Eq. 2)
    """
    H0 = 72 * u.km / u.s / u.Mpc
    Omega_m = 0.31
    rho_T = (beta**2 / (2 * alpha)) * (1 - np.exp(-2 * alpha * z)) 
    rho_T += Gamma * beta**2 * np.sum([np.cos(n * 0.02 * z) for n in range(1,5)])
    
    H_sq = (H0**2) * (Omega_m * (1 + z)**3 + rho_T)
    return np.sqrt(H_sq)
