# Leaky Integrate-and-Fire Neuron: Computational Study

**Status: in progress.** This is a single-neuron study. It does not address synchronisation or coupled neurons.

## What this is
A Python implementation of the leaky integrate-and-fire (LIF) neuron model,
integrated with the forward Euler method. For constant input current, the
simulated interspike interval is compared with the exact analytical result.

## Model
C_m dV/dt = -g_L (V - E_L) + I(t), with threshold V_th, reset V_reset
and absolute refractory period t_ref. Units: mV, ms, pF, nS, pA.

## How to run
    pip install numpy matplotlib
    python lif_basic.py

This prints the simulated and analytical interspike intervals for a constant
current and saves a membrane potential trace as lif_trace.png.

## Planned next steps
- Firing rate as a function of input current
- Effect of membrane time constant, threshold, reset and refractory period
- Step and sinusoidal inputs

## Author
Ornet Vivya k.a, BS-MS Physics, IISER Berhampur
