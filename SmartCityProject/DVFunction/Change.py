import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import statsmodels.tsa.stattools as ss
from statsmodels.tsa.seasonal import *
import matplotlib as mpl
import calmap
from scipy.stats import sem
from dateutil.parser import parse
import matplotlib; matplotlib.use('TkAgg')
import warnings; warnings.filterwarnings('ignore')
#import warnings; warnings.filterwarnings(action='once')

large = 22; med = 16; small = 12
params = {'axes.titlesize': large,
          'legend.fontsize': med,
          'figure.figsize': (16, 10),
          'axes.labelsize': med,
          'axes.titlesize': med,
          'xtick.labelsize': med,
          'ytick.labelsize': med,
          'figure.titlesize': large}

###=============================================================================================

def Time_Series_Plot(self):

    df = pd.read_csv('dataVset/AirPassengers.csv')

    # Draw Plot
    plt.figure("Time Series Plot",figsize=(16, 10), dpi=80)
    plt.plot('date', 'value', data=df, color='tab:red')

    # Decoration
    plt.ylim(50, 750)
    xtick_location = df.index.tolist()[::12]
    xtick_labels = [x[-4:] for x in df.date.tolist()[::12]]
    plt.xticks(ticks=xtick_location, labels=xtick_labels, rotation=0, fontsize=12, horizontalalignment='center',
               alpha=.7)
    plt.yticks(fontsize=12, alpha=.7)
    plt.title("Air Passengers Traffic (1949 - 1969)", fontsize=22)
    plt.grid(axis='both', alpha=.3)

    # Remove borders
    plt.gca().spines["top"].set_alpha(0.0)
    plt.gca().spines["bottom"].set_alpha(0.3)
    plt.gca().spines["right"].set_alpha(0.0)
    plt.gca().spines["left"].set_alpha(0.3)
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
    plt.show()


###=============================================================================================
def Time_Series_with_Peaks_and_Troughs_Annotated(self):
    df = pd.read_csv('dataVset/AirPassengers.csv')

    # Draw Plot
    # Get the Peaks and Troughs
    data = df['value'].values
    doublediff = np.diff(np.sign(np.diff(data)))
    peak_locations = np.where(doublediff == -2)[0] + 1

    doublediff2 = np.diff(np.sign(np.diff(-1 * data)))
    trough_locations = np.where(doublediff2 == -2)[0] + 1

    # Draw Plot
    plt.figure("Time Series with Peaks and Troughs Annotated",figsize=(16, 10), dpi=80)
    plt.plot('date', 'value', data=df, color='tab:blue', label='Air Traffic')
    plt.scatter(df.date[peak_locations], df.value[peak_locations], marker=mpl.markers.CARETUPBASE, color='tab:green',
                s=100, label='Peaks')
    plt.scatter(df.date[trough_locations], df.value[trough_locations], marker=mpl.markers.CARETDOWNBASE,
                color='tab:red', s=100, label='Troughs')

    # Annotate
    for t, p in zip(trough_locations[1::5], peak_locations[::3]):
        plt.text(df.date[p], df.value[p] + 15, df.date[p], horizontalalignment='center', color='darkgreen')
        plt.text(df.date[t], df.value[t] - 35, df.date[t], horizontalalignment='center', color='darkred')

    # Decoration
    plt.ylim(50, 750)
    xtick_location = df.index.tolist()[::6]
    xtick_labels = df.date.tolist()[::6]
    plt.xticks(ticks=xtick_location, labels=xtick_labels, rotation=90, fontsize=12, alpha=.7)
    plt.title("Peak and Troughs of Air Passengers Traffic (1949 - 1969)", fontsize=22)
    plt.yticks(fontsize=12, alpha=.7)

    # Lighten borders
    plt.gca().spines["top"].set_alpha(.0)
    plt.gca().spines["bottom"].set_alpha(.3)
    plt.gca().spines["right"].set_alpha(.0)
    plt.gca().spines["left"].set_alpha(.3)

    plt.legend(loc='upper left')
    plt.grid(axis='y', alpha=.3)
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
    plt.show()

