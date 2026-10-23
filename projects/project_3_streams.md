# Project 3: Stellar Streams as Probes of the LMC and the Milky Way's Reflex Motion

## Motivation

Stellar streams are the debris of dwarf galaxies and globular clusters torn apart by the tides of the Milky Way (MW). In a static, smooth potential the stars of a stream follow, roughly, the orbit of their progenitor: the stream lies close to a single plane, and the stars move along the stream. This changes when the Large Magellanic Cloud (LMC) falls in. With a mass of ~10^11 Msun, the LMC perturbs streams in two ways:

1. **Direct pull (torques):** the LMC's gravity acts on the stream stars. It is strongest for the stars that pass close to the LMC.
2. **Reflex motion of the MW:** the LMC also pulls on the MW, so the inner MW (and the Sun with it) is accelerated towards the LMC. Seen from the MW, every star feels an extra, uniform force $-\mathbf{a}_{\rm MW}(t)$: the MW frame is not inertial. It acts on *every* stream, even on those that never come close to the LMC (Gómez et al. 2015).

Near the MW centre the two effects cancel: what is left is the tidal field of the LMC. Far from the centre they do not cancel, and streams can be strongly perturbed. The best-known examples are the Orphan stream, whose stars do not move along the stream (Koposov et al. 2019; Erkal et al. 2019), and the Sagittarius stream (Vasiliev et al. 2021). Several streams were used together to weigh the LMC (Shipp et al. 2021).

In this project you will generate mock streams of different lengths, up to two wraps around the MW, on many different orbits. For each one you will separate the effect of the **LMC's direct pull** from the effect of the **MW's reflex motion**, and work out which streams are dominated by which.

## The four models

You will make every stream in four potentials, all written in the **MW frame** (the MW centre stays at the origin):

| model | MW | LMC pull | moving frame $-\mathbf{a}_{\rm MW}(t)$ | what it is |
|---|---|---|---|---|
| **A. MW isolated** | ✓ | | | reference |
| **B. Reflex only** | ✓ | | ✓ | the MW moves as it would under the LMC, but the LMC does not pull on the stars |
| **C. Direct pull only** | ✓ | ✓ | | the LMC pulls on the stars, but the MW is nailed in place |
| **D. MW + LMC** | ✓ | ✓ | ✓ | the full (rigid) MW + LMC system |

Models B and C are not physical on their own: they are a **decomposition**. Comparing B with A isolates the reflex motion; comparing C with A isolates the direct pull. D is the real answer, and in general D ≠ B + C − A, because the response of a stream is not linear.

