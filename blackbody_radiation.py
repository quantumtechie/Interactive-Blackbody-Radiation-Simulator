import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Physical Constants (SI Units)
h = 6.626e-34  # Planck constant (J*s)
c = 3.0e8      # Speed of light (m/s)
k = 1.38e-23   # Boltzmann constant (J/K)

def planck(wav, T):
    """Calculates spectral radiance for a given wavelength (m) and temperature (K)."""
    a = 2.0 * h * c**2
    b = h * c / (wav * k * T)
    
    # Suppress overflow warnings for extremely small wavelengths
    with np.errstate(over='ignore'):
        intensity = a / ( (wav**5) * (np.exp(b) - 1.0) )
    return intensity

# Set up wavelength array (100 nm to 3000 nm) and convert to meters
wavelengths_nm = np.linspace(100, 3000, 500)
wavelengths_m = wavelengths_nm * 1e-9

init_temp = 5000 # Initial temperature in Kelvin

# Set up the figure and Matplotlib subplots
fig, ax = plt.subplots(figsize=(10, 6))
plt.subplots_adjust(bottom=0.25)

# Plot initial blackbody curve
intensities = planck(wavelengths_m, init_temp)
line, = ax.plot(wavelengths_nm, intensities, lw=2, color='crimson')

# Formatting the plot axes
ax.set_title("Interactive Blackbody Radiation Simulator")
ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Spectral Radiance (W / (m² sr m))")
ax.set_xlim(100, 3000)
ax.set_ylim(0, np.max(planck(wavelengths_m, 10000)) * 1.1)
ax.grid(True, alpha=0.3)

# Highlight the visible light spectrum (400nm - 700nm)
ax.axvspan(400, 700, color='gray', alpha=0.15, label='Visible Light')
ax.legend()

# Configure the interactive slider axis
ax_temp = plt.axes([0.15, 0.1, 0.65, 0.03])
temp_slider = Slider(
    ax=ax_temp,
    label='Temperature (K)',
    valmin=3000,
    valmax=10000,
    valinit=init_temp,
    color='crimson'
)

# Update function bound to slider movement
def update(val):
    T = temp_slider.val
    new_intensities = planck(wavelengths_m, T)
    line.set_ydata(new_intensities)
    
    # Dynamically adjust y-axis to handle T^4 intensity explosion
    ax.set_ylim(0, np.max(new_intensities) * 1.1)
    fig.canvas.draw_idle()

temp_slider.on_changed(update)

plt.show()
