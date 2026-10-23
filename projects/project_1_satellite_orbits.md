# Project 1: Orbits of the Milky Way Satellite Galaxies

## Motivation

The Milky Way (MW) is surrounded by dozens of satellite galaxies. Where did they come from? Have they been orbiting the MW for many Gyr, or did they fall in recently? The Large Magellanic Cloud (LMC) is the most massive satellite (~10^11 Msun) and it is close to its first pericentre. It is so massive that it pulls on the MW itself and may have brought its own satellites with it.

In this project you will integrate the orbits of the MW satellites backwards in time in three different models of the Galaxy and compare the results. The goal is to learn which satellites are "classical" MW satellites, which ones came with the LMC, and how much the LMC changes our picture.

## The data: Local Volume Database

You will use the **Local Volume Database (LVDB)**: https://github.com/apace7/local_volume_database

The LVDB is a public catalogue of dwarf galaxies and star clusters in the Local Volume (the MW satellites, M31 satellites, and more distant dwarfs). For each object it provides, among other things:

- Sky position (RA, Dec)
- Distance (or distance modulus)
- Line-of-sight velocity
- Proper motions
- Structural properties (half-light radius, luminosity, etc.)

Read the repository README first to understand the table structure and the column names, and to see how to install and load it. For this project you need the full 6D phase-space information (position + velocity), so you will have to select the objects that have all of these measurements.

## The three models

You will integrate every satellite in three potentials:

1. **MW isolated:** a static MW potential. No LMC.
2. **MW + LMC:** the MW plus an LMC that is also moving (the LMC orbit is integrated at the same time, and it pulls on the satellites). The MW is allowed to react to the LMC (see the hint below).
3. **MW in a moving frame (no LMC):** the MW potential is the same as in case 1, but the MW is *accelerated*, as if it were moving under the pull of the LMC. The LMC itself is not included as a gravitating body in the satellite's equation of motion.

Comparing 2 and 3 tells you the effect of the LMC's direct pull on the satellites versus the effect of the shifting MW reference frame.

> **Hints:**
>
> - Use [`gala`](https://gala.adrian.pw) for potentials and orbit integration.
> - Use `gala` or [`astropy.coordinates`](https://docs.astropy.org/en/stable/coordinates/) for coordinate transformations.
> - The notebook [dynamical_friction_MWLMC_tutorial.ipynb](dynamical_friction_MWLMC_tutorial.ipynb) shows how to set up the MW+LMC system and integrate the LMC orbit, and it is a good starting point.

## Steps

1. **Get the data.** Download the LVDB and select the MW satellites with full 6D phase-space information, including the LMC.
2. **Coordinates.** Convert (RA, Dec, distance, proper motions, radial velocity) to Galactocentric Cartesian positions and velocities. Think about which solar position and velocity you adopt, and write it down.
3. **Build the potentials.** Choose a MW model (e.g. a bulge + disc + halo) and an LMC model (e.g. a Hernquist or NFW profile). Justify the masses and scale radii you pick.
4. **Integrate the MW+LMC system first.** Before touching the other satellites, integrate the LMC and the MW backwards together (both move!). Check that the LMC's pericentre and apocentre look sensible. You will need this LMC orbit and the MW's motion in models 2 and 3.
5. **Integrate the satellites.** Integrate each satellite backwards for ~5 Gyr in each of the three models.
6. **Measure properties.** For each satellite and each model, compute the pericentre, apocentre, eccentricity, and the orbital pole (direction of the angular momentum vector).
7. **Uncertainties.** Use Monte Carlo sampling of the observational errors (distance, proper motions, line-of-sight velocity) to see how robust your results are. Even a modest number of realizations (~100) is useful.
8. **Compare** the three models and interpret the results.

## Expected outcomes

Your report (or notebook) should include:

- **Orbit plots:** e.g. orbits in x-y, x-z, and distance vs. time for a few interesting satellites, in all three models.
- **Orbital poles:** a sky map of the orbital poles (in Galactic coordinates) of the satellites. Do they cluster?
- **Eccentricities** (and pericentres/apocentres) of the satellites, and how they change from one model to another.
- **A discussion** that answers:
  - Which satellites are likely **associated with the LMC** (e.g. close to the LMC in position and velocity in the past, similar orbital pole)?
  - Which are **MW satellites** unrelated to the LMC?
  - Which have been bound to the MW for a **long time** (e.g. multiple pericentres, small pericentre, short orbital period) and which are on **first infall**?
  - How do the results change between models? Which satellites are most sensitive to the LMC?
  - What are the limitations of your approach (static MW, no dynamical friction, observational errors, ...)?

## Advanced topics (optional)

- **Vary the MW mass.** Try e.g. 0.8, 1.2, and 1.5 × 10^12 Msun. How do the orbits and the LMC association change?
- **Vary the LMC mass.** Try e.g. 0.5, 1, and 2 × 10^11 Msun. What happens to the satellites' orbits? Which ones are most affected?
- **Change the shape of the MW halo.** Make it oblate, prolate or triaxial instead of spherical (e.g. a flattened NFW in `gala`). How do the orbits, orbital poles and eccentricities change? Is the orbital pole of a satellite still conserved?
- Add **dynamical friction** on the LMC (see [dynamical_friction_MWLMC_tutorial.ipynb](dynamical_friction_MWLMC_tutorial.ipynb)).

## Tips

- Start simple: make one satellite work in the isolated MW before running everything.
- Always check energy and angular momentum conservation in the isolated MW case.
- Keep units consistent (kpc, km/s, Gyr, Msun).
- Make your analysis reproducible: clean notebook, clear figures, labelled axes.

## References

### MW+LMC models and the effect of the LMC

- Garavito-Camargo, N., Besla, G., Laporte, C. F. P., et al. 2019, ApJ, 884, 51: *Hunting for the Dark Matter Wake Induced by the Large Magellanic Cloud*, [arXiv:1902.05089](https://arxiv.org/abs/1902.05089)
- Correa Magnus, L. & Vasiliev, E. 2022, MNRAS, 511, 2610: *Measuring the Milky Way mass distribution in the presence of the LMC*, [arXiv:2110.00018](https://arxiv.org/abs/2110.00018)
- Vasiliev, E. 2023, Galaxies, 11, 59: *The Effect of the LMC on the Milky Way System* (review), [arXiv:2304.09136](https://arxiv.org/abs/2304.09136)

### Orbits of MW satellites and LMC satellites

- Patel, E., Kallivayalil, N., Garavito-Camargo, N., et al. 2020, ApJ, 893, 121: *The Orbital Histories of Magellanic Satellites Using Gaia DR2 Proper Motions*, [arXiv:2001.01746](https://arxiv.org/abs/2001.01746)
- Battaglia, G., Taibi, S., Thomas, G. F., & Fritz, T. K. 2022, A&A, 657, A54: *Gaia early DR3 systemic motions of Local Group dwarf galaxies and orbital properties with a massive Large Magellanic Cloud*, [arXiv:2106.08819](https://arxiv.org/abs/2106.08819)
- Pace, A. B., Erkal, D., & Li, T. S. 2022, ApJ, 940, 136: *Proper Motions, Orbits, and Tidal Influences of Milky Way Dwarf Spheroidal Galaxies*, [arXiv:2205.05699](https://arxiv.org/abs/2205.05699)
