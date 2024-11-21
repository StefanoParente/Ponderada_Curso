import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    data = pd.read_csv("/Users/stefanoparente/Desktop/Ponderada_Curso/Sea Level Predictor/epa-sea-level.csv")
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label="Dados reais", color="blue")
    slope, intercept, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_levels = intercept + slope * years_extended
    plt.plot(years_extended, sea_levels, label="Melhor ajuste (1880-2050)", color="red")
    recent_data = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    sea_levels_recent = intercept_recent + slope_recent * years_recent
    plt.plot(years_recent, sea_levels_recent, label="Melhor ajuste (2000-2050)", color="green")
    plt.xlabel("Ano")
    plt.ylabel("Nível do Mar (polegadas)")
    plt.title("Aumento do Nível do Mar")
    plt.legend()
    plt.savefig('sea_level_plot.png')
    return plt.gca()
