import fastf1
import matplotlib.pyplot as plt
import os

# Create cache folder if it doesn't exist, then enable it
os.makedirs('f1_cache', exist_ok=True)
fastf1.Cache.enable_cache('f1_cache')

# Load the 2026 Austrian Grand Prix race session
session = fastf1.get_session(2026, 'Austria', 'R')
session.load()

# Pick a driver to analyse - change 'RUS' to any 3-letter driver code
driver_code = 'RUS'
laps = session.laps.pick_driver(driver_code)

# Convert lap times to seconds for plotting
laps['LapTimeSeconds'] = laps['LapTime'].dt.total_seconds()

# Plot lap time degradation across the race
plt.figure(figsize=(10, 6))
plt.plot(laps['LapNumber'], laps['LapTimeSeconds'], marker='o', color='#00D2BE')
plt.title(f'{driver_code} Lap Time Degradation - Austrian GP 2026')
plt.xlabel('Lap Number')
plt.ylabel('Lap Time (seconds)')
plt.grid(True, alpha=0.3)
plt.savefig('tyre_degradation.png')
plt.show()

print("Done! Chart saved as tyre_degradation.png")
