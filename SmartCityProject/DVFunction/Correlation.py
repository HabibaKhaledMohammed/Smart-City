import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import seaborn as sns
import statistics
import collections
import random
import itertools
import warnings
import warnings; warnings.filterwarnings('ignore')
##try:
    ##import collections.abc as collections_abc # only works on python 3.3+
##except ImportError:
    ##import collections as collections_abc

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

def Scatter_plot(self):
    midwest = pd.read_csv("dataVset/midwest_filter.csv")

    # Prepare Data
    # Create as many colors as there are unique midwest['category']
    categories = np.unique(midwest['category'])
    #colors = [plt.cm.tab10(i / float(len(categories) - 1)) for i in range(len(categories))]
    color = ["blue","red","green","yellow","purple","brown","black","pink","orange","black","crimson","gray","skyblue","violet"]
    # Draw Plot for Each Category
    plt.figure("Scatter plot",figsize=(16, 10), dpi=80, facecolor='w', edgecolor='k')
    for i, category in enumerate(categories):
        plt.scatter('area', 'poptotal',
                    data=midwest.loc[midwest.category == category, :],
                    s=20, c=color[i%14], label=str(category))

    # Decorations
    plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 90000),
                  xlabel='Area', ylabel='Population')
    plt.xticks(fontsize=12);
    plt.yticks(fontsize=12)
    plt.title("Scatterplot of Midwest Area vs Population", fontsize=22)
    plt.legend(fontsize=12)


    plt.rcParams.update(params)
    plt.style.use('seaborn-whitegrid')
    sns.set_style("white")
    mean = midwest['area'].mean()
    median = midwest['area'].median()
    mode = midwest['area'].mode().get_values()[0]
    variance = statistics.variance(midwest['area'])
    stdev = statistics.stdev(midwest['area'])
    plt.axvline(mean, color='r', linestyle='--')
    plt.axvline(median, color='g', linestyle='-')
    plt.axvline(mode, color='b', linestyle='-')
    plt.axvline(variance, color='r', linestyle='-')
    plt.axvline(stdev, color='b', linestyle='--')
    plt.legend({'Mean': mean, 'Median': median, 'Mode': mode, 'variance': variance, 'standard deviation': stdev})
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
    plt.show()
    #try:
       # collectionsAbc = collections.abc
    #except AttributeError:
        #collectionsAbc = collections

###=============================================================================================
def Bubble_plot_with_Encircling(self):

    # Step 1: Prepare Data
    midwest = pd.read_csv("dataVset/midwest_filter.csv")

    # As many colors as there are unique midwest['category']
    categories = np.unique(midwest['category'])
    color = ["blue", "red", "green", "yellow", "purple", "brown", "black", "pink", "orange", "black", "crimson", "gray",
             "skyblue", "violet"]

    # Step 2: Draw Scatterplot with unique color for each category
    fig = plt.figure("Bubble plot with Encircling",figsize=(16, 10), dpi= 80, facecolor='w', edgecolor='k')

    for i, category in enumerate(categories):
        plt.scatter('area', 'poptotal', data=midwest.loc[midwest.category==category, :], s='dot_size', c=color[i%14], label=str(category), edgecolors='black', linewidths=.5)

    # Step 3: Encircling
    # https://stackoverflow.com/questions/44575681/how-do-i-encircle-different-data-sets-in-scatter-plot
    def encircle(x,y, ax=None, **kw):
        if not ax: ax=plt.gca()
        p = np.c_[x, y]
        hull = ConvexHull(p)
        poly = plt.Polygon(p[hull.vertices,:], **kw)
        ax.add_patch(poly)

    # Select data to be encircled
    midwest_encircle_data = midwest.loc[midwest.state=='IN', :]

    # Draw polygon surrounding vertices
    encircle(midwest_encircle_data.area, midwest_encircle_data.poptotal, ec="k", fc="gold", alpha=0.1)
    encircle(midwest_encircle_data.area, midwest_encircle_data.poptotal, ec="firebrick", fc="none", linewidth=1.5)

    # Step 4: Decorations
    plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 90000),
              xlabel='Area', ylabel='Population')

    plt.xticks(fontsize=12); plt.yticks(fontsize=12)
    plt.title("Bubble Plot with Encircling", fontsize=22)
    plt.legend(fontsize=12)
    mean = midwest['area'].mean()
    median = midwest['area'].median()
    mode = midwest['area'].mode().get_values()[0]
    variance = statistics.variance(midwest['area'])
    stdev = statistics.stdev(midwest['area'])
    plt.axvline(mean, color='r', linestyle='--')
    plt.axvline(median, color='g', linestyle='-')
    plt.axvline(mode, color='b', linestyle='-')
    plt.axvline(variance, color='r', linestyle='-')
    plt.axvline(stdev, color='b', linestyle='--')
    plt.legend({'Mean': mean, 'Median': median, 'Mode': mode, 'variance': variance, 'standard deviation': stdev})
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
    plt.show()
