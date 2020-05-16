# This version for separate folds
## How to execute a program?

1) From python3 

You have to write "python3 " + the number of the program that you want to check.
For example:

    python3 Hauss.py 

2) Jupyter

You have to write "jupyter notebook " and of the homework that you want to check.
Secondly, you must add ".ipynb" to the note.
For example:
  
    jupyter notebook homework1.ipynb

To execute the programs in Jupyter press button-combination Shift+Enter.
## What do this programs
### Heat equation
In physics and mathematics, the heat equation is a partial differential equation that describes how the distribution of some quantity (such as heat) evolves over time in a solid medium, as it spontaneously flows from places where it is higher towards places where it is lower. It is a special case of the diffusion equation.

This equation was first developed and solved by Joseph Fourier in 1822 to describe heat flow. 
However, it is of fundamental importance in diverse scientific fields. In probability theory, the heat equation is connected with the study of random walks and Brownian motion, via the Fokker–Planck equation. 
In financial mathematics, it is used to solve the Black–Scholes partial differential equation. 
In quantum mechanics, it is used for finding spread of wave function in potential free region. 
A variant was also instrumental in the solution of the longstanding Poincaré conjecture of topology.

Meaning of the equation

Informally, the Laplacian operator ∇^2 gives the difference between the average value of a function in the neighborhood of a point, and its value at that point. 

Thus, if u is the temperature, ∇^2 tells whether (and by how much) the material surrounding each point is hotter or colder, on the average, than the material at that point.

By the second law of thermodynamics, heat will flow from hotter bodies to adjacent colder bodies, in proportion to the difference of temperature and of the thermal conductivity of the material between them. 

When heat flows into (or out of) a material, its temperature increases (respectively, decreases), in proportion to the amount of heat divided by the amount (mass) of material, with a proportionality factor called the specific heat capacity of the material.

Therefore, the equation says that the rate u' at which the material at a point will heat up (or cool down) is proportional to how much hotter (or cooler) the surrounding material is. 

The coefficient α  in the equation takes into account the thermal conductivity, the specific heat, and the density of the material. 

Character of the solutions

The heat equation implies that peaks (local maxima) of u will be gradually eroded down, while depressions (local minima) will be filled in. 

The value at some point will remain stable only as long as it is equal to the average value in its immediate surroundings. 

