"""Check that the LAPIS26 software environment is installed correctly.

Usage:  python check_install.py
"""
import importlib
import sys

REQUIRED = ["numpy", "scipy", "matplotlib", "h5py", "numba", "astropy",
            "agama", "nbody_streams"]
OPTIONAL = ["cvxopt", "pyfalcon", "healpy", "cupy"]

failed = False
print(f"Python {sys.version.split()[0]}")
if not (3, 10) <= sys.version_info[:2] <= (3, 13):
    print("[FAIL] Python version should be between 3.10 and 3.13")
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
    # Quick functional test: orbit integration in an Agama potential
    import numpy as np
    import agama
    agama.setUnits(mass=1, length=1, velocity=1)
    pot = agama.Potential(type="NFW", mass=1e12, scaleRadius=20)
    orbit = agama.orbit(potential=pot, ic=[8, 0, 0, 0, 200, 0],
                        time=1.0, trajsize=100)
    energy = pot.potential(orbit[1][:, :3]) + 0.5 * np.sum(orbit[1][:, 3:]**2, axis=1)
    if np.ptp(energy) / abs(energy[0]) > 1e-6:
        print("[FAIL] Agama orbit integration does not conserve energy")
        failed = True
    else:
        print("[ OK ] Agama orbit integration")

print("\nSomething is wrong, see INSTALL.md > Troubleshooting." if failed
      else "\nAll good!")
sys.exit(int(failed))
