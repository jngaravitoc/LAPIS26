# Project 2: Revealing the Origin of Hypervelocity Stars

## Motivation

Hypervelocity stars (HVSs) move so fast that some of them are not bound to the Milky Way (MW). The classical way to make one is the **Hills mechanism**: a binary star passes close to a supermassive black hole, one star is captured, and the other is ejected at more than 1000 km/s. If an HVS comes from the MW's black hole (Sgr A*), its orbit traced back in time should go through the **Galactic Centre**.

But not all fast stars point back to the Galactic Centre. Other possible origins are:

- The **LMC**, which may host its own massive black hole and can also eject stars.
- **Satellite dwarf galaxies**, which are disrupted by the MW or may host black holes.
- The **MW disc**, from which "runaway" stars are kicked by supernovae in binaries or by close encounters in star clusters. These are usually slower than true HVSs.

In this project you will integrate the orbits of a sample of fast-moving stars backwards in time and look for places where their orbits cross. Do some of them share a common origin?

## The data

The file [data/hvs_observables.csv](data/hvs_observables.csv) contains the 16 late-type hypervelocity star candidates studied by [Nelson et al. 2024](https://ui.adsabs.harvard.edu/abs/2024MNRAS.532.2875N/abstract) ([arXiv:2407.02593](https://arxiv.org/abs/2407.02593)). The distances and radial velocities come from that paper, and the positions and proper motions from Gaia DR3. For each star you get:

| Column | Description |
|---|---|
| `source_id` | Gaia DR3 source ID |
| `name` | Short name used in this project (`star 1`, ..., `star 16`) |
| `ra_deg`, `dec_deg` | Sky position (ICRS) [deg] |
| `pmra_masyr`, `pmdec_masyr` | Proper motions [mas/yr] (`pmra` includes the cos(dec) factor) |
| `distance_kpc` | Heliocentric distance [kpc] |
| `rv_kms` | Line-of-sight (radial) velocity [km/s] |

The file does not include uncertainties. You can get them from the Gaia archive using the `source_id` (see the advanced topics).

## The models

You will integrate the orbits in two models:

1. **MW only:** a static MW potential.
2. **MW + LMC:** the MW plus a moving LMC that pulls on the stars, and a MW that reacts to the LMC.

> **Hints:**
>
> - Use [`gala`](https://gala.adrian.pw) for potentials and orbit integration.
> - Use `gala` or [`astropy.coordinates`](https://docs.astropy.org/en/stable/coordinates/) for coordinate transformations.
> - The notebook [dynamical_friction_MWLMC_tutorial.ipynb](dynamical_friction_MWLMC_tutorial.ipynb) shows how to set up the MW+LMC system and integrate the LMC orbit.
> - HVSs are fast, so their orbits change quickly near the Galactic Centre. Use a small time step and check that your orbits are converged.

## Steps

1. **Read the data** and look at it. Which stars are moving towards us and which away from us? Which are the closest and the most distant?
2. **Coordinates.** Convert (RA, Dec, distance, proper motions, radial velocity) to Galactocentric positions and velocities. Write down the solar position and velocity you adopt.
3. **Speeds.** Compute the Galactocentric speed of each star and compare it with the escape speed of your MW model at the star's position. Which stars are unbound?
4. **Build the potentials.** Choose a MW model (e.g. bulge + disc + halo) and an LMC model (e.g. a Hernquist profile). Integrate the MW+LMC system backwards first.
5. **Integrate the stars** backwards in time in both models. How far back does it make sense to integrate? (Hint: how long do these stars live, and how long does it take them to cross the Galaxy?)
6. **Look for the origin.** For each star, find:
   - its closest approach to the Galactic Centre, and when it happened;
   - its closest approach to the LMC, and when it happened.
7. **Satellite galaxies and globular clusters.** Get the MW satellite galaxies and globular clusters with full 6D phase-space information from the [Local Volume Database](https://github.com/apace7/local_volume_database) (Pace 2024; the same catalogue as in [Project 1](project_1_satellite_orbits.md)). Integrate their orbits backwards in the same models and over the same times as the stars.
8. **Closest encounters.** For each star, find which satellite galaxy or globular cluster it got closest to, how close, and when. Remember to compare the *relative* distance between the star and the object at the same time, not just the positions along the orbits. Is the relative velocity at that moment small enough for the star to have been ejected from that object?
9. **Look for a common origin.** Compare the orbits of the stars with each other. Do some stars point back to the same object or pass through the same place at the same time?
10. **Compare** the results of the MW-only and MW+LMC models.

## Expected outcomes

Your report (or notebook) should include:

- **Orbit plots** of the stars in Galactocentric coordinates (e.g. x-y, x-z, y-z), with the Galactic Centre and the LMC orbit marked.
- **Distance vs. time** plots showing each star's distance to the Galactic Centre and to the LMC.
- A **table** with, for each star: Galactocentric speed, bound or unbound, the minimum distance (and time) to the Galactic Centre and to the LMC, and the closest satellite galaxy or globular cluster (with its minimum distance, time and relative velocity), in both models.
- **A discussion** that answers:
  - Which stars are consistent with being ejected from the **Galactic Centre**?
  - Which could come from the **LMC**?
  - Which stars could come from a **satellite galaxy or a globular cluster**? Which object, and when?
  - Which stars have an **unknown origin**? Could they be runaway stars from the disc, or halo stars?
  - Do some stars share a **common origin**?
  - How much does including the LMC change your conclusions?
  - What are the limitations of your analysis (no uncertainties, choice of MW potential, ...)?

## Advanced topics (optional)

- **Uncertainties.** Download the proper motion uncertainties from the [Gaia archive](https://gea.esac.esa.int/archive/) using the `source_id`s (e.g. with `astroquery.gaia`). Assume an uncertainty for the distances and radial velocities (e.g. 10% and 5 km/s). Use Monte Carlo sampling to estimate how likely each origin is: what fraction of the sampled orbits passes within some distance of the Galactic Centre or the LMC?
- **Vary the MW and LMC masses.** How sensitive are your conclusions to the mass of the MW and the LMC?
- **Change the shape of the MW halo** (oblate, prolate, triaxial). Do the stars still point back to the Galactic Centre?
- **Ejection velocities.** For the stars coming from the Galactic Centre or the LMC, what ejection velocity did they need? Is it consistent with the Hills mechanism?
- **Compare with Nelson et al. 2024.** They used the chemical abundances of these stars to constrain their origin. Do your orbits agree with their conclusions?

## Tips

- Start simple: integrate one star in the MW-only model and plot its orbit before running all of them.
- Always check energy conservation in the MW-only model.
- Keep units consistent (kpc, km/s, Myr, Msun).
- Make your analysis reproducible: clean notebook, clear figures, labelled axes.

## References

- Nelson, T., Hawkins, K., Reggiani, H., et al. 2024, MNRAS, 532, 2875: *A Detailed Chemical Study of the Extreme Velocity Stars in the Galaxy*, [arXiv:2407.02593](https://arxiv.org/abs/2407.02593)
- Pace, A. B. 2024: *The Local Volume Database: a library of the observed properties of nearby dwarf galaxies and star clusters*, [arXiv:2411.07424](https://arxiv.org/abs/2411.07424)
