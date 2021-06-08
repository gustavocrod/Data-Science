import numpy
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import ListedColormap, BoundaryNorm
from sklearn import neighbors
import matplotlib.patches as mpatches
import graphviz
from sklearn.tree import export_graphviz
import matplotlib.patches as mpatches

def plot_decision_tree(clf, feature_names, class_names):
    """

    :param clf: instancia do classificador
    :param feature_names: df.columns
    :param class_names: target.unique()
    :return:
    """
    # This function requires the pydotplus module and assumes it's been installed.

    export_graphviz(clf, out_file="crod_tree_temp.dot", feature_names=feature_names, class_names=class_names, filled = True, impurity = False)
    with open("crod_tree_temp.dot") as f:
        dot_graph = f.read()
    # Alternate method using pydotplus, if installed.
    # graph = pydotplus.graphviz.graph_from_dot_data(dot_graph)
    # return graph.create_png()
    return graphviz.Source(dot_graph)

def plot_feature_importances(clf, feature_names):
    """

    :param clf: modelo
    :param feature_names: df.columns
    :return:
    """
    c_features = len(feature_names)
    plt.barh(range(c_features), clf.feature_importances_)
    plt.xlabel("Feature importance")
    plt.ylabel("Feature name")
    plt.yticks(numpy.arange(c_features), feature_names)

