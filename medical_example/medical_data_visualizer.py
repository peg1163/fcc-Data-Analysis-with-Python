import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = df['overweight'] = ((df['weight'] / (df['height'] / 100) ** 2) > 25).astype(int)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

df['cholesterol'] = (df['cholesterol'] >1 ).astype(int)

df['gluc'] = (df['gluc'] > 1).astype(int)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(df,value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat =pd.melt(df,id_vars='cardio',value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])
    

    # Draw the catplot with 'sns.catplot()'

    sns.catplot(data=df_cat,x='variable',hue='value',col='cardio',kind='count',order = sorted(df_cat['variable'].unique()))
    plt.show()
    # Get the figure for the output
    fig = plt.gcf()


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &  # Presión diastólica menor o igual que la sistólica
                (df['height'] >= df['height'].quantile(0.025)) &  # Altura mayor o igual que el percentil 2.5
                (df['height'] <= df['height'].quantile(0.975)) &  # Altura menor o igual que el percentil 97.5
                (df['weight'] >= df['weight'].quantile(0.025)) &  # Peso mayor o igual que el percentil 2.5
                (df['weight'] <= df['weight'].quantile(0.975))]  


    # Calculate the correlation matrix
    corr = df_heat.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(10, 8))

    # Draw the heatmap with 'sns.heatmap()'

    sns.heatmap(correlation, mask=mask, annot=True, cmap='coolwarm', fmt=".1f", square=True, ax=ax)
    
    
    plt.show()

    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
