import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_clean_data(file_path):
    df = pd.read_csv(file_path, parse_dates=['date'], index_col='date')
    df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
    return df

def draw_line_plot(df):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df['value'], color='red', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot(df):
    df['year'] = df.index.year
    df['month'] = df.index.month
    df_bar = df.groupby(['year', 'month'])['value'].mean().unstack()

    fig = df_bar.plot(kind='bar', figsize=(12, 6)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', labels=[calendar.month_name[i] for i in range(1, 13)])
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot(df):
    df['year'] = [d.year for d in df.index]
    df['month'] = [d.strftime('%b') for d in df.index]
    df['month_num'] = df.index.month
    df = df.sort_values('month_num')

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 6))
    sns.boxplot(x='year', y='value', data=df, ax=axes[0])
    sns.boxplot(x='month', y='value', data=df, ax=axes[1])

    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    fig.savefig('box_plot.png')
    return fig
