# --------------------------------------------------------------------------- #
# ---------------------------- LIBRARY IMPORTS ------------------------------ #
# --------------------------------------------------------------------------- #
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
from sklearn import preprocessing 
from sklearn.preprocessing import StandardScaler

# --------------------------------------------------------------------------- #pp
# ----------------------------- DATASET IMPORT ------------------------------ #
# --------------------------------------------------------------------------- #
# 1. When importing libraries, call for the file with: from UNSW_DF import *
# 2. Initiate with: x_train, x_test, y_train, y_test = XY_import()

#--------------------------------------------------------#
#--------code to select dataset on multi_class-----------#
#desiding on The On_hot_encoding or the on_hot_labeling
# ENCODING

encoding = False # if True encoding. if False labeling
train_on_hot_encoding = '../Dataset/train_ppMULT_on_hot.csv'
test_on_hot_encoding = '../Dataset/test_ppMULT_on_hot.csv'
#LABELING
train_on_hot_labeling = "../Dataset/train_pp3_multi.csv"
test_on_hot_labeling = "../Dataset/test_pp3_multi.csv"
# if statement to deside on_hot: label or encoding
if encoding:
    print("one hot encoding dataset is activated")
    train_dataset = train_on_hot_encoding
    test_dataset = test_on_hot_encoding
else:
    print("one hot labeling dataset is activated")
    train_dataset = train_on_hot_labeling
    test_dataset = test_on_hot_labeling
#----------------------------------------------#
#------end of selection dataset code-----------#


def DF_XY():
    """Loads preprocessed dataset files from pre-defined path, and splits into inputs and output.

    Returns:
        x_train, x_test, y_train, y_test: preprocessed splitted dataset
    """
    try:
        print("( 1 ) Reading Preprocessed CSV files..")
        train = pd.read_csv("../Dataset/train_pp3.csv")
        print("\t Training dataset loaded..")
        test = pd.read_csv("../Dataset/test_pp3.csv")
        print("\t Testing dataset loaded..\n")


        print("( 2 ) Loading done, splitting into X and Y..")
        x_train, y_train = train.drop(["label"], axis=1), train["label"]
        x_test, y_test = test.drop(["label"], axis=1), test["label"]
        print('\t ( 2.1 ) x_train Shape: ', '\t', x_train.shape)
        print('\t ( 2.2 ) y_train Shape: ', '\t', y_train.shape)
        print('\t ( 2.3 ) x_test Shape: ', '\t', x_test.shape)
        print('\t ( 2.4 ) y_test Shape: ', '\t', y_test.shape)

        print("( 3 ) Done!")
        print("PS! Import with: x_train, x_test, y_train, y_test = XY_import()")

        x_train = np.asarray(x_train).astype(np.float64)
        y_train = np.asarray(y_train).astype(np.float64)


        x_test = np.asarray(x_test).astype(np.float64)
        y_test = np.asarray(y_test).astype(np.float64)

    except:
        print("Could not load dataset, try again..")
    return x_train, x_test, y_train, y_test


# --------------------------------------------------------------------------- #pp
# ----------------------------- DATASET IMPORT MULTICLASS ------------------------------ #
# --------------------------------------------------------------------------- #
# 1. When importing libraries, call for the file with: from UNSW_DF import *
# 2. Initiate with: x_train_multi, x_test_multi, y_train_multi, y_test_multi = DF_XY_MULTI()
def DF_XY_MULTI():
    
    """Loads preprocessed dataset files from pre-defined path, and splits into inputs and output.

    Returns:
        x_train, x_test, y_train, y_test: preprocessed splitted dataset
    """
    try:
        print("( 1 ) Reading Preprocessed CSV files..")
        print(f"Train Dataset: {train_dataset} is used!")
        print(f"Test Dataset: {test_dataset} is used!")
        train_multi = pd.read_csv(train_dataset) # selected in code started line 17 if els
        print("\t Training dataset loaded..")
        test_multi = pd.read_csv(test_dataset) # selected in code started line 17 if els
        print("\t Testing dataset loaded..\n")

        print("( 2 ) Loading done, splitting into X and Y..")
        x_train_multi, y_train_multi = train_multi.drop(["attack_cat"], axis=1), train_multi["attack_cat"]
        x_test_multi, y_test_multi = test_multi.drop(["attack_cat"], axis=1), test_multi["attack_cat"]
        print('\t ( 2.1 ) x_train Shape: ', '\t', x_train_multi.shape)
        print('\t ( 2.2 ) y_train Shape: ', '\t', y_train_multi.shape)
        print('\t ( 2.3 ) x_test Shape: ', '\t', x_test_multi.shape)
        print('\t ( 2.4 ) y_test Shape: ', '\t', y_test_multi.shape)

        print("( 3 ) Done!")
        print("PS! Import with: x_train_multi, x_test_multi, y_train_multi, y_test_multi = DF_XY_MULTI")

        #random forest and DT does not work when converted to flot Not sure way...
        #x_train_multi = np.asarray(x_train_multi).astype(np.float64)
        #y_train_multi = np.asarray(x_train_multi).astype(np.float64)

        #y_test_multi  = np.asaray(y_test_multi).astype(np.float64)
        #x_test_multi  = np.assary(x_test_multi).astype(np.float64)

    except:
        print("Could not load dataset, try again..")
    return x_train_multi, x_test_multi, y_train_multi, y_test_multi

