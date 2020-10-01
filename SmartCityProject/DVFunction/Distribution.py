import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joypy
import statistics
import warnings; warnings.filterwarnings('ignore')
import warnings; warnings.filterwarnings(action='once')
import matplotlib; matplotlib.use('TkAgg')
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
def HistogramforContinuousVariable(self):

    df = pd.read_csv("dataVset/mpg_ggplot2.csv")

    # Prepare data
    x_var = 'displ'
    groupby_var = 'class'
    df_agg = df.loc[:, [x_var, groupby_var]].groupby(groupby_var)
    vals = [df[x_var].values.tolist() for i, df in df_agg]

    # Draw
    # Draw
    plt.figure("Histogram for Continuous Variable",figsize=(16, 9), dpi=80)
    colors = [plt.cm.Spectral(i / float(len(vals) - 1)) for i in range(len(vals))]
    n, bins, patches = plt.hist(vals, 30, stacked=True, density=False, color=colors[:len(vals)])
    # Decoration
    plt.legend({group: col for group, col in zip(np.unique(df[groupby_var]).tolist(), colors[:len(vals)])})
    plt.title(f"Stacked Histogram of ${x_var}$ colored by ${groupby_var}$", fontsize=22)
    plt.xlabel(x_var)
    plt.ylabel("Frequency")
    plt.ylim(0, 25)
    plt.xticks(ticks=bins[::3], labels=[round(b, 1) for b in bins[::3]])
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
    plt.legend({'Mean': mean, 'Median': median, 'Mode': mode, 'variance': variance, 'standard deviation': stdev})
    plt.show()




###=============================================================================================
def HistogramforCategoricalVariable(self):
    # Import Data
    df = pd.read_csv("dataVset/mpg_ggplot2.csv")

    # Prepare data
    x_var = 'manufacturer'
    groupby_var = 'class'
    df_agg = df.loc[:, [x_var, groupby_var]].groupby(groupby_var)
    vals = [df[x_var].values.tolist() for i, df in df_agg]

    # Draw
    plt.figure("Histogram for Categorical Variable",figsize=(16, 9), dpi=80)
    colors = [plt.cm.Spectral(i / float(len(vals) - 1)) for i in range(len(vals))]
    n, bins, patches = plt.hist(vals, df[x_var].unique().__len__(), stacked=True, density=False,
                                color=colors[:len(vals)])

    # Decoration
    plt.legend({group: col for group, col in zip(np.unique(df[groupby_var]).tolist(), colors[:len(vals)])})
    plt.title(f"Stacked Histogram of ${x_var}$ colored by ${groupby_var}$", fontsize=22)
    plt.xlabel(x_var)
    plt.ylabel("Frequency")
    plt.ylim(0, 40)
    plt.xticks(ticks=bins, labels=np.unique(df[x_var]).tolist(), rotation=90, horizontalalignment='left')
    """""
    mean = df['manufacturer'].mean()
    median = df['manufacturer'].median()
    mode = df['manufacturer'].mode().get_values()[0]
    variance = statistics.variance(df['manufacturer'])
    stdev = statistics.stdev(df['manufacturer'])
    plt.axvline(mean, color='r', linestyle='--')
    plt.axvline(median, color='g', linestyle='-')
    plt.axvline(mode, color='b', linestyle='-')
    plt.axvline(variance, color='r', linestyle='-')
    plt.axvline(stdev, color='b', linestyle='--')
    plt.legend({'Mean': mean, 'Median': median, 'Mode': mode, 'variance': variance, 'standard deviation': stdev})
    """""
    plt.show()

###=============================================================================================
def DensityPlot(self):
    # Import Data
    df = pd.read_csv("dataVset/mpg_ggplot2.csv")

    # Draw Plot
    plt.figure("Density Plot",figsize=(16, 10), dpi=80)
    sns.kdeplot(df.loc[df['cyl'] == 4, "cty"], shade=True, color="g", label="Cyl=4", alpha=.7)
    sns.kdeplot(df.loc[df['cyl'] == 5, "cty"], shade=True, color="deeppink", label="Cyl=5", alpha=.7)
    sns.kdeplot(df.loc[df['cyl'] == 6, "cty"], shade=True, color="dodgerblue", label="Cyl=6", alpha=.7)
    sns.kdeplot(df.loc[df['cyl'] == 8, "cty"], shade=True, color="orange", label="Cyl=8", alpha=.7)

    # Decoration
    plt.title('Density Plot of City Mileage by n_Cylinders', fontsize=22)
    plt.legend()
    mean = df['hwy'].mean()
    median = df['hwy'].median()
    mode = df['hwy'].mode().get_values()[0]
    variance = statistics.variance(df['hwy'])
    stdev = statistics.stdev(df['hwy'])
    plt.axvline(mean, color='r', linestyle='--')
    plt.axvline(median, color='g', linestyle='-')
    plt.axvline(mode, color='b', linestyle='-')
    plt.axvline(variance, color='r', linestyle='-')
    plt.axvline(stdev, color='b', linestyle='--')
    plt.legend({'Mean': mean, 'Median': median, 'Mode': mode, 'variance': variance, 'standard deviation': stdev})
    plt.show()