###=============================================================================================

def Scatter_plot_with_linear_regression_line_of_best_fit(self):

    df = pd.read_csv("dataVset/mpg_ggplot2.csv")
    df_select = df.loc[df.cyl.isin([4, 8]), :]

    # Plot
    sns.set_style("white")
    #plt.figure("Scatter plot with linear regression line of best fit",figsize=(20,15))
    gridobj = sns.lmplot(x="displ", y="hwy", hue="cyl", data=df_select,
                         height=7, aspect=1.3, robust=True, palette='tab10',
                         scatter_kws=dict(s=50, linewidths=.5, edgecolors='black'))

    # Decorations
    gridobj.set(xlim=(0.0, 7.5), ylim=(0, 40))
    plt.title("Scatterplot with line of best fit grouped by number of cylinders", fontsize=12)
    mean = df['displ'].mean()
    median = df['displ'].median()
    mode = df['displ'].mode().get_values()[0]
    plt.axvline(mean, color='r', linestyle='--')
    plt.axvline(median, color='orange', linestyle='-')
    plt.axvline(mode, color='b', linestyle='-')
    plt.legend({'Mean': mean, 'Median': median, 'Mode': mode})
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
    plt.show()

###=============================================================================================
def Each_regression_line_in_its_own_column(self):
    df = pd.read_csv("dataVset/mpg_ggplot2.csv")
    df_select = df.loc[df.cyl.isin([4, 8]), :]

    # Each line in its own column
    sns.set_style("white")
    gridobj = sns.lmplot(x="displ", y="hwy",
                         data=df_select,
                         height=7,
                         robust=True,
                         palette='Set1',
                         col="cyl",
                         scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))

    # Decorations
    gridobj.set(xlim=(0.5, 7.5), ylim=(0, 50))
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
    plt.show()
###=============================================================================================
def Jittering_with_stripplot(self):
    df = pd.read_csv("dataVset/mpg_ggplot2.csv")

    # Draw Stripplot
    fig, ax = plt.subplots(figsize=(16, 10), dpi=80)
    sns.stripplot(df.cty, df.hwy, jitter=0.25, size=8, ax=ax, linewidth=.5)

    # Decorations
    plt.title('Use jittered plots to avoid overlapping of points', fontsize=22)
    mean = df['cty'].mean()
    median = df['cty'].median()
    mode = df['cty'].mode().get_values()[0]
    variance = statistics.variance(df['cty'])
    stdev = statistics.stdev(df['cty'])
    plt.axvline(mean, color='r', linestyle='--')
    plt.axvline(median, color='g', linestyle='-')
    plt.axvline(mode, color='b', linestyle='-')
    plt.axvline(variance, color='r', linestyle='-')
    plt.axvline(stdev, color='b', linestyle='--')
    plt.legend({'Mean': mean, 'Median': median, 'Mode': mode, 'variance': variance, 'standard deviation': stdev})
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
    plt.show()
###=============================================================================================
def Counts_Plot(self):
    df = pd.read_csv("dataVset/mpg_ggplot2.csv")
    df_counts = df.groupby(['hwy', 'cty']).size().reset_index(name='counts')

    # Draw Stripplot
    fig, ax = plt.subplots(figsize=(16, 10), dpi=80)
    sns.stripplot(df_counts.cty, df_counts.hwy, size=df_counts.counts * 2, ax=ax)

    # Decorations
    plt.title('Counts Plot - Size of circle is bigger as more points overlap', fontsize=22)
    mean = df['cty'].mean()
    median = df['cty'].median()
    mode = df['cty'].mode().get_values()[0]
    variance = statistics.variance(df['cty'])
    stdev = statistics.stdev(df['cty'])
    plt.axvline(mean, color='r', linestyle='--')
    plt.axvline(median, color='g', linestyle='-')
    plt.axvline(mode, color='b', linestyle='-')
    plt.axvline(variance, color='r', linestyle='-')
    plt.axvline(stdev, color='b', linestyle='--')
    plt.legend({'Mean': mean, 'Median': median, 'Mode': mode, 'variance': variance, 'standard deviation': stdev})
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
    plt.show()