In particular, if the values in a neighborhood are very close to a linear function Ax + By + Cz + D , then the value at the center of that neighborhood will not be changing at that time (that is, the derivative u').

A more subtle consequence is the maximum principle, that says that the maximum value of u {\displaystyle u} u in any region R of the medium will not exceed the maximum value that previously occurred in R, unless it is on the boundary of R. 

That is, the maximum temperature in a region R can increase only if heat comes in from outside R. This is a property of parabolic partial differential equations and is not difficult to prove mathematically (see below).

Another interesting property is that even if u initially has a sharp jump (discontinuity) of value across some surface inside the medium, the jump is immediately smoothed out by a momentary, infinitesimally short but infinitely large rate of flow of heat through that surface. 

For example, if two isolated bodies, initially at uniform but different temperatures u0 and u1, are made to touch each other, the temperature at the point of contact will immediately assume some intermediate value, and a zone will develop around that point where u will gradually vary between u0 and u1.

If a certain amount of heat is suddenly applied to a point the medium, it will spread out in all directions in the form of a diffusion wave. Unlike the elastic and electromagnetic waves, the speed of a diffusion wave drops with time: as it spreads over a larger region, the temperature gradient decreases, and therefore the heat flow decreases too. 

### Transport equation 
The convection–diffusion equation is a combination of the diffusion and convection (advection) equations, and describes physical phenomena where particles, energy, or other physical quantities are transferred inside a physical system due to two processes: diffusion and convection. Depending on context, the same equation can be called the advection–diffusion equation, drift–diffusion equation,or (generic) scalar transport equation.

The general equation is

    ∂c/∂t = ∇ ⋅ (D∇c) − ∇⋅(vc) + R

where

c is the variable of interest (species concentration for mass transfer, temperature for heat transfer), D is the diffusivity (also called diffusion coefficient), such as mass diffusivity for particle motion or thermal diffusivity for heat transport, v is the velocity field that the quantity is moving with. 
It is a function of time and space. For example, in advection, c might be the concentration of salt in a river, and then v would be the velocity of the water flow as a function of time and location. 
Another example, c might be the concentration of small bubbles in a calm lake, and then v would be the velocity of bubbles rising towards the surface by buoyancy (see below) depending on time and location of the bubble. 
For multiphase flows and flows in porous media, v is the (hypothetical) superficial velocity.
R describes sources or sinks of the quantity c. 
For example, for a chemical species, R > 0 means that a chemical reaction is creating more of the species, and R < 0 means that a chemical reaction is destroying the species. 
For heat transport, R > 0 might occur if thermal energy is being generated by friction.
∇ represents gradient and ∇ ⋅ represents divergence. 
In this equation, ∇c represents concentration gradient.

Understanding the terms involved

The right-hand side of the equation is the sum of three contributions.

The first, ∇ ⋅ (D∇c), describes diffusion. 
Imagine that c is the concentration of a chemical. 
When concentration is low somewhere compared to the surrounding areas (e.g. a local minimum of concentration), the substance will diffuse in from the surroundings, so the concentration will increase. Conversely, if concentration is high compared to the surroundings (e.g. a local maximum of concentration), then the substance will diffuse out and the concentration will decrease. 
The net diffusion is proportional to the Laplacian (or second derivative) of concentration if the diffusivity D is a constant.
The second contribution, −∇ ⋅ (vc), describes convection (or advection). 
Imagine standing on the bank of a river, measuring the water's salinity (amount of salt) each second. 
Upstream, somebody dumps a bucket of salt into the river. 
A while later, you would see the salinity suddenly rise, then fall, as the zone of salty water passes by. 
Thus, the concentration at a given location can change because of the flow.
The final contribution, R, describes the creation or destruction of the quantity. 
For example, if c is the concentration of a molecule, then R describes how the molecule can be created or destroyed by chemical reactions. 
R may be a function of c and of other parameters. 
Often there are several quantities, each with its own convection–diffusion equation, where the destruction of one quantity entails the creation of another. 
For example, when methane burns, it involves not only the destruction of methane and oxygen but also the creation of carbon dioxide and water vapor. 
Therefore, while each of these chemicals has its own convection–diffusion equation, they are coupled together and must be solved as a system of simultaneous differential equations.

Common simplifications

In a common situation, the diffusion coefficient is constant, there are no sources or sinks, and the velocity field describes an incompressible flow (i.e., it has zero divergence). Then the formula simplifies to:[5][6][7]

    ∂c/∂t = D(∇^2)c − v⋅∇c. 

In this form, the convection–diffusion equation combines both parabolic and hyperbolic partial differential equations.

In non-interacting material, D=0 (for example, when temperature is close to absolute zero, dilute gas has almost zero mass diffusivity), hence the transport equation is simply:

    ∂c/∂t + v⋅∇c = 0. 

Using Fourier transform in both temporal and spatial domain (that is, with integral kernel ejωt + jk⋅x) , its characteristic equation can be obtained:

    jω(c~) + v⋅jk(c~) = 0→ω =−k⋅v,

which gives the general solution:

    c = f(x−vt), 

where f  is any differentiable scalar function. 
This is the basis of temperature measurement for near Bose–Einstein condensate via time of flight method.

Stationary version:

The stationary convection–diffusion equation describes the steady-state behavior of a convective-diffusive system. In a steady state, ∂c/∂t = 0, so the formula is:

    0=∇⋅(D∇c)−∇⋅(vc)+R. 

## Input data:
 In input data you have to set how shallow will be a cell.
