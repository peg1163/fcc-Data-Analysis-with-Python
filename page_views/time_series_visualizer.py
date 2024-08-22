import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df.date = pd.to_datetime(df.date)
# Clean data
df = df[(df['value'] <= df['value'].quantile(0.975)) & (df['value'] >= df['value'].quantile(0.025))]


def draw_line_plot():
    # Draw line plot

    fig=plt.figure(figsize=(20, 6))
    plt.plot(df['date'], df['value'], color='red')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')

    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar=df.copy()
    df_bar['month'] = pd.DatetimeIndex(df_bar['date']).month
    df_bar['year'] = pd.DatetimeIndex(df_bar['date']).year


    # Draw bar plot
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean()
    df_bar=df_bar.unstack()
    df_bar.columns = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]
    fig=df_bar.plot(kind='bar', figsize=(15, 10)).figure
    plt.xlabel('Years',fontsize=12)
    plt.ylabel('Average Page Views',fontsize=12)
    plt.legend(loc='upper left',title='Months',title_fontsize='12',fontsize='12')
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
 
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig=plt.figure(figsize=(20, 6))
    plt.subplot(1,2,1)
    sns.boxplot(data=df_box, x='year', y='value',palette='tab10')
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.subplot(1,2,2)
    month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(data=df_box, x='month', y='value',order=month,palette='tab10').set_ylim(0, 200000)
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')
    plt.tight_layout()
 
    fig=plt.gcf()


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