###=============================================================================================
def Autocorrelation_ACF_and_Partial_Autocorrelation_PACF_Plot(self):
    df = pd.read_csv('dataVset/AirPassengers.csv')

    # Draw Plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6), dpi=80)
    plot_acf(df.value.tolist(), ax=ax1, lags=50)
    plot_pacf(df.value.tolist(), ax=ax2, lags=20)

    # Decorate
    # lighten the borders
    ax1.spines["top"].set_alpha(.3);
    ax2.spines["top"].set_alpha(.3)
    ax1.spines["bottom"].set_alpha(.3);
    ax2.spines["bottom"].set_alpha(.3)
    ax1.spines["right"].set_alpha(.3);
    ax2.spines["right"].set_alpha(.3)
    ax1.spines["left"].set_alpha(.3);
    ax2.spines["left"].set_alpha(.3)

    # font size of tick labels
    ax1.tick_params(axis='both', labelsize=12)
    ax2.tick_params(axis='both', labelsize=12)
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
    plt.show()

###=============================================================================================
def Cross_Correlation_plot(self):

    df = pd.read_csv('dataVset/mortality.csv')
    x = df['mdeaths']
    y = df['fdeaths']

    # Compute Cross Correlations
    ccs = ss.ccf(x, y)[:100]
    nlags = len(ccs)

    # Compute the Significance level
    # ref: https://stats.stackexchange.com/questions/3115/cross-correlation-significance-in-r/3128#3128
    conf_level = 2 / np.sqrt(nlags)

    # Draw Plot
    plt.figure("Cross Correlation plot",figsize=(12, 7), dpi=80)

    plt.hlines(0, xmin=0, xmax=100, color='gray')  # 0 axis
    plt.hlines(conf_level, xmin=0, xmax=100, color='gray')
    plt.hlines(-conf_level, xmin=0, xmax=100, color='gray')

    plt.bar(x=np.arange(len(ccs)), height=ccs, width=.3)

    # Decoration
    #plt.title('$Cross\; Correlation\; Plot:\; mdeaths\; vs\; fdeaths$', fontsize=22)
    plt.title('Cross Correlation Plot : mdeaths vs fdeaths', fontsize=22)
    plt.xlim(0, len(ccs))
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
    plt.show()

###=============================================================================================
def Time_Series_Decomposition_Plot(self):
    df = pd.read_csv('dataVset/AirPassengers.csv')
    dates = pd.DatetimeIndex([parse(d).strftime('%Y-%m-01') for d in df['date']])
    df.set_index(dates, inplace=True)

    # Decompose
    result = seasonal_decompose(df['value'], model='multiplicative')

    # Plot
    plt.rcParams.update({'figure.figsize': (10, 10)})
    result.plot().suptitle('Time Series Decomposition of Air Passengers')
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
    plt.show()
###=============================================================================================

###=============================================================================================
def Plotting_with_different_scales_using_secondary_Y_axis(self):
    df = pd.read_csv("dataVset/economics.csv")

    x = df['date']
    y1 = df['psavert']
    y2 = df['unemploy']

    # Plot Line1 (Left Y Axis)
    fig, ax1 = plt.subplots(1, 1, figsize=(16, 9), dpi=80)
    ax1.plot(x, y1, color='tab:red')

    # Plot Line2 (Right Y Axis)
    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    ax2.plot(x, y2, color='tab:blue')

    # Decorations
    # ax1 (left Y axis)
    ax1.set_xlabel('Year', fontsize=20)
    ax1.tick_params(axis='x', rotation=0, labelsize=12)
    ax1.set_ylabel('Personal Savings Rate', color='tab:red', fontsize=20)
    ax1.tick_params(axis='y', rotation=0, labelcolor='tab:red')
    ax1.grid(alpha=.4)

    # ax2 (right Y axis)
    ax2.set_ylabel("# Unemployed (1000's)", color='tab:blue', fontsize=20)
    ax2.tick_params(axis='y', labelcolor='tab:blue')
    ax2.set_xticks(np.arange(0, len(x), 60))
    ax2.set_xticklabels(x[::60], rotation=90, fontdict={'fontsize': 10})
    ax2.set_title("Personal Savings Rate vs Unemployed: Plotting in Secondary Y Axis", fontsize=22)
    fig.tight_layout()
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
    plt.show()


