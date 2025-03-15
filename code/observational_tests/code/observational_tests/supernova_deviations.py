import numpy as np
import pandas as pd

def predict_sn_deviations(z, delta_w=0.01, omega=0.02):
    """
    Calculates supernova magnitude deviations (Eq. 8)
    """
    return 0.02 * np.sin(omega * z)

# Example usage with DESI mock data
desi_data = pd.read_csv("../data/observational/desi_supernovae.csv")
z = desi_data['redshift'].values
dm_tfm = predict_sn_deviations(z)
