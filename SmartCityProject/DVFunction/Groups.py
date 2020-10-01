import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as shc
from sklearn.cluster import AgglomerativeClustering
from scipy.spatial import ConvexHull
import warnings; warnings.filterwarnings(action='once')
from pandas.plotting import andrews_curves
from pandas.plotting import parallel_coordinates
import collections
import warnings; warnings.filterwarnings('ignore')


try:
    import collections.abc as collections_abc # only works on python 3.3+
except ImportError:
    import collections as collections_abc
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
def Dendrogram(self):
    # Import Data
    df = pd.read_csv('dataVset/USArrests.csv')

    # Plot
    plt.figure("Dendrogram",figsize=(16, 10), dpi=80)
    plt.title("USArrests Dendograms", fontsize=22)
    dend = shc.dendrogram(shc.linkage(df[['Murder', 'Assault', 'UrbanPop', 'Rape']], method='ward'),
                          labels=df.State.values, color_threshold=100)
    plt.xticks(fontsize=12)
    plt.show()

###=============================================================================================
def ClusterPlot(self):
    # Import Data
    df = pd.read_csv('dataVset/USArrests.csv')

    # Agglomerative Clustering
    cluster = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
    cluster.fit_predict(df[['Murder', 'Assault', 'UrbanPop', 'Rape']])

    # Plot
    plt.figure("Cluster Plot",figsize=(14, 10), dpi=80)
    plt.scatter(df.iloc[:, 0], df.iloc[:, 1], c=cluster.labels_, cmap='tab10')

    # Encircle
    def encircle(x, y, ax=None, **kw):
        if not ax: ax = plt.gca()
        p = np.c_[x, y]
        hull = ConvexHull(p)
        poly = plt.Polygon(p[hull.vertices, :], **kw)
        ax.add_patch(poly)

    # Draw polygon surrounding vertices
    encircle(df.loc[cluster.labels_ == 0, 'Murder'], df.loc[cluster.labels_ == 0, 'Assault'], ec="k", fc="gold",
             alpha=0.2, linewidth=0)
    encircle(df.loc[cluster.labels_ == 1, 'Murder'], df.loc[cluster.labels_ == 1, 'Assault'], ec="k", fc="tab:blue",
             alpha=0.2, linewidth=0)
    encircle(df.loc[cluster.labels_ == 2, 'Murder'], df.loc[cluster.labels_ == 2, 'Assault'], ec="k", fc="tab:red",
             alpha=0.2, linewidth=0)
    encircle(df.loc[cluster.labels_ == 3, 'Murder'], df.loc[cluster.labels_ == 3, 'Assault'], ec="k", fc="tab:green",
             alpha=0.2, linewidth=0)
    encircle(df.loc[cluster.labels_ == 4, 'Murder'], df.loc[cluster.labels_ == 4, 'Assault'], ec="k", fc="tab:orange",
             alpha=0.2, linewidth=0)

    # Decorations
    plt.xlabel('Murder');
    plt.xticks(fontsize=12)
    plt.ylabel('Assault');
    plt.yticks(fontsize=12)
    plt.title('Agglomerative Clustering of USArrests (5 Groups)', fontsize=22)
    plt.show()

###=============================================================================================
def AndrewsCurve(self):
    # Import
    df = pd.read_csv("dataVset/mtcars.csv")
    df.drop(['cars', 'carname'], axis=1, inplace=True)

    # Plot
    plt.figure("Andrews Curve",figsize=(12, 9), dpi=80)
    andrews_curves(df, 'cyl', colormap='Set1')

    # Lighten borders
    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(.3)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(.3)

    plt.title('Andrews Curves of mtcars', fontsize=22)
    plt.xlim(-3, 3)
    plt.grid(alpha=0.3)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()

###=============================================================================================
def ParallelCoordinates(self):
    # Import Data
    df_final = pd.read_csv("dataVset/diamonds_filter.csv")

    # Plot
    plt.figure("Parallel Coordinates",figsize=(12, 9), dpi=80)
    parallel_coordinates(df_final, 'cut', colormap='Dark2')

    # Lighten borders
    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(.3)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(.3)

    plt.title('Parallel Coordinated of Diamonds', fontsize=22)
    plt.grid(alpha=0.3)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.show()

###=============================================================================================
