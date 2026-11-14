import numpy as np
import matplotlib.pyplot as plt

# Parameters. Units: mV, ms, pF, nS, pA
C_m = 200.0       # membrane capacitance, pF
g_L = 10.0        # leak conductance, nS
E_L = -70.0       # leak reversal / resting potential, mV
V_th = -50.0      # spike threshold, mV
V_reset = -65.0   # reset potential, mV
t_ref = 2.0       # absolute refractory period, ms

tau_m = C_m / g_L   # membrane time constant, ms
R = 1.0 / g_L       # membrane resistance, mV/pA


def simulate_lif(I, T=200.0, dt=0.1):
    """Euler simulation of the LIF neuron with constant input I (pA)."""
    n_steps = int(round(T / dt))
    ref_steps = int(round(t_ref / dt))
    t = np.arange(n_steps + 1) * dt
    V = np.zeros(n_steps + 1)
    V[0] = E_L
    spike_times = []
    ref_counter = 0                      # steps left in refractory period
    for n in range(n_steps):
        if ref_counter > 0:              # refractory: hold at reset
            V[n + 1] = V_reset
            ref_counter -= 1
            continue
        dVdt = (-(V[n] - E_L) + R * I) / tau_m
        V[n + 1] = V[n] + dt * dVdt      # Euler step
        if V[n + 1] >= V_th:             # threshold crossing
            spike_times.append(t[n + 1])
            V[n + 1] = V_reset
            ref_counter = ref_steps
    return t, V, np.array(spike_times)


def analytical_isi(I):
    """Exact interspike interval (ms) for constant I, or inf if no firing."""
    RI = R * I
    if RI <= V_th - E_L:
        return np.inf
    return t_ref + tau_m * np.log((RI - (V_reset - E_L)) / (RI - (V_th - E_L)))


if __name__ == "__main__":
    I = 250.0
    t, V, spikes = simulate_lif(I)
    isi_sim = np.diff(spikes)
    print(f"tau_m = {tau_m:.1f} ms, I_th = {g_L * (V_th - E_L):.1f} pA")
    print(f"simulated ISI (mean): {isi_sim.mean():.2f} ms")
    print(f"analytical ISI:       {analytical_isi(I):.2f} ms")

    fig, ax = plt.subplots(figsize=(7, 3.5))
    ax.plot(t, V)
    ax.axhline(V_th, ls="--", lw=0.8, color="k", label="threshold")
    ax.set_xlabel("Time (ms)")
    ax.set_ylabel("Membrane potential (mV)")
    ax.legend()
    fig.savefig("lif_trace.png", dpi=200, bbox_inches="tight")
    plt.show()