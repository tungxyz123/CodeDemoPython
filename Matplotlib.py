import matplotlib.pyplot as plt
import numpy as np

#Line Chart
# Define the x and y coordinates
x = ['May 05', 'May 12', 'May 19', 'May 26', 'Jun 02']
y = [50.1, 42.1, 58.5, 23.4, 34.9]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Plot the line chart
ax.plot(x, y, color='black', linewidth=2)

# Add grid lines
ax.grid(True, linestyle='--', color='gray', alpha=0.5)

# Add labels and title
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Annual revenue of countries', fontsize=12)
ax.set_title('Annual revenue of countries', fontsize=14, fontweight='bold')

# Add data labels
for i, value in enumerate(y):
    ax.text(x[i], value + 0.5, f'{value:.2f}', ha='center', va='bottom', fontsize=10)
# Set x-axis tick rotation
plt.xticks(rotation=45, ha='right')
# Adjust the spacing between subplots
plt.subplots_adjust(bottom=0.2)
# Display the chart
plt.show()





#Stacked bar chart
# Define the data
labels = ['High-performance desktop computer for professional use', 'Powerful laptop for professional use', 'Ultra HD smart TV with built-in streaming services', 'Next-gen gaming console for immersive gameplay', 'High-resolution camera with advanced shooting modes', '10-inch tablet with powerful performance', 'Advanced security system for home protection', 'High-performance smartphone with advanced features', 'Compact projector for presentations and entertainment', 'Interactive mirror with built-in display and voice assistant', 'Wireless printer with scanning and copying capabilities', '24-inch LED monitor with crisp visuals', 'Fitness tracking smartwatch with heart rate monitor', 'Keyless entry door lock with fingerprint recognition', '500GB portable SSD for fast and reliable storage', 'Wi-Fi enabled thermostat for efficient temperature control', 'Air purifier with HEPA filter for clean and fresh air', 'Central control hub for home automation devices', 'Over-ear headphones with immersive sound quality', 'Outdoor wireless CCTV camera for surveillance', 'Waterproof portable speaker with 360° sound', 'Wireless headset with noise cancellation for crystal-clear audio', '1TB portable external hard drive for data storage', 'Gaming headset with surround sound and detachable microphone']
values = [930.99, 899.99, 749.99, 499.99, 479.99, 399.99, 349.99, 699.99, 349.99, 149.99, 99.99, 149.99, 99.99, 99.99, 79.99, 99.99, 149.99, 99.99, 99.99, 79.99, 69.99, 59.99, 59.99, 49.99]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(16, 12))

# Plot the stacked bar chart
ax.barh(labels, values, color='royalblue', edgecolor='black')

# Add labels and title
ax.set_title('Production Cost', fontsize=16, fontweight='bold')
ax.set_xlabel('Sum of Product_Cost_Price', fontsize=14)
ax.set_ylabel('Product Description', fontsize=14)

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')

# Adjust the spacing between subplots
plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, hspace=0.5)

# Display the chart
plt.show()