> **Hints:**
>
> - Use [`gala`](https://gala.adrian.pw) for potentials, orbit integration and mock streams (`gd.MockStreamGenerator` with `gd.FardalStreamDF`).
> - The notebook [stream_evolution.ipynb](stream_evolution.ipynb) already builds models A, B and D and generates streams in them. Model C is the "no fictitious force" case of Step 5 of [dynamical_friction_MWLMC_tutorial.ipynb](dynamical_friction_MWLMC_tutorial.ipynb): `mw_plus(lmc=lmc_moving)` in `stream_evolution.ipynb`.
> - The LMC moves in the MW frame: use `gp.TimeInterpolatedPotential` with a time-dependent `origin`.
> - `gala` has no uniform-field potential. The notebook gets one from a very distant, very massive Kepler point mass (`TimeInterpolatedPotential` with a time-dependent `origin` and `m`). Read Section 2 of `stream_evolution.ipynb` before you build your own.
> - Stream distribution functions assume that the host is at the origin. This is why we work in the MW frame and not in the inertial frame.

## How to explore different stream orbits

Each stream is defined by its progenitor's initial conditions at the start time $t_{\rm start}$ (e.g. 4–6 Gyr ago), its mass, and how long it disrupts. A convenient parameterisation:

- **Orbital plane (pole):** pick a unit vector $\hat{\mathbf{n}}$, the initial orbital pole. Sample the poles uniformly on the sphere, for example with a Fibonacci grid or with `healpy` (`nside=2` gives 48 directions). Poles $\hat{\mathbf{n}}$ and $-\hat{\mathbf{n}}$ give the same plane with opposite senses of rotation. Compare them, because the sense of rotation relative to the LMC orbit matters.
- **Starting point in the plane:** pick a unit vector $\hat{\mathbf{u}}\perp\hat{\mathbf{n}}$ and an angle $\psi$ in the plane, and start the progenitor at apocentre, $\mathbf{x}_0 = r_{\rm apo}\,\hat{\mathbf{u}}(\psi)$. The phase $\psi$ sets where the progenitor is when the LMC arrives; try a few values.
- **Eccentricity:** give the progenitor a purely tangential velocity $\mathbf{v}_0 = f\,v_c(r_{\rm apo})\,(\hat{\mathbf{n}}\times\hat{\mathbf{u}})$, with $f<1$. In the notebooks $f=0.5$ at $r_{\rm apo}=100$ kpc gives a pericentre of ~27 kpc and an eccentricity of ~0.6. Use the isolated MW to map $f$ to pericentre and eccentricity (`orbit.pericenter()`, `orbit.eccentricity()`).
- **Length of the stream (number of wraps):** a stream gets longer with time and with the energy spread of its stars, which grows with the progenitor mass (roughly as $M^{1/3}$). To get up to two wraps:
  - choose $r_{\rm apo}$ so that the radial period is a fraction of the integration time (`orbit.estimate_period()`): e.g. $r_{\rm apo}\sim40$–60 kpc and $t_{\rm start}\sim5$ Gyr;
  - increase the progenitor mass (e.g. $10^7$–$10^8$ Msun) for longer, wider streams;
  - measure the length as the angular extent of the stream in its orbital plane, unwrapped with the `lead_trail` label of each star (as in `stream_evolution.ipynb`).
- **Old vs. young debris:** each star has a `release_time`. Use it to split a long stream into its old wrap and its young wrap, and compute the metrics for each part separately.

Fix the **past** initial conditions in all four models: you then see how each potential changes the same stream. (The alternative, fixing the present-day progenitor, is closer to observations: `MockStreamGenerator.run` with a negative time step takes the progenitor's present-day position and velocity, integrates it back, and then forms the stream forwards to today.)

## Metrics of the perturbation

Compute all three metrics for the stream today in each model, and for each part of the stream (e.g. leading vs. trailing arm, old vs. young wrap).

1. **Proper-motion misalignment** (Erkal et al. 2019; Koposov et al. 2019; Shipp et al. 2021). In an unperturbed stream the stars move along the stream on the sky. Observe the stream from the Sun:
   - Put the Sun at its present position in the MW frame and convert the star positions and velocities to heliocentric coordinates (`astropy.coordinates.Galactocentric`).
   - Correct the proper motions for the solar motion (`gala.coordinates.reflex_correct`).
   - Rotate to stream coordinates $(\phi_1, \phi_2)$ aligned with the stream (`gala.coordinates.GreatCircleICRSFrame`, e.g. from the mean orbital pole of the stars).
   - The misalignment along the stream is the angle between the track direction and the proper motion: $\Delta\theta(\phi_1) = \arctan(\mu_{\phi_2}/\mu_{\phi_1}) - \arctan(d\phi_2/d\phi_1)$, computed in bins of $\phi_1$.
2. **Orbital poles.** Compute the pole of every star, $\hat{\mathbf{L}} = \mathbf{x}\times\mathbf{v}/|\mathbf{x}\times\mathbf{v}|$, in the MW frame. Use the mean pole, the spread of the poles, and how the pole changes along the stream. Plot the poles on the sky (e.g. Mollweide projection of $(l, b)$ of $\hat{\mathbf{L}}$).
3. **Tilt of the orbital plane.** Two estimates:
   - the angle between today's mean pole and the progenitor's initial pole;
   - the angle between the initial pole and the normal of the best-fitting plane through the star positions (an SVD of the positions gives the normal).

   Compare the tilt of the old and the young wrap.

For each metric $M$ and each stream, the perturbations are $\Delta M_{\rm reflex} = M_B - M_A$, $\Delta M_{\rm direct} = M_C - M_A$ and $\Delta M_{\rm full} = M_D - M_A$. A simple way to classify the streams is the **reflex fraction**

$$
f_{\rm reflex} = \frac{|\Delta M_{\rm reflex}|}{|\Delta M_{\rm reflex}| + |\Delta M_{\rm direct}|},
$$

e.g. reflex-dominated for $f_{\rm reflex}>0.6$, torque-dominated for $f_{\rm reflex}<0.4$, and mixed in between. Watch the signs: the two effects often work against each other (in `stream_evolution.ipynb` the reflex motion alone tilts the stream by ~20°, but the full MW + LMC system only by ~10°).

## Steps and milestones

### Step 1: Warm-up

Run [dynamical_friction_MWLMC_tutorial.ipynb](dynamical_friction_MWLMC_tutorial.ipynb) (Steps 1–5) and [stream_evolution.ipynb](stream_evolution.ipynb). Make sure you understand why the MW frame needs a fictitious force, and how the streams are generated.

**Milestone 1:** for one progenitor (e.g. starting at apocentre at ~100 kpc, 4 Gyr ago, with half the local circular velocity), you have a mock stream in the isolated MW and one in the full MW + LMC potential, together with:

- plots of the stream today in its orbital plane and edge-on, in both potentials, with the LMC's orbit marked;
- the out-of-plane thickness of the stream and the median tilt of the orbital poles of its stars. In the isolated MW the stream stays close to its initial plane: thickness ~1 kpc, pole tilt ~1°, set only by the spread of the released stars and by the disk. With the LMC it is visibly tilted and thicker. The changes grow mostly in the last ~1 Gyr, when the LMC approaches pericentre;
- a short explanation, in your own words, of the difference between the direct pull of the LMC and the reflex motion, and of why the frame of the MW disk is not inertial.

### Step 2: The four potentials

Integrate the live MW + LMC system backwards (with dynamical friction on the LMC) and build models A–D from it.

- Check that the moving-frame force equals $-\mathbf{a}_{\rm MW}(t)$ in the region you care about.
- Check model D against an integration in the **inertial** frame for a single test particle: the two must agree (see Section 3 of `stream_evolution.ipynb`).
- Make sure that the time range of your interpolated potentials covers the whole integration: outside it they return `NaN`.

**Milestone 2:** four validated potentials, and a plot of $|\mathbf{a}_{\rm MW}(t)|$ and of the LMC distance vs. time.

### Step 3: One stream, all metrics

Take one stream (e.g. the X–Z orbit of `stream_evolution.ipynb`) and implement the three metrics.

- In model A the misalignment should be small and the poles should stay close to the initial pole. These values set the noise floor: what you measure there comes from the disk, from the spread of the released stars, and from your own method.
- Compute the metrics in models B, C and D, and the reflex fraction.

**Milestone 3:** a single figure that shows the stream and its three metrics in the four models, and a table with $\Delta M_{\rm reflex}$, $\Delta M_{\rm direct}$, $\Delta M_{\rm full}$ and $f_{\rm reflex}$.

### Step 4: Many orbits, many lengths

Build a set of streams with the parameterisation above. Start small (e.g. 12 pole directions × 2 senses of rotation × 2 apocentres) before you go to larger grids. Include short streams (less than half a wrap), long ones (~1 wrap) and some with two wraps.

**Milestone 4:** a catalogue (a table or a `pandas` DataFrame) with, for each stream, its initial pole, apocentre, pericentre, eccentricity, length (in wraps), closest approach to the LMC, and all metrics in the four models.

### Step 5: Which streams feel what?

Use the catalogue to answer:

- Which streams are **reflex-dominated** and which are **torque-dominated**? Plot $f_{\rm reflex}$ on a sky map of the initial poles.
- How do the perturbations depend on:
  - the **distance** of the stream (pericentre, apocentre)?
  - the **orientation** of its plane relative to the LMC orbit and relative to $\mathbf{a}_{\rm MW}$? Is a uniform force perpendicular to the stream's plane more effective at tilting it?
  - the **closest approach to the LMC**?
  - the **sense of rotation** relative to the LMC?
  - the **length** of the stream, and the age of the debris (old vs. young wrap)?
- Which metric is the most sensitive to the reflex motion, and which to the direct pull?

Then turn the classification into **predictions for the Rubin Observatory Legacy Survey of Space and Time (LSST)**. Which of these perturbations could LSST actually see? "Observe" your mock streams:

- **Footprint:** keep only the stars in the LSST footprint (roughly the southern sky, Dec ≲ +5°). Which parts of your streams fall inside it? Note that the LMC is in the south.
- **Depth:** give each star an absolute magnitude drawn from a luminosity function (e.g. an old, metal-poor isochrone). Keep the stars brighter than the 10-year LSST depth ($r\approx27$; ~24.5 in a single visit). Main-sequence turn-off stars are then visible out to a few hundred kpc.
- **Proper motions:** add LSST-like proper-motion errors that grow with magnitude. They are of order 0.2 mas/yr for bright stars and ~1 mas/yr near $r\approx24$ over 10 years; check the values in Ivezić et al. (2019). Compare with Gaia, which only reaches $G\approx21$.
- **Distances and radial velocities:** LSST gives photometric distances, but no radial velocities. Decide which metrics still work with positions, distances and proper motions alone, and which need spectroscopic follow-up (e.g. 4MOST, DESI, PFS).

Recompute the metrics from the "observed" stars only.

**Milestone 5:** a classification of the streams with a physical explanation of the trends, and a prediction for LSST:

- Which streams, and which parts of them, could LSST detect, and at what distances?
- For which of them is the reflex signal larger than the observational errors, in which metric?
- How many such streams would you need to tell the reflex motion apart from the direct pull of the LMC?

### Step 6: Interpretation

Compare your results with the observed streams: Sagittarius (two wraps, ~20–100 kpc; Vasiliev et al. 2021), Orphan–Chenab (Koposov et al. 2019; Erkal et al. 2019) and the S5 streams (Shipp et al. 2021). Where would they sit in your classification?

**Milestone 6:** a short report or a clean notebook.

## Expected outcomes

Your report (or notebook) should include:

- **Stream plots** in the four models for a few representative streams (one short, one long, one with two wraps).
- **The three metrics** as a function of position along the stream, for the same streams.
- **Sky maps** of the initial poles, coloured by $\Delta M_{\rm reflex}$, $\Delta M_{\rm direct}$ and $f_{\rm reflex}$.
- **Scatter plots** of the perturbations against distance, closest approach to the LMC and stream length.
- **LSST predictions:** the metrics recomputed from the stars LSST would observe, and a list of the streams (and stream regions) where the reflex motion would be detectable.
- **A discussion** that answers:
  - Which streams are most affected by the **direct pull** of the LMC, and which by the **reflex motion**? Why?
  - Are there orbits on which the two effects **cancel**?
  - Do long streams (two wraps) carry more information than short ones? Is the old wrap perturbed differently from the young one?
  - Which metric would you measure first with real data?
  - What are the limitations of your approach (rigid potentials, no deformation of the MW halo, no observational errors, choice of MW and LMC masses, ...)?

## Advanced topics (optional)

- **Vary the LMC mass** (e.g. 1, 1.5 and 2.5 × 10^11 Msun). How do the reflex fractions change?
- **A flattened or triaxial halo** also makes orbital poles precess. Can you tell this apart from the LMC? Polar orbits barely precess in an axisymmetric halo; check this.
- **Observational errors.** Add Gaia-like proper-motion errors and 5–10% distance errors to the stars. Which metrics survive?
- **Real streams.** Get the present-day tracks of known streams from [`galstreams`](https://github.com/cmateu/galstreams) (Mateu 2023), set up progenitors on similar orbits, and repeat the analysis.
- **Non-linearity.** How different is $\Delta M_{\rm full}$ from $\Delta M_{\rm reflex} + \Delta M_{\rm direct}$? For which streams does the decomposition break down?

## Tips

- Start simple: one stream in model A, with its metrics, before you build a grid.
- Mock streams are cheap: a few seconds each without snapshots (`output_every=None`). With 4 models, budget for a full grid before you start it. `release_every` and `n_particles` control the number of stars and the run time.
- Use the same random seed (`random_state`) for all four models of a stream, so that the differences come from the potential and not from the random release.
- A small fraction of the stars (often those released early) end up on chaotic orbits. Use robust statistics (medians, clipping) in your metrics.
- Snapshots (`output_every`, `output_filename`) need `h5py` and only work with the DOP853 integrator. They are useful to follow the evolution of a few streams, but not for a large grid.
- Keep units consistent (kpc, km/s, Myr, Msun).
- Make your analysis reproducible: clean notebook, clear figures, labelled axes.

## References

### The effect of the LMC on the MW and on streams

- Gómez, F. A., Besla, G., Carpintero, D. D., et al. 2015, ApJ, 802, 128: *And Yet It Moves: The Dangers of Artificially Fixing the Milky Way Center of Mass in the Presence of a Massive Large Magellanic Cloud*, [arXiv:1408.4128](https://arxiv.org/abs/1408.4128)
- Vasiliev, E., Belokurov, V., & Erkal, D. 2021, MNRAS, 501, 2279: *Tango for three: Sagittarius, LMC, and the Milky Way*, [arXiv:2009.10726](https://arxiv.org/abs/2009.10726)
- Garavito-Camargo, N., Besla, G., Laporte, C. F. P., et al. 2019, ApJ, 884, 51: *Hunting for the Dark Matter Wake Induced by the Large Magellanic Cloud*, [arXiv:1902.05089](https://arxiv.org/abs/1902.05089)
- Petersen, M. S. & Peñarrubia, J. 2021, Nature Astronomy, 5, 251: *Detection of the Milky Way reflex motion due to the Large Magellanic Cloud infall*
- Vasiliev, E. 2023, Galaxies, 11, 59: *The Effect of the LMC on the Milky Way System* (review), [arXiv:2304.09136](https://arxiv.org/abs/2304.09136)

### Streams perturbed by the LMC

- Koposov, S. E., Belokurov, V., Li, T. S., et al. 2019, MNRAS, 485, 4726: *Piercing the Milky Way: an all-sky view of the Orphan Stream*, [arXiv:1812.08172](https://arxiv.org/abs/1812.08172)
- Erkal, D., Belokurov, V., Laporte, C. F. P., et al. 2019, MNRAS, 487, 2685: *The total mass of the Large Magellanic Cloud from its perturbation on the Orphan stream*, [arXiv:1812.08192](https://arxiv.org/abs/1812.08192)
- Shipp, N., Erkal, D., Drlica-Wagner, A., et al. 2021, ApJ, 923, 149: *Measuring the Mass of the Large Magellanic Cloud with Stellar Streams Observed by S5*, [arXiv:2107.13004](https://arxiv.org/abs/2107.13004)

### LSST

- Ivezić, Ž., Kahn, S. M., Tyson, J. A., et al. 2019, ApJ, 873, 111: *LSST: From Science Drivers to Reference Design and Anticipated Data Products*, [arXiv:0805.2366](https://arxiv.org/abs/0805.2366)

### Tools

- Fardal, M. A., Huang, S., & Weinberg, M. D. 2015, MNRAS, 452, 301: *Generation of mock tidal streams* (the stream model used by `gd.FardalStreamDF`)
- Mateu, C. 2023, MNRAS, 520, 5225: *galstreams: A library of Milky Way stellar stream footprints and tracks*
- `gala` docs: [mock streams](https://gala.adrian.pw/en/latest/dynamics/mockstreams.html), [coordinate frames for streams](https://gala.adrian.pw/en/latest/coordinates/index.html)
