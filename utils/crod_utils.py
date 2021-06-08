import numpy as np
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import ListedColormap, BoundaryNorm
from sklearn import neighbors
import matplotlib.patches as mpatches
import graphviz
import seaborn as sns
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
    plt.yticks(np.arange(c_features), feature_names)


def plot_horizontal_bar(df, column, xlabel, title,  fix_distance, hide_ylabel=True):
    """
    plota um coutplot horizontal com valores anotados

    :param df: dataframe
    :param column: nome da coluna para plotar a contagem
    :param xlabel: xlabel
    :param title: titulo
    :param fix_distance: valor para somar ou diminuir da distancia da barra
    :param hide_y_label: desabilitar ylabels
    :return:
    """
    df1 = pd.DataFrame(df[column].value_counts(), columns=[column])
    ax = sns.barplot(x=column, y=df1.index, data=df1, palette='mako')

    ax.set_title(title, fontsize=18, pad=30)

    if hide_ylabel:
        ax.set_ylabel('')

    ax.set_xlabel(xlabel, fontsize=14)
    ax.secondary_xaxis('top')
    # ax.annotate('*Dados de 2013 à 2020\n**Valores do estado do RS', xy=(830, 70), xycoords='figure pixels')

    # adicionar valor à barra
    for i, value in enumerate(df1[column]):
        ax.text(value + fix_distance, i + 0.05, "{0:.0f}".format(value), color='white', fontweight='bold', fontsize=12)

    # tamanho dos e yticks labels
    ax.tick_params(axis='both', which='major', labelsize=12)


def show_values_on_bars(axs, fix_distance):
    def _show_on_single_plot(ax):
        for p in ax.patches:
            _x = p.get_x() + p.get_width() / 2  # divide por 2 pra ficar no meio
            _y = p.get_y() + p.get_height() + fix_distance  # mais valor pra n ficar colado na altura da barra
            value = '{:.0f}'.format(p.get_height())
            ax.text(_x, _y, value, ha="center", fontsize=10, color='black',)

    if isinstance(axs, np.ndarray):
        for idx, ax in np.ndenumerate(axs):
            _show_on_single_plot(ax)
    else:
        _show_on_single_plot(axs)


def plot_vertical_bar(df, column, ylabel, title, fix_distance, hue=None, hide_xlabel=True):
    """
     plota um coutplot vertical com valores anotados
    :param df: dataframe
    :param column: coluna para contagem
    :param ylabel: ylabel
    :param title:
    :param fix_distance: valor para somar ou diminuir da distancia da barra
    :param hue: coluna para plotar hue
    :param hide_xlabel:
    :return:
    """
    if hue:
        ax = sns.countplot(x=column, data=df, hue=hue, palette='mako')
    else:
        ax = sns.countplot(x=column, data=df, palette='mako')

    show_values_on_bars(ax, fix_distance)

    ax.set_title(title, fontsize=18, pad=30)
    ax.set_ylabel(ylabel, fontsize=14)
    if hide_xlabel:
        ax.set_xlabel('')
    ax.secondary_yaxis('right')
    #ax.annotate('*Valores do estado do RS', xy=(100, 650), xycoords='figure pixels')

    ax.tick_params(axis='both', which='major', labelsize=12)


def print_df_dimensions(df):
    print("DIMENSÕES DO DATAFRAME:")
    print(f"Linhas:\t\t{df.shape[0]}")
    print(f"Colunas:\t{df.shape[1]}")


def get_percents(df, column):
    """
        Retorna a quantidade e a porcentagem de valores em uma coluna
    :param df: df
    :param column: nome da coluna
    :return:
    """
    df1 = df[column].value_counts().rename_axis(column).reset_index(name='QTD')
    df2 = (df[column].value_counts(normalize=True) * 100).rename_axis(column).reset_index(name='%').drop(
        columns=column)
    return pd.concat([df1, df2], axis=1)

