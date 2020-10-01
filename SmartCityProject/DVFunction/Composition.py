import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull
import seaborn as sns
from pywaffle import Waffle
import squarify
import random
import math
import matplotlib; matplotlib.use('TkAgg')
import warnings; warnings.filterwarnings('ignore')
import warnings; warnings.filterwarnings(action='once')


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


def Waffle_Chart(self):

    df_raw = pd.read_csv("dataVset/mpg_ggplot2.csv")

    # Prepare Data
    df = df_raw.groupby('class').size().reset_index(name='counts')
    n_categories = df.shape[0]
    colors = [plt.cm.inferno_r(i / float(n_categories)) for i in range(n_categories)]

    # Draw Plot and Decorate
    fig = plt.figure(
        "Waffle Chart",
        FigureClass=Waffle,
        plots={
            '111': {
                'values': df['counts'],
                'labels': ["{0} ({1})".format(n[0], n[1]) for n in df[['class', 'counts']].itertuples()],
                'legend': {'loc': 'upper left', 'bbox_to_anchor': (1.05, 1), 'fontsize': 12},
                'title': {'label': '# Vehicles by Class', 'loc': 'center', 'fontsize': 18}
            },
        },
        rows=7,
        colors=colors,
        figsize=(16, 9)
    )
    plt.show()

###=============================================================================================

def Pie_Chart(self):
    df_raw = pd.read_csv("dataVset/mpg_ggplot2.csv")

    # Prepare Data
    df = df_raw.groupby('class').size().reset_index(name='counts')

    # Draw Plot
    fig, ax = plt.subplots(figsize=(12, 7), subplot_kw=dict(aspect="equal"), dpi=80)

    data = df['counts']
    categories = df['class']
    explode = [0, 0, 0, 0, 0, 0.1, 0]

    def func(pct, allvals):
        absolute = int(pct / 100. * np.sum(allvals))
        return "{:.1f}% ({:d} )".format(pct, absolute)

    wedges, texts, autotexts = ax.pie(data,
                                      autopct=lambda pct: func(pct, data),
                                      textprops=dict(color="w"),
                                      colors=plt.cm.Dark2.colors,
                                      startangle=140,
                                      explode=explode)

    # Decoration
    ax.legend(wedges, categories, title="Vehicle Class", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.setp(autotexts, size=10, weight=700)
    ax.set_title("Class of Vehicles: Pie Chart")
    plt.show()

###=============================================================================================

def Treemap(self):
    df_raw = pd.read_csv("dataVset/mpg_ggplot2.csv")

    # Prepare Data
    df = df_raw.groupby('class').size().reset_index(name='counts')
    labels = df.apply(lambda x: str(x[0]) + "\n (" + str(x[1]) + ")", axis=1)
    sizes = df['counts'].values.tolist()
    colors = [plt.cm.Spectral(i / float(len(labels))) for i in range(len(labels))]

    # Draw Plot
    plt.figure("Treemap",figsize=(12, 8), dpi=80)
    squarify.plot(sizes=sizes, label=labels, color=colors, alpha=.8)

    # Decorate
    plt.title('Treemap of Vechile Class')
    plt.axis('off')
    plt.show()

###=============================================================================================

def Bar_Chart(self):
    df_raw = pd.read_csv("dataVset/mpg_ggplot2.csv")

    # Prepare Data
    df = df_raw.groupby('manufacturer').size().reset_index(name='counts')
    n = df['manufacturer'].unique().__len__() + 1
    all_colors = list(plt.cm.colors.cnames.keys())
    random.seed(100)
    c = random.choices(all_colors, k=n)

    # Plot Bars
    plt.figure("Bar Chart",figsize=(16, 10), dpi=80)
    plt.bar(df['manufacturer'], df['counts'], color=c, width=.5)
    for i, val in enumerate(df['counts'].values):
        plt.text(i, val, float(val), horizontalalignment='center', verticalalignment='bottom',
                 fontdict={'fontweight': 500, 'size': 12})

    # Decoration
    plt.gca().set_xticklabels(df['manufacturer'], rotation=60, horizontalalignment='right')
    plt.title("Number of Vehicles by Manaufacturers", fontsize=22)
    plt.ylabel('# Vehicles')
    plt.ylim(0, 45)
    plt.show()

###=============================================================================================