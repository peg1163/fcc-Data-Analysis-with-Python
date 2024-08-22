import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file

    df=pd.read_csv('epa-sea-level.csv')
    df.head()
    
    # Create scatter plot

    fig=plt.figure(figsize=(10,10))
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'])
    
    # Create first line of best fit

    model=linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    pendiente=model.slope
    intercept=model.intercept
    years_extended = pd.Series(range(1880, 2051)) 
    plt.plot(years_extended,pendiente*years_extended+intercept,label='fitted line',color='green')
    
    # Create second line of best fit
    df_2=df[df['Year']>=2000]
    model1=linregress(df_2['Year'],df_2['CSIRO Adjusted Sea Level'])
    pendiente1=model1.slope
    intercept1=model1.intercept
    years_extended2 = pd.Series(range(2000, 2051)) 
    plt.plot(years_extended2,pendiente1*years_extended2+intercept1,label='fitted line',color='black')
    plt.plot(2050,pendiente*2050+intercept,'ro',label='2050')
    plt.plot(2050,pendiente1*2050+intercept1,'ro',label='2050')
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

  
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()