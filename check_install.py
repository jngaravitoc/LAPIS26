"""Check that the LAPIS26 software environment is installed correctly.

Usage:  python check_install.py
"""
import importlib
import sys

REQUIRED = ["numpy", "scipy", "matplotlib", "h5py", "astropy", "pandas", "gala"]
OPTIONAL = ["healpy"]

failed = False
print(f"Python {sys.version.split()[0]}")
if not (3, 11) <= sys.version_info[:2] <= (3, 13):
    print("[FAIL] Python version should be between 3.11 and 3.13")
    failed = True

for name in REQUIRED + OPTIONAL:
    try:
        mod = importlib.import_module(name)
        print(f"[ OK ] {name:14s} {getattr(mod, '__version__', '')}")
    except Exception as e:
        if name in REQUIRED:
            print(f"[FAIL] {name:14s} {type(e).__name__}: {e}")
            failed = True
        else:
            print(f"[ -- ] {name:14s} not installed (optional)")

if not failed:
    # Quick functional test: orbit integration in a Gala potential
    import numpy as np
    import astropy.units as u
    import gala.dynamics as gd
    import gala.potential as gp
    from gala.units import galactic

    pot = gp.NFWPotential(m=1e12 * u.Msun, r_s=20 * u.kpc, units=galactic)
    w0 = gd.PhaseSpacePosition(pos=[8, 0, 0] * u.kpc,
                               vel=[0, 200, 0] * u.km / u.s)
    orbit = gp.Hamiltonian(pot).integrate_orbit(
        w0, dt=0.5 * u.Myr, n_steps=2000, Integrator="dopri853")
    energy = orbit.energy()
    if np.ptp(energy) / abs(energy[0]) > 1e-6:
        print("[FAIL] Gala orbit integration does not conserve energy")
        failed = True
    else:
        print("[ OK ] Gala orbit integration")

print("\nSomething is wrong, see INSTALL.md > Troubleshooting." if failed
      else "\nAll good!")
sys.exit(int(failed))