###=============================================================================================
def Marginal_Histogram(self):
    df = pd.read_csv("dataVset/mpg_ggplot2.csv")

    # Create Fig and gridspec
    fig = plt.figure("Marginal Histogram",figsize=(16, 10), dpi=80)
    grid = plt.GridSpec(4, 4, hspace=0.5, wspace=0.2)

    # Define the axes
    ax_main = fig.add_subplot(grid[:-1, :-1])
    ax_right = fig.add_subplot(grid[:-1, -1], xticklabels=[], yticklabels=[])
    ax_bottom = fig.add_subplot(grid[-1, 0:-1], xticklabels=[], yticklabels=[])

    # Scatterplot on main ax
    ax_main.scatter('displ', 'hwy', s=df.cty * 4, c=df.manufacturer.astype('category').cat.codes, alpha=.9, data=df,
                    cmap="tab10", edgecolors='gray', linewidths=.5)

    # histogram on the right
    ax_bottom.hist(df.displ, 40, histtype='stepfilled', orientation='vertical', color='deeppink')
    ax_bottom.invert_yaxis()

    # histogram in the bottom
    ax_right.hist(df.hwy, 40, histtype='stepfilled', orientation='horizontal', color='deeppink')

    # Decorations
    ax_main.set(title='Scatterplot with Histograms \n displ vs hwy', xlabel='displ', ylabel='hwy')
    ax_main.title.set_fontsize(20)
    for item in ([ax_main.xaxis.label, ax_main.yaxis.label] + ax_main.get_xticklabels() + ax_main.get_yticklabels()):
        item.set_fontsize(14)

    xlabels = ax_main.get_xticks().tolist()
    ax_main.set_xticklabels(xlabels)
    mean = df['displ'].mean()
    median = df['displ'].median()
    mode = df['displ'].mode().get_values()[0]
    variance = statistics.variance(df['displ'])
    stdev = statistics.stdev(df['displ'])
    plt.axvline(mean, color='r', linestyle='--')
    plt.axvline(median, color='g', linestyle='-')
    plt.axvline(mode, color='b', linestyle='-')
    plt.axvline(variance, color='r', linestyle='-')
    plt.axvline(stdev, color='b', linestyle='--')
    plt.legend({'Mean': mean, 'Median': median, 'Mode': mode, 'variance': variance, 'standard variance': stdev})
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
    plt.show()
###=============================================================================================
def Marginal_Boxplot(self):
    df = pd.read_csv("dataVset/mpg_ggplot2.csv")

    # Create Fig and gridspec
    fig = plt.figure("Marginal Boxplot",figsize=(16, 10), dpi=80)
    grid = plt.GridSpec(4, 4, hspace=0.5, wspace=0.2)

    # Define the axes
    ax_main = fig.add_subplot(grid[:-1, :-1])
    ax_right = fig.add_subplot(grid[:-1, -1], xticklabels=[], yticklabels=[])
    ax_bottom = fig.add_subplot(grid[-1, 0:-1], xticklabels=[], yticklabels=[])

    # Scatterplot on main ax
    ax_main.scatter('displ', 'hwy', s=df.cty * 5, c=df.manufacturer.astype('category').cat.codes, alpha=.9, data=df,
                    cmap="Set1", edgecolors='black', linewidths=.5)

    # Add a graph in each part
    sns.boxplot(df.hwy, ax=ax_right, orient="v")
    sns.boxplot(df.displ, ax=ax_bottom, orient="h")

    # Decorations ------------------
    # Remove x axis name for the boxplot
    ax_bottom.set(xlabel='')
    ax_right.set(ylabel='')

    # Main Title, Xlabel and YLabel
    ax_main.set(title='Scatterplot with Histograms \n displ vs hwy', xlabel='displ', ylabel='hwy')

    # Set font size of different components
    ax_main.title.set_fontsize(20)
    for item in ([ax_main.xaxis.label, ax_main.yaxis.label] + ax_main.get_xticklabels() + ax_main.get_yticklabels()):
        item.set_fontsize(14)
    mean = df['displ'].mean()
    median = df['displ'].median()
    mode = df['displ'].mode().get_values()[0]
    variance = statistics.variance(df['displ'])
    stdev = statistics.stdev(df['displ'])
    plt.axvline(mean, color='r', linestyle='--')
    plt.axvline(median, color='g', linestyle='-')
    plt.axvline(mode, color='b', linestyle='-')
    plt.axvline(variance, color='r', linestyle='-')
    plt.axvline(stdev, color='b', linestyle='--')
    plt.legend({'Mean': mean, 'Median': median, 'Mode': mode, 'variance': variance, 'standard variance': stdev})
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
    plt.show()
###=============================================================================================
def Correllogram(self):
    df = pd.read_csv("dataVset/mtcars.csv")

    # Plot
    plt.figure("Correllogram",figsize=(12, 10), dpi=80)
    sns.heatmap(df.corr(), xticklabels=df.corr().columns, yticklabels=df.corr().columns, cmap='RdYlGn', center=0,
                annot=True)

    # Decorations
    plt.title('Correlogram of mtcars', fontsize=22)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
    plt.show()
###=============================================================================================
def Pairwise_Plot(self):
    df = sns.load_dataset('iris')

    # Plot
    # plt.figure(figsize=(10,8), dpi= 80)
    sns.pairplot(df, kind="scatter", hue="species", plot_kws=dict(s=80, edgecolor="white", linewidth=2.5))
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
    plt.show()

   # df1 = sns.load_dataset('iris')

    # Plot
    #plt.figure(figsize=(10,8), dpi= 80)
   # sns.pairplot(df1, kind="reg", hue="species")
    #plt.show()

###=============================================================================================
