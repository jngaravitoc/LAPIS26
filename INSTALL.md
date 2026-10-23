# Installation guide

The tutorials and projects use **[Gala](https://gala.adrian.pw)**, a Python package for galactic dynamics: gravitational potentials, orbit integration, and coordinate transformations. It also uses the standard scientific Python stack (numpy, scipy, matplotlib, astropy) and Jupyter.

Gala ships as pre-compiled wheels for Linux and macOS, so a normal `pip install` is enough and you don't need a compiler. Please **finish the installation before the school starts**, so any problems can be fixed ahead of time instead of during a tutorial.

---

## 0. What you need

| | Linux | macOS | Windows |
|---|---|---|---|
| Python | 3.11 or 3.12 (recommended) | 3.11 or 3.12 | Use [WSL](https://learn.microsoft.com/windows/wsl/install) and follow the Linux instructions |

**Python 3.12** is the safest choice. You don't need a GPU.

---

## 1. Create a Python environment

Use a separate environment called `lapis-xmc` for the school so it won't conflict with other projects. Pick **one** of the two options below.

### Option A: conda / mamba (recommended)

If you don't have conda yet, install [Miniforge](https://github.com/conda-forge/miniforge#install).

```bash
conda create -n lapis-xmc python=3.12
conda activate lapis-xmc
```

### Option B: venv

This needs Python 3.11 or 3.12 already installed on your system.

```bash
python3 -m venv ~/venvs/lapis-xmc
source ~/venvs/lapis-xmc/bin/activate
```

**Activate this environment** (`conda activate lapis-xmc` or `source ~/venvs/lapis-xmc/bin/activate`) every time you open a new terminal to work on the tutorials.

---

## 2. Install the Python packages

Clone this repository and install the requirements (this includes Gala):

```bash
git clone https://github.com/jngaravitoc/LAPIS26.git
cd LAPIS26
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 3. Check the installation

From the `LAPIS26` folder, run:

```bash
python check_install.py
```

When everything works, every line shows `[ OK ]` and the script ends with `All good!`. Lines marked `[ -- ]` are optional packages, and it's fine if they're missing.

To make the environment available in Jupyter as a kernel named "lapis-xmc":

```bash
python -m ipykernel install --user --name lapis-xmc --display-name "lapis-xmc"
```

Then start Jupyter with `jupyter lab` and select the **lapis-xmc** kernel in the notebooks.

---

## Optional extras

You **don't need** these for the tutorials.

**healpy** is used for Mollweide sky projections: `pip install healpy`

---

## Troubleshooting

| Problem | Solution |
|---|---|
| `pip` tries to compile Gala from source and fails | There is no pre-built wheel for your Python version. Create the environment with `python=3.12`. With conda you can also run `conda install -c conda-forge gala`. |
| `ModuleNotFoundError: No module named 'gala'` in Jupyter | Jupyter is using a different Python. Install the kernel ([step 3](#3-check-the-installation)) and select "lapis-xmc" in the notebook. |
| `ModuleNotFoundError` in the terminal | The environment is not active. Run `conda activate lapis-xmc` (or `source ~/venvs/lapis-xmc/bin/activate`). |
| macOS: architecture errors on Apple Silicon | Use a native arm64 Python (Miniforge provides one) and not an x86 Python running under Rosetta. |
| Anything else | Copy the **full** error message and bring it to the installation help session or send it to the organizers. |

For more detail, see the [Gala installation instructions](https://gala.adrian.pw/en/latest/install.html).
