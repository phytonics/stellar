# Stellar Structure

The stellar structure is largely predicated by two distinct but important phenomena: **nuclear fusion** and **hydrostatic equilibrium**.

## Hydrostatic Equilibrium
Consider a star as a singular container which holds a set of molecules together in vaccuum. By logic, we know that this structure, on it's own, does NOT hold, since, by the Ideal Gas Law,

$$PV = nRT$$

Anything which holds a certain amount of molecules, $n$, exerts an outward pressure. The intuition behind this is the consistent collisions of molecules against the walls of the container, exerting a large force per unit area which leads to an outward pressure. To counteract this pressure, we suggest that these molecules are in fact giant masses, owing to us currently exploring how a star might work. If the parts are so big, we know that there is a net inward gravitational force which suggests that we can counteract the outward pressure with "gravitational pressure". This is known as **hydrostatic equilibrium**.

## The Actual Structure of the Star

The 








## The Key Equations
There are four key differential equations that dictate the star's evolution history.

### The Equation of Mass Continuity
Given a mass $M(r)$ is contained within a radius $r$, with density $\rho(r)$, we have:
$$
\frac{d}{dr} M(r) = 4\pi r^2 \rho(r)
$$

Nothing much is to be said here, except this result is very useful for the other 3 equations.

### The Equation of Hydrostatic Equilibrium

For the above situation, it must be balanced by an outward gas pressure $P(r)$ such that:

$$
\begin{align*}
\frac{d}{dr} P(r) &= - \rho(r) \frac{GM(r)}{r^2} \\
\text{or otherwise, }\frac{dP}{dM} &= - \frac{GM(r)}{4\pi r^4} \\
\text{We can hence solve this via:} \\
4\pi \int_0^r r^4 \frac{dP}{dr} dr &= G \int_0^M M(r) dM \\
4\pi (r^4 P(r) - 4\int_0^r r^3 P dr) &= G\frac{(M(r))^2}{2} \\ 
\end{align*}
$$

### The Equation of Energy Conservation

Given a star has some outward luminosity, $L$ for a given mass $M(r)$ of density $\rho(r)$ and energy per unit mass per unit time $\varepsilon(r)$ (which is defined based on the chemical composition and mass, density and temperature), it holds that:

$$
\begin{align*}
\frac{dL}{dr} &= 4\pi r^2 \rho(r) \varepsilon(r) \\
\text{or by Eqn 1, }\frac{dL}{dM} &= \varepsilon(r)
\end{align*}
$$

### The Equation for Radiative Energy Transfer

To represent the Temperature, $T(r)$ of this given star, based on the radiative energy transferred to that distance, in addition some radiative resistance $\kappa(r)$,

$$
\begin{align*}
\frac{d}{dr} T(r) &= - \frac{3\kappa(r)\rho(r)L(r)}{16\pi r^2 ac (T(r))^3} \\
\text{or by Eqn 1, }\frac{dT}{dM} &= -\frac{3\Kappa(r)L(r)}{64\pi^2 acr^4 (T(r))^3}
\end{align*}
$$