###=============================================================================================
def DensityCurveswithHistogram(self):
    # Import Data
    df = pd.read_csv("dataVset/mpg_ggplot2.csv")

    # Draw Plot
    plt.figure("Density Curves with Histogram",figsize=(13, 10), dpi=80)
    sns.distplot(df.loc[df['class'] == 'compact', "cty"], color="dodgerblue", label="Compact", hist_kws={'alpha': .7},
                 kde_kws={'linewidth': 3})
    sns.distplot(df.loc[df['class'] == 'suv', "cty"], color="orange", label="SUV", hist_kws={'alpha': .7},
                 kde_kws={'linewidth': 3})
    sns.distplot(df.loc[df['class'] == 'minivan', "cty"], color="g", label="minivan", hist_kws={'alpha': .7},
                 kde_kws={'linewidth': 3})
    plt.ylim(0, 0.35)

    # Decoration
    plt.title('Density Plot of City Mileage by Vehicle Type', fontsize=22)
    plt.legend()
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
    plt.show()
###=============================================================================================
def  JoyPlot(self):
    # !pip install joypy
    # Import Data
    mpg = pd.read_csv("dataVset/mpg_ggplot2.csv")

    # Draw Plot
    #plt.figure(figsize=(16, 10), dpi=80)
    fig, axes = joypy.joyplot(mpg, column=['hwy', 'cty'], by="class", ylim='own', figsize=(14, 10))

    # Decoration
    plt.title('Joy Plot of City and Highway Mileage by Class', fontsize=22)
    """""
    mean = mpg['cty'].mean()
    median = mpg['cty'].median()
    mode = mpg['cty'].mode().get_values()[0]
    variance = statistics.variance(mpg['cty'])
    stdev = statistics.stdev(mpg['cty'])
    plt.axvline(mean, color='r', linestyle='--')
    plt.axvline(median, color='g', linestyle='-')
    plt.axvline(mode, color='b', linestyle='-')
    plt.axvline(variance, color='r', linestyle='-')
    plt.axvline(stdev, color='b', linestyle='--')
    plt.legend({'Mean': mean, 'Median': median, 'Mode': mode, 'variance': variance, 'standard deviation': stdev})
    """""
    plt.show()

