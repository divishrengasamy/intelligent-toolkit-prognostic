#====================================================================
# Title:  Main function to create benchmark and plots for toolkit.py
# Author: Divish Rengasamy
# Date:   30 - 04 - 2020
#====================================================================

import pandas as pd
import numpy as np

# Scikit learn
from sklearn.datasets import make_regression
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor 
from sklearn.metrics import *
from sklearn.model_selection import train_test_split, cross_validate, KFold

# Scipy
from scipy.stats import mannwhitneyu

# Tensorflow
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier, KerasRegressor
import tensorflow as tf
import tensorflow_addons as tfa
from tensorflow.keras import layers
from tensorflow.keras.models import load_model

# visuals
import matplotlib
import matplotlib.pyplot as plt
from tqdm import tqdm
plt.style.use('seaborn-pastel')

def create_benchmark(X=None, y=None, new_model_list=None, new_model_name_list=None, custom_scorer_list=None, custom_scorer_name_list=None, num_cv_fold=10):
    """
    Create a pandas table of cross validation result and p-value heatmap plots.

    Parameters
    ----------
    X
        A numpy array of length N by M features. Optional if default dataset exist.
    y
        A numpy array of length N label. Only 1-D allowed. Optional if default dataset exist.
    new_model_list
        A list of scikit model.
    new_model_name_list
        A list of new model names. Optional. If no name given 'custom_model_{NUM}' is used.
    custom_scorer_list
        A list of new scorer. Create using make_scorer from scikit-learn.
    custom_scorer_name_list
        A list of new scorer names. Optional. If no name given 'custom_scorer_{NUM}' is used.
    num_cv_fold
        Numver of cross validation fold. Default value is 10.
    """
    ###############################################################
    # load default dataset
    ###############################################################
    if (X is None) or (y is None):
        """
        If data not provided load, default dataset
        """
        X, y = pd.read_csv('')
    
    
    ###############################################################
    # create a list of models and its names
    ###############################################################
    
    # test case to see if model exist while model name doesn't exist and vice versa
    if ((new_model_name_list is not None) and (new_model_list is None)):
        raise ValueError('Please provide a list of model(s).')
    if ((new_model_name_list is None) and (new_model_list is not None)):
        raise ValueError('Please provide a list of custom model name(s).')
    # check for empty list
    if (new_model_list is not None) and (not new_model_list):
        raise ValueError('new_model_list: Custom model list is empty.')
    if (new_model_name_list is not None) and (not new_model_name_list):
        raise ValueError('new_model_name_list: Custom model name list is empty.')
    
    # models
    models = list()  
    if (new_model_list is not None):
        for new_model in new_model_list:
            models.append(new_model)
      
    models.append(LinearRegression())
    models.append(KNeighborsRegressor())
    models.append(RandomForestRegressor(n_estimators=200, max_depth=5))
    models.append(DummyRegressor())
    
    # models' name
    models_name = list()
    if (new_model_name_list is not None):
        for new_model_name in new_model_name_list:
            assert type(new_model_name) is str
            models_name.append(new_model_name)
        
    models_name.append('Linear Regression')
    models_name.append('K Neighbors Regressor')
    models_name.append('Random Forest')
    models_name.append('Dummy Regressor')
    ###############################################################
    
    ###############################################################
    # create a list of scores and its name
    ###############################################################
    model_scores = list()

    scores_name = ['r2',
              'max error',
              'mean squared error',
              'mean squared log error',
              'median absolute error',
              'root mean squared error',
              'mean absolute error',
              'mean poisson deviance',
              'mean gamma deviance']
    
    scores = {'r2': 'r2',
           'max_error': 'max_error',
           'neg_mean_squared_error': 'neg_mean_squared_error',
           'neg_mean_squared_log_error': 'neg_mean_squared_log_error',
           'neg_median_absolute_error': 'neg_median_absolute_error',
           'neg_root_mean_squared_error': 'neg_root_mean_squared_error',
           'neg_mean_absolute_error': 'neg_mean_absolute_error',
           'neg_mean_poisson_deviance': 'neg_mean_poisson_deviance',
           'neg_mean_gamma_deviance': 'neg_mean_gamma_deviance'}
    
    test_scores = ['test_r2',
                   'test_max_error',
                   'test_neg_mean_squared_error',
                   'test_neg_mean_squared_log_error',
                   'test_neg_median_absolute_error',
                   'test_neg_root_mean_squared_error',
                   'test_neg_mean_absolute_error',
                   'test_neg_mean_poisson_deviance',
                   'test_neg_mean_gamma_deviance']
    ###############################################################
    # ensuring the input of custom model and scorer is OK
    ###############################################################
    
    
    # test case for existence of custom score but not custom score name and vice versa.
    if ((custom_scorer_list is None) and (custom_scorer_name_list is not None)):
        raise ValueError('Please provide a list of custom score(s).')
    if ((custom_scorer_list is not None) and (custom_scorer_name_list is None)):
        raise ValueError('Please provide a list of custom scores name(s).')
    # check for empty list
    if (custom_scorer_list is not None) and (not custom_scorer_list):
        raise ValueError('custom_scorer_list: Custom score list is empty.')
    if (custom_scorer_name_list is not None) and (not custom_scorer_name_list):
        raise ValueError('custom_scorer_name_list: Custom score name list is empty.')
        
    # custom scorers
    if ((custom_scorer_list is not None) and (custom_scorer_name_list is not None)):
        for custom_scorer, custom_scorer_name in zip(custom_scorer_list, custom_scorer_name_list):
            scores.update({f'{custom_scorer_name}': custom_scorer})
    
    # custom scorers' name
    
    if (custom_scorer_name_list is not None):
        for custom_scorer_name in custom_scorer_name_list:
                assert type(custom_scorer_name) is str
                scores_name.append(custom_scorer_name)
                test_scores.append(f'test_{custom_scorer_name}')
      

    # if negative label mean squared log error cannot be used
    if (y[y<0].shape[0] >= 0):
        scores.pop('neg_mean_squared_log_error', None)
        scores.pop('neg_mean_poisson_deviance', None)
        scores.pop('neg_mean_gamma_deviance', None)

        scores_name.remove('mean squared log error')
        scores_name.remove('mean poisson deviance')
        scores_name.remove('mean gamma deviance')

        test_scores.remove('test_neg_mean_squared_log_error')
        test_scores.remove('test_neg_mean_poisson_deviance')
        test_scores.remove('test_neg_mean_gamma_deviance')
    
    ###############################################################
    # cross validate all models
    ###############################################################
    
    # test for feature(X) and label(y) shape
    if (X.shape[0] != y.shape[0]):
        raise ValueError(f'Shape mismatch: Feature data have {X.shape[0]} rows and label have {y.shape[0]} rows. Feature data and  label should have the same number of rows.')
    
    for i in tqdm(range(len(models))):
        
        print(f'Running {models_name[i]}...')
        
        if (models_name[i] == 'Random Forest'):
            y = np.reshape(y, (y.shape[0],)) # (n_row,)
        else:
            y = np.reshape(y, (-1,1)) # (n_row, 1)
            
        model_scores.append(cross_validate(models[i],
                                X,
                                y,
                                cv=num_cv_fold,
                                scoring=scores))
        
    # combine mean and standard deviation in a single string
    def combine_mean_std_np(mean_array, std_array):
        return (f'{mean_array:.4f}\u00B1{std_array:.4f}')
    
    # store results in a matrix
    idx = np.array(models_name)
    col_names = np.array(scores_name)

    all_scores = []
    for i in range(idx.shape[0]):
        all_scores.append([])
        for j in range(col_names.shape[0]):
            all_scores[i].append(combine_mean_std_np(np.abs(model_scores[i][test_scores[j]]).mean(),
                                                    model_scores[i][test_scores[j]].std()))

    # Create dataframe with all result
    df_all_scores = pd.DataFrame(np.array(all_scores),
                                     columns = col_names,
                                     index = idx)
    display(df_all_scores)
    ###############################################################
    # Helper function for matplotlib heatmap plotting
    ###############################################################
    def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", **kwargs):
        """
        Create a heatmap from a numpy array and two lists of labels.

        Parameters
        ----------
        data
            A 2D numpy array of shape (N, M).
        row_labels
            A list or array of length N with the labels for the rows.
        col_labels
            A list or array of length M with the labels for the columns.
        ax
            A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
            not provided, use current axes or create a new one.  Optional.
        cbar_kw
            A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
        cbarlabel
            The label for the colorbar.  Optional.
        **kwargs
            All other arguments are forwarded to `imshow`.
        """

        if not ax:
            ax = plt.gca()

        # Plot the heatmap
        im = ax.imshow(data, **kwargs)

        # Create colorbar
        cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
        cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

        # We want to show all ticks...
        ax.set_xticks(np.arange(data.shape[1]))
        ax.set_yticks(np.arange(data.shape[0]))
        # ... and label them with the respective list entries.
        ax.set_xticklabels(col_labels)
        ax.set_yticklabels(row_labels)

        # Let the horizontal axes labeling appear on top.
        ax.tick_params(top=True, bottom=False,
                       labeltop=True, labelbottom=False)

        # Rotate the tick labels and set their alignment.
        plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
                 rotation_mode="anchor")

        # Turn spines off and create white grid.
        for edge, spine in ax.spines.items():
            spine.set_visible(False)

        ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
        ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
        ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
        ax.tick_params(which="minor", bottom=False, left=False)

        return im, cbar


    def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                         textcolors=["black", "white"],
                         threshold=None, **textkw):
        """
        A function to annotate a heatmap.

        Parameters
        ----------
        im
            The AxesImage to be labeled.
        data
            Data used to annotate.  If None, the image's data is used.  Optional.
        valfmt
            The format of the annotations inside the heatmap.  This should either
            use the string format method, e.g. "$ {x:.2f}", or be a
            `matplotlib.ticker.Formatter`.  Optional.
        textcolors
            A list or array of two color specifications.  The first is used for
            values below a threshold, the second for those above.  Optional.
        threshold
            Value in data units according to which the colors from textcolors are
            applied.  If None (the default) uses the middle of the colormap as
            separation.  Optional.
        **kwargs
            All other arguments are forwarded to each call to `text` used to create
            the text labels.
        """

        if not isinstance(data, (list, np.ndarray)):
            data = im.get_array()

        # Normalize the threshold to the images color range.
        if threshold is not None:
            threshold = im.norm(threshold)
        else:
            threshold = im.norm(data.max())/2.

        # Set default alignment to center, but allow it to be
        # overwritten by textkw.
        kw = dict(horizontalalignment="center",
                  verticalalignment="center")
        kw.update(textkw)

        # Get the formatter in case a string is supplied
        if isinstance(valfmt, str):
            valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

        # Loop over the data and create a `Text` for each "pixel".
        # Change the text's color depending on the data.
        texts = []
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
                text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
                texts.append(text)

        return texts
    
    ###############################################################
    # calculate and plot p-value
    ###############################################################
    for k in range(col_names.shape[0]):
        p_values = []
        for i in range(idx.shape[0]):
            p_values.append([])
            for j in range(idx.shape[0]):
                _, p = mannwhitneyu(model_scores[i][test_scores[k]], model_scores[j][test_scores[k]])
                p_values[i].append(p)


        p_values_np = np.array(p_values)
        p_values_np = np.around(p_values_np, decimals=4)

        fig, ax = plt.subplots()

        im, cbar = heatmap(p_values_np, models_name, models_name, ax=ax,
                           cmap="Blues", cbarlabel="p-value")
        texts = annotate_heatmap(im, valfmt="{x:.4f}")

        plt.title(f'p-value between models using {scores_name[k]}')
        plt.savefig(f'p-value between models using {scores_name[k]}')
        #fig.tight_layout()
        #plt.show()
    
    df_all_scores.to_csv('all_scores.csv', index=False)
    