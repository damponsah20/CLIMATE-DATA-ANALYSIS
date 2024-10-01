
# Required Libraries
import xarray as xr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# File Handling and Data Loading
def load_climate_data(file_path):
    """
    Load NetCDF climate data using xarray
    Args:
    file_path (str): Path to the NetCDF file
    
    Returns:
    ds (xarray.Dataset): The loaded dataset
    """
    ds = xr.open_dataset(file_path)
    print(ds)
    return ds

# Example function for calculating the monthly average
def calculate_monthly_mean(ds, var_name):
    """
    Calculate monthly average from daily climate data
    Args:
    ds (xarray.Dataset): Dataset containing the climate data
    var_name (str): Variable name to calculate mean for
    
    Returns:
    monthly_mean (xarray.DataArray): Monthly mean of the variable
    """
    monthly_mean = ds[var_name].resample(time='1M').mean()
    return monthly_mean

# Plotting the Monthly Mean Temperature
def plot_monthly_mean(monthly_mean, var_name):
    """
    Plot the monthly mean data
    Args:
    monthly_mean (xarray.DataArray): Monthly mean data
    var_name (str): Name of the variable for plotting title
    """
    plt.figure(figsize=(10, 6))
    monthly_mean.plot()
    plt.title(f'Monthly Mean {var_name}')
    plt.xlabel('Time')
    plt.ylabel(f'{var_name} (units)')
    plt.grid(True)
    plt.show()

# Example of calculating anomalies
def calculate_anomalies(ds, var_name):
    """
    Calculate climate anomalies
    Args:
    ds (xarray.Dataset): The loaded climate dataset
    var_name (str): The name of the variable for anomaly calculation
    
    Returns:
    anomalies (xarray.DataArray): Anomalies of the selected variable
    """
    climatology = ds[var_name].groupby('time.month').mean('time')
    anomalies = ds[var_name].groupby('time.month') - climatology
    return anomalies

# Plotting Climate Anomalies
def plot_anomalies(anomalies, var_name):
    """
    Plot climate anomalies
    Args:
    anomalies (xarray.DataArray): Anomalies of the climate variable
    var_name (str): Name of the variable for plotting
    """
    plt.figure(figsize=(10, 6))
    anomalies.plot()
    plt.title(f'{var_name} Anomalies')
    plt.xlabel('Time')
    plt.ylabel(f'{var_name} (units)')
    plt.grid(True)
    plt.show()

# Main function for analysis
def main():
    # Replace 'your_data.nc' with the path to your NetCDF file
    file_path = 'your_data.nc'
    
    # Load the data
    ds = load_climate_data(file_path)
    
    # Specify the climate variable you want to analyze (e.g., temperature)
    var_name = 'temperature'  # Change this to match your dataset variable
    
    # Calculate monthly mean
    monthly_mean = calculate_monthly_mean(ds, var_name)
    
    # Plot the monthly mean
    plot_monthly_mean(monthly_mean, var_name)
    
    # Calculate and plot anomalies
    anomalies = calculate_anomalies(ds, var_name)
    plot_anomalies(anomalies, var_name)

# Execute the main function when running the script
if __name__ == "__main__":
    main()
