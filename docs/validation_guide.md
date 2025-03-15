# Validation Guide for TFM Dark Energy Predictions

## 1. Reproduce Hubble Tension Resolution
```bash
python code/hpc_simulations/cosmic_acceleration.py \
  --alpha 0.1 \
  --beta 14.8 \
  --Gamma 1e-5
```
**Expected Output**:  
`H0 = 72.1 ± 0.3 km/s/Mpc`

## 2. Generate Supernova Deviations Plot
```python
from observational_tests import supernova_deviations as sn

sn.plot_deviation_comparison()  # Saves to figures/sn_deviations.pdf
```

## 3. Gravitational Wave Background Prediction
```python
from observational_tests.gravitational_waves import calculate_OmegaGW

frequencies = np.logspace(-9, -6, 100)  # nHz to μHz
Omega_GW = calculate_OmegaGW(frequencies)
plt.loglog(frequencies, Omega_GW)
plt.savefig('figures/gw_background.pdf')
```