# For importing the preprocessed dataset by train and test multiclass
def DF_preprocessed_traintest_multi():
    """Loads preprocessed dataset files from pre-defined path.

    Returns:
        train, test: preprocessed dataset
    """
    print("Reading Preprocessed CSV Files..")
    train_multi = pd.read_csv(train_dataset) # selected in code started line 17 if els
    test_multi = pd.read_csv(test_dataset) # selected in code start at line 17 if els
    print(f"Train Dataset: {train_dataset} is used!")
    print(f"Test Dataset: {test_dataset} is used!")
    print('\t Train Shape: ', '\t', train_multi.shape)
    print('\t Test Shape: ', '\t', test_multi.shape)
    print("Dataset Loaded!")
    return train_multi, test_multi


# For importing the preprocessed dataset by train and test
def DF_preprocessed_traintest():
    """Loads preprocessed dataset files from pre-defined path.

    Returns:
        train, test: preprocessed dataset 
    """
    print("Reading Preprocessed CSV Files..")
    train = pd.read_csv("../Dataset/train_pp3.csv")
    test = pd.read_csv("../Dataset/test_pp3.csv")
    print('\t Train Shape: ', '\t', train.shape)
    print('\t Test Shape: ', '\t', test.shape)
    print("Dataset Loaded!")
    return train, test

# For importiong the orignal dataset by train and test
def DF_original_traintest():
    print("Reading Original CSV Files..")
    # importing original dataset
    UNSW_train = pd.read_csv("../Dataset/UNSW_NB15_training-set.csv", delimiter=",")
    UNSW_test = pd.read_csv("../Dataset/UNSW_NB15_testing-set.csv", delimiter=",")
    if UNSW_train.shape < UNSW_test.shape:
        UNSW_train, UNSW_test = UNSW_test, UNSW_train
    print('\t Train Shape: ', '\t', UNSW_train.shape)
    print('\t Test Shape: ', '\t', UNSW_test.shape)
    print("Dataset Loaded!")
    return UNSW_train, UNSW_test


# --------------------------------------------------------------------------- #
# ------------------------ ARTIFICIAL NEURAL NETWORK ------------------------ #
# --------------------------------------------------------------------------- #
# For prediction of ANN models
# The function takes in the dataset, model build and model name as input.
def UNSW_predict_ANN_model(x_train, y_train, x_test, y_test, model, model_name):
    # Printing the name of the model
    print("( 1 ) Running: ", model_name)
    
    # Predicting the training dataset
    print("( 2 ) Predicting on train..")
    train = model.predict(x_train)
    train_scores = model.evaluate(x_train, y_train, verbose=0)
    print('\tAccuracy on training data: \t{}'.format(train_scores[1]))
    print('\tError on training data: \t{}'.format(1 - train_scores[1]), "\n")

    # Predicting the testing dataset
    print("( 3 ) Predicting on test..")
    test = model.predict(x_test)
    test_scores = model.evaluate(x_test, y_test, verbose=0)
    print('\tAccuracy on testing data: \t{}'.format(test_scores[1]))
    print('\tError on testing data: \t\t{}'.format(1 - test_scores[1]), "\n")
    print("( 4 ) Done!")
    
    
# --------------------------------------------------------------------------- #
# ------------------------------ KNN Predict -------------------------------- #
# --------------------------------------------------------------------------- #    
def UNSW_predict_KNN_model(K, x_train, y_train, x_test, y_test):
    """Used to initiate KNN model on our preprocessed dataset.

    Args:
        K (int): K-value for the algorithm
        x_train (dataframe): input train variable
        y_train (dataframe): input test variable
        x_test (dataframe: output train variable
        y_test (dataframe): output test variable
    """
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn import metrics
    print("Predicting KNN model with K = %s" %K)
    # Create KNN Classifier
    knn = KNeighborsClassifier(n_neighbors=K)
    
    # Train the model using the training sets
    knn.fit(x_train, y_train)
    print("Done: Train the model using the training set..")
    
    # Predict the response for test dataset
    y_pred = knn.predict(x_test)
    print("Done: Predict the response for test dataset..")
    print("------------------------------------------------")
    print("Accuracy Score: \t", metrics.accuracy_score(y_test, y_pred))
    print("F1 Score: \t\t", metrics.f1_score(y_test, y_pred))
    print("Precision Score: \t", metrics.precision_score(y_test, y_pred))
    print("Recall Score: \t\t", metrics.recall_score(y_test, y_pred))   
    print("------------------------------------------------")
    print("Classification report for K = %s" %K)
    print(metrics.classification_report(y_test, y_pred))

