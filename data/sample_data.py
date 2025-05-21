import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def get_environmental_data():
    """
    Generate synthetic environmental data for demonstration purposes.
    The function creates a pandas DataFrame with environmental metrics including:
    - date
    - temperature
    - humidity
    - soil_moisture
    - water_usage
    - energy_consumption
    
    Returns:
        DataFrame: Environmental metrics data
    """
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=60)
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    
    n = len(dates)
    
   
    np.random.seed(42)
    
    
    base_temp = 20 + 5 * np.sin(np.linspace(0, 4*np.pi, n))  
    daily_variation = np.random.normal(0, 2, n)  
    temperature = base_temp + daily_variation
    
    
    base_humidity = 60 + 15 * np.sin(np.linspace(0, 3*np.pi, n))  
    humidity_variation = np.random.normal(0, 5, n)  
    humidity = base_humidity + humidity_variation
    
    
    base_soil_moisture = 70 + 10 * np.sin(np.linspace(0, 6*np.pi, n))  
    soil_moisture_variation = np.random.normal(0, 3, n) 
    humidity_effect = 0.1 * (humidity - 60)
    soil_moisture = base_soil_moisture + soil_moisture_variation + humidity_effect
    
   
    base_water = 10 + 2 * np.sin(np.linspace(0, 8*np.pi, n)) 
    temp_effect = 0.3 * (temperature - 20)
    moisture_effect = -0.2 * (soil_moisture - 60)
    water_usage = base_water + temp_effect + moisture_effect + np.random.normal(0, 1, n)
    
   
    base_energy = 10 + 3 * np.sin(np.linspace(0, 2*np.pi, n))  
    temp_deviation = np.abs(temperature - 21)
    energy_effect = 0.5 * temp_deviation
    energy_consumption = base_energy + energy_effect + np.random.normal(0, 1.5, n)
    
    
    temperature = np.clip(temperature, 10, 35)
    humidity = np.clip(humidity, 30, 95)
    soil_moisture = np.clip(soil_moisture, 20, 95)
    water_usage = np.clip(water_usage, 2, 30)
    energy_consumption = np.clip(energy_consumption, 3, 40)
    
    
    df = pd.DataFrame({
        'date': dates,
        'temperature': temperature,
        'humidity': humidity,
        'soil_moisture': soil_moisture,
        'water_usage': water_usage,
        'energy_consumption': energy_consumption
    })
    
    return df
