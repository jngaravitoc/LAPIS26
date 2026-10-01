# Installation guide

The lectures and tutorials use two packages:

- **[Agama](https://github.com/GalacticDynamics-Oxford/Agama)**: a library for galaxy modelling (potentials, orbits, actions, distribution functions).
- **[nbody_streams](https://github.com/appy2806/Nbody_streams)**: an N-body simulator and set of tools for stellar streams. It uses Agama for external potentials and for fast stream generation.

Both include C/C++ code that is compiled on your machine, so you need a working compiler. Please **finish the installation before the school starts**. Compiling Agama takes 5–15 minutes, and problems are much easier to fix ahead of time than during a tutorial.

---

## 0. What you need

| | Linux | macOS |
|---|---|---|
| C/C++ compiler | `gcc`/`g++` | Xcode Command Line Tools (`clang`) |
| Python | 3.11 or 3.12 (recommended) | 3.11 or 3.12 |

Why these Python versions: Agama needs Python ≥ 3.10 to install with `pip`, and nbody_streams does not support anything newer than 3.13. **Python 3.12** is the safest choice.

You don't need a GPU. Everything in the tutorials runs on a CPU. The GPU backends of nbody_streams are optional (see [Optional extras](#optional-extras)).

---

## 1. Install system tools

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install build-essential git wget libgsl-dev
```

On Fedora, use `sudo dnf install gcc gcc-c++ make git wget gsl-devel`.

### macOS

```bash
xcode-select --install          # C/C++ compiler and git
```

With [Homebrew](https://brew.sh) you can also run `brew install gsl wget`. This is optional, because Agama downloads and compiles GSL itself if it can't find it.

---

## 2. Create a Python environment

Use a separate environment for the school so it won't conflict with other projects. Pick **one** of the two options below.

### Option A: conda / mamba (recommended)

If you don't have conda yet, install [Miniforge](https://github.com/conda-forge/miniforge#install).

```bash
conda create -n mwlmc python=3.12
conda activate mwlmc
```

### Option B: venv

This needs Python 3.11 or 3.12 already installed on your system.

```bash
python3 -m venv ~/venvs/mwlmc
source ~/venvs/mwlmc/bin/activate
```

> **Ubuntu/Debian + venv:** if the system package `python3-numpy` is installed (check with `dpkg -l python3-numpy`), its old numpy headers can end up in the Agama build. Agama then fails with *"A module that was compiled using NumPy 1.x cannot be run in NumPy 2.x"*. To avoid this, either use conda, or run `pip install "numpy<2"` after step 3 and before installing Agama.

**Activate this environment** (`conda activate mwlmc` or `source ~/venvs/mwlmc/bin/activate`) every time you open a new terminal to work on the tutorials.

---

## 3. Install the Python dependencies

Clone this repository and install the requirements:

```bash
git clone https://github.com/jngaravitoc/LAPIS26.git
cd LAPIS26
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 4. Install Agama

```bash
pip install --no-build-isolation -v \
    "agama @ git+https://github.com/GalacticDynamics-Oxford/Agama.git" \
    --config-settings --build-option=--yes
```

- `--no-build-isolation` lets the build use the numpy you just installed. Without it the build fails with *"NumPy is not present"*.
- `--build-option=--yes` automatically accepts Agama's offers to download extra libraries (GSL, Eigen, UNSIO).
- `-v` shows the compilation progress. Expect a lot of output, which is normal. The build takes several minutes.

---

## 5. Install nbody_streams

```bash
pip install "nbody_streams @ git+https://github.com/appy2806/Nbody_streams.git"
```

---

## 6. Check the installation

From the `LAPIS26` folder, run:

```bash
python check_install.py
```

When everything works, every line shows `[ OK ]` and the script ends with `All good!`. Lines marked `[ -- ]` are optional packages, and it's fine if they're missing.

To make the environment available in Jupyter as a kernel named "mwlmc":

```bash
python -m ipykernel install --user --name mwlmc --display-name "mwlmc"
```

---

## Optional extras

You **don't need** any of these for the tutorials.

**pyfalcon** is a fast O(N) CPU tree code that nbody_streams can use (`method='tree'` on CPU):

```bash
pip install --no-build-isolation "pyfalcon @ git+https://github.com/GalacticDynamics-Oxford/pyfalcon.git"
```

**healpy** is used for Mollweide sky projections: `pip install healpy`

**NVIDIA GPU** (Linux, CUDA 12 drivers): `pip install cupy-cuda12x` enables the GPU direct-sum backend. The GPU tree code also needs `nvcc` and has to be compiled by hand. See the [nbody_streams README](https://github.com/appy2806/Nbody_streams#quick-start).

---

## Troubleshooting

| Problem | Solution |
|---|---|
| `NumPy is not present - python extension cannot be compiled` | Add `--no-build-isolation` to the Agama `pip install` command and check that `python -c "import numpy"` works in the **same** environment. |
| Agama build fails with `A module that was compiled using NumPy 1.x cannot be run in NumPy 2.x` / `_ARRAY_API not found` | This happens with a venv on Ubuntu/Debian when `python3-numpy` is installed system-wide. Run `pip install "numpy<2"` and install Agama again, or use a conda environment instead. |
| `GSL library (required) is not found`, then the install stops or hangs | Install GSL with your system package manager (`libgsl-dev` / `gsl-devel` / `brew install gsl`), or make sure the `--config-settings --build-option=--yes` flag is included. |
| `error: command 'gcc' failed` / `clang: command not found` | The compiler is missing. Go back to [step 1](#1-install-system-tools). |
| `Package 'nbody-streams' requires a different Python` | Your Python is too new or too old. Create the environment with `python=3.12`. |
| `ModuleNotFoundError: No module named 'agama'` in Jupyter | Jupyter is using a different Python. Install the kernel ([step 6](#6-check-the-installation)) and select "mwlmc" in the notebook. |
| macOS: `ld: library not found` or architecture errors on Apple Silicon | Use a native arm64 Python (Miniforge provides one) and not an x86 Python running under Rosetta. |
| Anything else | Copy the **full** error message (run `pip` with `-v`) and bring it to the installation help session or send it to the organizers. |

For more detail, see the upstream instructions:
[Agama INSTALL](https://github.com/GalacticDynamics-Oxford/Agama/blob/master/INSTALL) ·
[nbody_streams README](https://github.com/appy2806/Nbody_streams#quick-start)
