# Simulations of Liouville Quantum Gravity

Here you will find some of my simulations of Liouville Quantum gravity and Eden models on it.

If you go to the 'Grid Models' folder you will find five notebooks:

* `LQG.ipynb` implements and does a basic test for the GFF and LQG on a toroidal latticce. This was then ported to a library that can be found on `LQG_Simulations/lib`
* `DLA_Eclidean.ipynb` implements a DLA in the euclidean setting
* `FPP_0DBM.ipynb` implements an exponential First Passage Percolation / Eden Model / ODBM discrete model on a Lattice
* `DLA_in_LQG.ipynb` and `EDEN_in_LQG.ipynb`implement the modifications of the previous two algorithms in the LQG setting, as explained in section 5 of the master's thesis.

## Some examples of pictures

### Sqrt(8/3)-LQG unit ball


This image shows different attempts to produce a unit ball for a sqrt(8/3)-LQG on a torus, and how much they agree. Since, even when the LQG instance is fixed, the unit balls are created using an stochastic Eden aggregation, there is still some stochasticity that can be seen on the same unit ball.

![LQG Balls](https://github.com/jaumededios/LQG_Simulations/blob/master/Selected%20Media/Eden_balls_distance_threshold.png)

### Evolution of LQG balls

This is an animation of an evolution of an LQG ball as gamma increases. To smoothen the animation the Eden aggregations are simulated using FPP with exponential clocks times the LQG, where the exponential clocks are the same in all the photograms to make for a smoother transition.

![LQG GIF](https://github.com/jaumededios/LQG_Simulations/blob/master/Selected%20Media/output.gif)

### DLA process in the euclidean plane

Zoom-in to a DLA cluster  in the euclidean plane with 500,000 elements.  At the moment I'm thinking about the implementation a more efficient algorithm to simulate DLA clusters on a LQG using a free boundary Elliptic PDE 

![DLA zoom-in](https://github.com/jaumededios/LQG_Simulations/blob/master/Selected%20Media/DLA_Zoom.png)