###=============================================================================================
def DistributedDotPlot(self):
    # Prepare Data
    df_raw = pd.read_csv("dataVset/mpg_ggplot2.csv")
    cyl_colors = {4: 'tab:red', 5: 'tab:green', 6: 'tab:blue', 8: 'tab:orange'}
    df_raw['cyl_color'] = df_raw.cyl.map(cyl_colors)

    # Mean and Median city mileage by make
    df = df_raw[['cty', 'manufacturer']].groupby('manufacturer').apply(lambda x: x.mean())
    df.sort_values('cty', ascending=False, inplace=True)
    df.reset_index(inplace=True)
    df_median = df_raw[['cty', 'manufacturer']].groupby('manufacturer').apply(lambda x: x.median())

    # Draw horizontal lines
    fig, ax = plt.subplots(figsize=(16, 10), dpi=80)
    ax.hlines(y=df.index, xmin=0, xmax=40, color='gray', alpha=0.5, linewidth=.5, linestyles='dashdot')

    # Draw the Dots
    for i, make in enumerate(df.manufacturer):
        df_make = df_raw.loc[df_raw.manufacturer == make, :]
        ax.scatter(y=np.repeat(i, df_make.shape[0]), x='cty', data=df_make, s=75, edgecolors='gray', c='w', alpha=0.5)
        ax.scatter(y=i, x='cty', data=df_median.loc[df_median.index == make, :], s=75, c='firebrick')

    # Annotate
    ax.text(33, 13, "$red ; dots ; are ; the : median$", fontdict={'size': 12}, color='firebrick')

    # Decorations
    red_patch = plt.plot([], [], marker="o", ms=10, ls="", mec=None, color='firebrick', label="Median")
    plt.legend(handles=red_patch)
    ax.set_title('Distribution of City Mileage by Make', fontdict={'size': 22})
    ax.set_xlabel('Miles Per Gallon (City)', alpha=0.7)
    ax.set_yticks(df.index)
    ax.set_yticklabels(df.manufacturer.str.title(), fontdict={'horizontalalignment': 'right'}, alpha=0.7)
    ax.set_xlim(1, 40)
    plt.xticks(alpha=0.7)
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["bottom"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.grid(axis='both', alpha=.4, linewidth=.1)
    mean = df_raw['cty'].mean()
    median = df_raw['cty'].median()
    mode = df_raw['cty'].mode().get_values()[0]
    variance = statistics.variance(df_raw['cty'])
    stdev = statistics.stdev(df_raw['cty'])
    plt.axvline(mean, color='r', linestyle='--')
    plt.axvline(median, color='g', linestyle='-')
    plt.axvline(mode, color='b', linestyle='-')
    plt.axvline(variance, color='r', linestyle='-')
    plt.axvline(stdev, color='b', linestyle='--')
    plt.legend({'Mean': mean, 'Median': median, 'Mode': mode, 'variance': variance, 'standard deviation': stdev})
    plt.show()

###=============================================================================================
def BoxPlot(self):
    # Import Data
    df = pd.read_csv("dataVset/mpg_ggplot2.csv")

    # Draw Plot
    plt.figure("Box Plot",figsize=(13, 10), dpi=80)
    sns.boxplot(x='class', y='hwy', data=df, notch=False)

    # Add N Obs inside boxplot (optional)
    def add_n_obs(df, group_col, y):
        medians_dict = {grp[0]: grp[1][y].median() for grp in df.groupby(group_col)}
        xticklabels = [x.get_text() for x in plt.gca().get_xticklabels()]
        n_obs = df.groupby(group_col)[y].size().values
        for (x, xticklabel), n_ob in zip(enumerate(xticklabels), n_obs):
            plt.text(x, medians_dict[xticklabel] * 1.01, "#obs : " + str(n_ob), horizontalalignment='center',
                     fontdict={'size': 14}, color='white')

    add_n_obs(df, group_col='class', y='hwy')

    # Decoration
    plt.title('Box Plot of Highway Mileage by Vehicle Class', fontsize=22)
    plt.ylim(10, 40)
    plt.show()

###=============================================================================================
def DotPlusBoxPlot(self):
    # Import Data
    df = pd.read_csv("dataVset/mpg_ggplot2.csv")

    # Draw Plot
    plt.figure("Dot + Box Plot",figsize=(13, 10), dpi=80)
    sns.boxplot(x='class', y='hwy', data=df, hue='cyl')
    sns.stripplot(x='class', y='hwy', data=df, color='black', size=3, jitter=1)

    for i in range(len(df['class'].unique()) - 1):
        plt.vlines(i + .5, 10, 45, linestyles='solid', colors='gray', alpha=0.2)

    # Decoration
    plt.title('Box Plot of Highway Mileage by Vehicle Class', fontsize=22)
    plt.legend(title='Cylinders')
    plt.show()

###=============================================================================================
def ViolinPlot(self):
    # Import Data
    df = pd.read_csv("dataVset/mpg_ggplot2.csv")

    # Draw Plot
    plt.figure("Violin Plot",figsize=(13, 10), dpi=80)
    sns.violinplot(x='class', y='hwy', data=df, scale='width', inner='quartile')

    # Decoration
    plt.title('Violin Plot of Highway Mileage by Vehicle Class', fontsize=22)
    plt.show()
   # plt.savefig('demo.png', bbox_inches='tight')

###=============================================================================================
def PopulationPyramid(self):
    # Read data
    df = pd.read_csv("dataVset/email_campaign_funnel.csv")

    # Draw Plot
    plt.figure("Population Pyramid",figsize=(13, 10), dpi=80)
    group_col = 'Gender'
    order_of_bars = df.Stage.unique()[::-1]
    colors = [plt.cm.Spectral(i / float(len(df[group_col].unique()) - 1)) for i in range(len(df[group_col].unique()))]

    for c, group in zip(colors, df[group_col].unique()):
        sns.barplot(x='Users', y='Stage', data=df.loc[df[group_col] == group, :], order=order_of_bars, color=c,
                    label=group)

    # Decorations
    plt.xlabel("$Users$")
    plt.ylabel("Stage of Purchase")
    plt.yticks(fontsize=12)
    plt.title("Population Pyramid of the Marketing Funnel", fontsize=22)
    plt.legend()
    plt.show()

###=============================================================================================

###=============================================================================================