# --------------------------------------------------------------------------- #
# ------------------------------ PLOTTING  ---------------------------------- #
# --------------------------------------------------------------------------- #
def UNSW_plot_corr_matrix(dataset, title, fig_x, fig_y, x_label_rot=0, y_label_rot=0):
    """Plots correlation matrix based on dataset

    Args:
        dataset (dataframe): dataset to be used
        fig_x (int): figure x size
        fig_y (int): figure y size
    """
    f = plt.figure(figsize=(fig_x, fig_y))
    plt.matshow(dataset.corr(), fignum=f.number)
    
    plt.xticks(range(dataset.select_dtypes(['number']).shape[1]), 
               dataset.select_dtypes(['number']).columns, 
               fontsize=14, 
               rotation=x_label_rot)
    
    plt.yticks(range(dataset.select_dtypes(['number']).shape[1]), 
               dataset.select_dtypes(['number']).columns, 
               fontsize=14,
               rotation = y_label_rot)
    
    cb = plt.colorbar()
    cb.ax.tick_params(labelsize=14)
    plt.title(title, fontsize=16)

def UNSW_barplot(data, to_range, x_label, y_label, title, x_size, y_size):
    """Plots barplot based on x and y labels

    Args:
        x_label (dataframe): input variables
        y_label (dataframe): output variables
        title (string): The title of the plot
        x_size (int): figure x size
        y_size (int): figure y size
    """
    from matplotlib.ticker import PercentFormatter
    from matplotlib.ticker import MultipleLocator
    from matplotlib.ticker import AutoMinorLocator
    # plot bars or kind='barh' for horizontal bars; adjust figsize accordingly
    ax = data.plot(kind='bar', 
                rot=0, 
                xlabel = x_label, 
                ylabel = y_label, 
                title= title, 
                figsize=(x_size, y_size))

    # add some labels
    for c in ax.containers:
        # set the bar label
        ax.bar_label(c, 
                    fmt='%.2f%%', 
                    label_type='edge',
                    rotation=90, 
                    padding=7)

    # add a little space at the top of the plot for the annotation
    ax.margins(y=0.15)
    #ax.xaxis.set_major_locator(matplotlib.ticker.MultipleLocater(1))

    #yRange = np.linspace(0,1,11)
    #ax.set_yticks(yRange, minor=True)

    # Adding lines inbetween the bars
    minor_locator = AutoMinorLocator(2)
    ax.xaxis.set_minor_locator(minor_locator)
    plt.grid(which='minor')

    # Renaming the X ticks labels
    NewRange = range(1, to_range)
    OldRange = range(0,15)
    ax.set_xticks(OldRange)
    ax.set_xticklabels(NewRange)

    # move the legend out of the plot
    ax.legend(title='Metrics', bbox_to_anchor=(1, 1.02), loc='upper left')


# --------------------------------------------------------------------------- #
# --------------------------- DATA ANALYSIS  -------------------------------- #
# --------------------------------------------------------------------------- #    
def UNSW_data_analysis_preprocess(train, test):
    # Defining an empty list
    categorical = []
    # Iterating through the columns and checking for columns with datatyp "Object"
    train.info()

    for col in train.columns:
        if train[col].dtype == 'object':
            categorical.append(col) # appending "object" columns to categorical
            
    non_categorical_columns = [x for x in train.columns if x not in categorical]

    # Label encoding the categorical columns
    le = preprocessing.LabelEncoder()
    print("(1) \tLabel encoding the columns for training and testing set..")  
    # Label encoding the columns for the test and training set
    test[categorical] = test[categorical].apply(le.fit_transform)
    train[categorical] = train[categorical].apply(le.fit_transform)

    print("(2) \tApplying Standardscaler on training dataset..")
    # Applying StandardScaler on train to normalize the values.
    ss = StandardScaler()
    train = pd.DataFrame(ss.fit_transform(train),columns = train.columns)
    print("(3) \tDone!")
    #return train

    train.to_csv('../Dataset/train_pp4.csv', index=False)
    test.to_csv('../Dataset/test_pp4.csv', index=False)


# --------------------------------------------------------------------------- #
# ------------------------------ Utility ------------------------------------ #
# --------------------------------------------------------------------------- #    
def DF_print_shape(x, y):
    """Prints out the shape of each dataframe/array

    Args:
        x (dataframe/array)
        y (dataframe/array)
    """
    print(f"Shape of first data:\t {x.shape} \nShape of second data:\t {y.shape}")

train,test = DF_preprocessed_traintest()
x_train, y_train, x_test, y_test = DF_XY()