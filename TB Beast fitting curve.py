import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Load the CSV file
file_path = "C:/Users/Getamulu/TB Ethiopia Since 2020.csv"  # Update this to your actual file path
df = pd.read_csv(file_path, header=None)

# Clean and format the data
df.columns = ["Year", "Cases"]
df["Year"] = df["Year"].astype(int)
df["Cases"] = df["Cases"].astype(str).str.replace(" ", "").astype(int)

# Fix duplicate years by averaging cases
df = df.groupby("Year", as_index=False).mean()

# Sort data by year
df = df.sort_values(by="Year")

### ---- CUBIC SPLINE INTERPOLATION ---- ###
spline = CubicSpline(df["Year"], df["Cases"])

### ---- POLYNOMIAL FIT (Degree 5) ---- ###
poly_coeffs = np.polyfit(df["Year"], df["Cases"], 5)
poly_func = np.poly1d(poly_coeffs)

# Generate smooth values for plotting
x_values = np.linspace(df["Year"].min(), df["Year"].max(), 100)
y_spline = spline(x_values)
y_poly = poly_func(x_values)

# Plot the results
plt.figure(figsize=(8, 5))
plt.scatter(df["Year"], df["Cases"], color="red", label="Actual Data")
plt.plot(x_values, y_spline, label="", linestyle="dashed", color="blue")
plt.plot(x_values, y_poly, label="Polynomial Fit (Degree 5)", linestyle="dotted", color="green")
plt.xlabel("Year")
plt.ylabel("TB Cases")
plt.legend()
plt.title("")
plt.grid()
plt.show()
