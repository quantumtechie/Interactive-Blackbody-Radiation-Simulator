# Interactive-Blackbody-Radiation-Simulator
An interactive Python simulation of blackbody radiation using Planck's law, with a temperature slider for exploring spectral radiance.
## 🔬 Physics

This project simulates blackbody radiation using Planck's law. The spectral radiance is calculated as a function of wavelength and temperature.

## 📐 Planck's Law

The spectral radiance of a blackbody is given by:

$$
B(\lambda,T) =
\frac{2hc^2}{\lambda^5}
\frac{1}{e^{hc/(\lambda kT)}-1}
$$

where:

- $h$ = Planck's constant
- $c$ = speed of light
- $k$ = Boltzmann constant
- $\lambda$ = wavelength
- $T$ = absolute temperature

## 💻 Implementation

The simulation is written in Python using NumPy and Matplotlib.

An interactive temperature slider allows the user to change the blackbody temperature and observe how the spectrum changes.

## 🌡️ Temperature Range

The simulation allows temperatures between **3000 K and 10000 K**.

The wavelength range is **100 nm to 3000 nm**.

## 📊 Visualization

The simulation displays spectral radiance as a function of wavelength and highlights the visible-light region from **400 nm to 700 nm**.

## 🚀 How to Run

Install the required Python libraries:
```bash
pip install numpy matplotlib
```