###=============================================================================================
def  Time_Series_with_Error_Bands(self):

    df = pd.read_csv("dataVset/user_orders_hourofday.csv")
    df_mean = df.groupby('order_hour_of_day').quantity.mean()
    df_se = df.groupby('order_hour_of_day').quantity.apply(sem).mul(1.96)

    # Plot
    plt.figure("Time Series with Error Bands",figsize=(16, 10), dpi=80)
    plt.ylabel("# Orders", fontsize=16)
    x = df_mean.index
    plt.plot(x, df_mean, color="white", lw=2)
    plt.fill_between(x, df_mean - df_se, df_mean + df_se, color="#3F5D7D")

    # Decorations
    # Lighten borders
    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(1)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(1)
    plt.xticks(x[::2], [str(d) for d in x[::2]], fontsize=12)
    plt.title("User Orders by Hour of Day (95% confidence)", fontsize=22)
    plt.xlabel("Hour of Day")

    s, e = plt.gca().get_xlim()
    plt.xlim(s, e)

    # Draw Horizontal Tick lines
    for y in range(8, 20, 2):
        plt.hlines(y, xmin=s, xmax=e, colors='black', alpha=0.5, linestyles="--", lw=0.5)

    plt.show()

    df_raw = pd.read_csv('dataVset/orders_45d.csv',
                         parse_dates=['purchase_time', 'purchase_date'])

    # Prepare Data: Daily Mean and SE Bands
    df_mean = df_raw.groupby('purchase_date').quantity.mean()
    df_se = df_raw.groupby('purchase_date').quantity.apply(sem).mul(1.96)

    # Plot
    plt.figure(figsize=(16, 10), dpi=80)
    plt.ylabel("# Daily Orders", fontsize=16)
    x = [d.date().strftime('%Y-%m-%d') for d in df_mean.index]
    plt.plot(x, df_mean, color="white", lw=2)
    plt.fill_between(x, df_mean - df_se, df_mean + df_se, color="#3F5D7D")

    # Decorations
    # Lighten borders
    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(1)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(1)
    plt.xticks(x[::6], [str(d) for d in x[::6]], fontsize=12)
    plt.title("Daily Order Quantity of Brazilian Retail with Error Bands (95% confidence)", fontsize=20)

    # Axis limits
    s, e = plt.gca().get_xlim()
    plt.xlim(s, e - 2)
    plt.ylim(4, 10)

    # Draw Horizontal Tick lines
    for y in range(5, 10, 1):
        plt.hlines(y, xmin=s, xmax=e, colors='black', alpha=0.5, linestyles="--", lw=0.5)
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
    plt.show()

###=============================================================================================
def Stacked_Area_Chart(self):
    df = pd.read_csv('dataVset/nightvisitors.csv')

    # Decide Colors
    mycolors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:brown', 'tab:grey', 'tab:pink', 'tab:olive']

    # Draw Plot and Annotate
    fig, ax = plt.subplots(1, 1, figsize=(16, 9), dpi=80)
    columns = df.columns[1:]
    labs = columns.values.tolist()

    # Prepare data
    x = df['yearmon'].values.tolist()
    y0 = df[columns[0]].values.tolist()
    y1 = df[columns[1]].values.tolist()
    y2 = df[columns[2]].values.tolist()
    y3 = df[columns[3]].values.tolist()
    y4 = df[columns[4]].values.tolist()
    y5 = df[columns[5]].values.tolist()
    y6 = df[columns[6]].values.tolist()
    y7 = df[columns[7]].values.tolist()
    y = np.vstack([y0, y2, y4, y6, y7, y5, y1, y3])

    # Plot for each column
    labs = columns.values.tolist()
    ax = plt.gca()
    ax.stackplot(x, y, labels=labs, colors=mycolors, alpha=0.8)

    # Decorations
    ax.set_title('Night Visitors in Australian Regions', fontsize=18)
    ax.set(ylim=[0, 100000])
    ax.legend(fontsize=10, ncol=4)
    plt.xticks(x[::5], fontsize=10, horizontalalignment='center')
    plt.yticks(np.arange(10000, 100000, 20000), fontsize=10)
    plt.xlim(x[0], x[-1])

    # Lighten borders
    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(.3)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(.3)
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
    plt.show()
