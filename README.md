# LAPIS26

Material for the lectures "Galactic mergers in our backyard: The Milky Way's interaction with its more massive satellites, the LMC and the SMC", given at the [XII LAPIS 2026 school](https://congresos.unlp.edu.ar/xiilapis2026/).

## Installation

The tutorials and projects use [Gala](https://gala.adrian.pw) and the standard scientific Python stack. Follow the steps in the **[installation guide](https://github.com/jngaravitoc/LAPIS26/blob/main/INSTALL.md)**. In short, with Python 3.12:

```bash
conda create -n lapis-xmc python=3.12        # or: python3 -m venv ~/venvs/lapis-xmc
conda activate lapis-xmc                     # or: source ~/venvs/lapis-xmc/bin/activate
git clone https://github.com/jngaravitoc/LAPIS26.git
cd LAPIS26
pip install --upgrade pip
pip install -r requirements.txt
python check_install.py
python -m ipykernel install --user --name lapis-xmc --display-name "lapis-xmc"
```

`check_install.py` should end with `All good!`. Then start Jupyter with `jupyter lab` and select the **lapis-xmc** kernel in the notebooks. Please finish the installation **before the school starts**.

If you encounter any issues or errors in the installation guide, please don't hesitate to open an [issue](https://github.com/jngaravitoc/LAPIS26/issues) or email me.

## Lectures

TBD

## Tutorials

The tutorial notebooks in [`projects/`](https://github.com/jngaravitoc/LAPIS26/tree/main/projects) are the starting point for the projects:

- **[Dynamical friction in `gala`: the LMC orbit around the Milky Way](https://github.com/jngaravitoc/LAPIS26/blob/main/projects/dynamical_friction_MWLMC_tutorial.ipynb):** build the MW and LMC potentials, add Chandrasekhar dynamical friction to a `gala` integration, and integrate the LMC orbit as a test particle and in a live MW + LMC system. It ends with a test particle integrated in the inertial frame and in the (non-inertial) frame of the MW disk.
- **[Stellar stream evolution in the MW + LMC system](https://github.com/jngaravitoc/LAPIS26/blob/main/projects/stream_evolution.ipynb):** generate mock streams with `gala`'s `MockStreamGenerator` in time-dependent potentials, and separate the effect of the LMC's direct pull from that of the MW's reflex motion.

## Projects

- **[Project 1: Orbits of the Milky Way satellite galaxies](https://github.com/jngaravitoc/LAPIS26/blob/main/projects/project_1_satellite_orbits.md):** integrate the orbits of the MW satellites (from the Local Volume Database) backwards in time in an isolated MW, in a MW + LMC system, and in a moving MW frame. Find which satellites came with the LMC, which are long-term MW satellites, and which are on first infall.
- **[Project 2: Revealing the origin of hypervelocity stars](https://github.com/jngaravitoc/LAPIS26/blob/main/projects/project_2_HVS_origin.md):** integrate the orbits of 16 hypervelocity star candidates backwards, with and without the LMC, and find out whether they come from the Galactic Centre, the LMC, a satellite galaxy or a globular cluster, or share a common origin.
- **[Project 3: Stellar streams as probes of the LMC and the Milky Way's reflex motion](https://github.com/jngaravitoc/LAPIS26/blob/main/projects/project_3_streams.md):** generate mock streams of different lengths (up to two wraps around the MW) on many orbits, and measure how the LMC's direct pull and the MW's reflex motion perturb them (proper-motion misalignment, orbital poles, plane tilt). Make predictions for LSST.

## References

See the **[references file](https://github.com/jngaravitoc/LAPIS26/blob/main/references.md)** for the reading list for the lectures and projects.
