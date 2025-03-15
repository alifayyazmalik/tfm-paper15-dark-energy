# TFM Paper #15: Dark Energy as Emergent Stochastic Time Field Dynamics

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.XXXXXXX.svg)](https://doi.org/10.XXXX/zenodo.XXXXXXX)

Reproduces all results from:  
**"Dark Energy as Emergent Stochastic Time Field Dynamics: Micro--Big Bangs, Wave-Lump Expansion, and the End of Λ"**

---

## Key Features
- 🌌 **No cosmological constant** - Dark energy emerges from time wave dynamics
- 📈 **Oscillatory equation of state** \( w(z) = -1 + \delta_w \sin(\omega z) \)
- ⚡ **HPC-ready cosmic acceleration simulations**
- 📡 **Observational tests** against Planck, DESI, and NANOGrav data

---

## Quick Start
```bash
# Clone repository
git clone https://github.com/alifayyazmalik/tfm-paper15-dark-energy.git
cd tfm-paper15-dark-energy

# Install dependencies
pip install -r requirements.txt

# Run basic validation (requires pytest)
python -m pytest tests/
```

## Full Validation Guide | Cite This Work

---

## Repository Structure
| Directory  | Contents                                      |
|------------|----------------------------------------------|
| `code/`    | HPC simulations & modified CLASS code       |
| `data/`    | Observational datasets (Planck/DESI/NANOGrav) |
| `docs/`    | Validation guide & derivation notebooks     |
| `figures/` | Auto-generated publication figures          |

## Key Components
### 1. Modified CLASS Boltzmann Solver
```
code/boltzmann_solver/TFM-CLASS/
```
Custom modifications to compute TFM’s CMB power spectrum \( C_\ell^{\text{TFM}} \).

### 2. HPC Parameter Files
```yaml
# Example configuration (params/cosmic_accel_params.yaml)
alpha: 0.1       # Time wave dissipation rate
beta: 14.8       # Wave-lump correlation length (kpc)
Gamma: 1e-5      # Micro-Big Bang rate
H0: 72.0         # Initial Hubble parameter
```

### 3. Automated Figure Generation
Jupyter notebooks in `docs/derivations/` regenerate all paper figures:
```bash
jupyter notebook docs/derivations/AppendixA_Derivations.ipynb
```

---

## Support
- **Report issues:** [GitHub Issues](https://github.com/alifayyazmalik/tfm-paper15-dark-energy/issues)
- **Request features:** [Discussion Board](https://github.com/alifayyazmalik/tfm-paper15-dark-energy/discussions)