###=============================================================================================
def Area_Chart_UnStacked(self):
    df = pd.read_csv("dataVset/economics.csv")

    # Prepare Data
    x = df['date'].values.tolist()
    y1 = df['psavert'].values.tolist()
    y2 = df['uempmed'].values.tolist()
    mycolors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:brown', 'tab:grey', 'tab:pink', 'tab:olive']
    columns = ['psavert', 'uempmed']

    # Draw Plot
    fig, ax = plt.subplots(1, 1, figsize=(16, 9), dpi=80)
    ax.fill_between(x, y1=y1, y2=0, label=columns[1], alpha=0.5, color=mycolors[1], linewidth=2)
    ax.fill_between(x, y1=y2, y2=0, label=columns[0], alpha=0.5, color=mycolors[0], linewidth=2)

    # Decorations
    ax.set_title('Personal Savings Rate vs Median Duration of Unemployment', fontsize=18)
    ax.set(ylim=[0, 30])
    ax.legend(loc='best', fontsize=12)
    plt.xticks(x[::50], fontsize=10, horizontalalignment='center')
    plt.yticks(np.arange(2.5, 30.0, 2.5), fontsize=10)
    plt.xlim(-10, x[-1])

    # Draw Tick lines
    for y in np.arange(2.5, 30.0, 2.5):
        plt.hlines(y, xmin=0, xmax=len(x), colors='black', alpha=0.3, linestyles="--", lw=0.5)

    # Lighten borders
    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(.3)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(.3)
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
    plt.show()

###=============================================================================================
def Calendar_Heat_Map(self):
    df = pd.read_csv("dataVset/yahoo.csv", parse_dates=['date'])
    df.set_index('date', inplace=True)

    # Plot
    # plt.figure(figsize=(16, 10), dpi=80)
    calmap.calendarplot(df['2014']['VIX.Close'], fig_kws={'figsize': (16, 10)},
                            yearlabel_kws={'color': 'black', 'fontsize': 14},
                            subplot_kws={'title': 'Yahoo Stock Prices'})

    plt.show()

###=============================================================================================
def Seasonal_Plot(self):
    df = pd.read_csv('dataVset/AirPassengers.csv')

    # Prepare data
    df['year'] = [parse(d).year for d in df.date]
    df['month'] = [parse(d).strftime('%b') for d in df.date]
    years = df['year'].unique()

    # Draw Plot
    mycolors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:brown', 'tab:grey', 'tab:pink', 'tab:olive',
                'deeppink', 'steelblue', 'firebrick', 'mediumseagreen']
    plt.figure("Seasonal Plot",figsize=(16, 10), dpi=80)

    for i, y in enumerate(years):
        plt.plot('month', 'value', data=df.loc[df.year == y, :], color=mycolors[i], label=y)
        plt.text(df.loc[df.year == y, :].shape[0] - .9, df.loc[df.year == y, 'value'][-1:].values[0], y, fontsize=12,
                 color=mycolors[i])

    # Decoration
    plt.ylim(50, 750)
    plt.xlim(-0.3, 11)
    plt.ylabel('$Air Traffic$')
    plt.yticks(fontsize=12, alpha=.7)
    plt.title("Monthly Seasonal Plot: Air Passengers Traffic (1949 - 1969)", fontsize=22)
    plt.grid(axis='y', alpha=.3)

    # Remove borders
    plt.gca().spines["top"].set_alpha(0.0)
    plt.gca().spines["bottom"].set_alpha(0.5)
    plt.gca().spines["right"].set_alpha(0.0)
    plt.gca().spines["left"].set_alpha(0.5)
    # plt.legend(loc='upper right', ncol=2, fontsize=12)
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
    plt.show()
###=============================================================================================
