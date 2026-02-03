"""Deployment of Financial Inclusion model. Utilities"""
import pandas as pd
import path
import sys


dir = path.Path(__file__).abspath()
sys.path.append(dir.parent.parent)

# helper functions for wrangle function

def group_household_size(x):
    if x<5:
        return 1
    elif x<10:
        return 2
    else:
        return 3

def group_age(x):
    if x>=15 and x<25:
        return (1)
    if x>=25 and x<35:
        return (2)
    if x>=35 and x<45:
        return (3)
    if x>=45 and x<55:
        return (4)
    if x>=55 and x<65:
        return (5)
    if x>=65 and x<75:
        return (6)
    if x>=75 and x<85:
        return (7)
    if x>=85 and x<95:
        return (8)
    if x>=95 and x<=105:
        return (9)

def wrangle(input: pd.DataFrame, test=False):
    """ Wrangle function to process user input
    
    Args:
        input (pd.DataFrame): input data to predict on
        test (bool): False, track test file for necessary differences
                            in processing
    Return:
        df (pd.DataFrame): result of the wrangling process
    """

    # if a df is passed in, no need to read from any csv
    df = input
    
    # conert year to a datetime type
    df.year = pd.to_datetime(df.year.astype('int32'), format='%Y')

    # convert cellphone_access column to boolean
    df.cellphone_access = df.cellphone_access.astype('bool')

    if test == False:
        # convert target column, bank_account, to 0's and 1's
        df.bank_account = df.bank_account.map({'Yes':1, 'No':0})

    # create x group column
    df['age_group'] = list(map(group_age, df.age_of_respondent))

    # group household_sizes
    df['house_size_groups'] = list(map(group_household_size, df.household_size))

    # create 'Other' category in relationship_with_head column
    df.relationship_with_head = df.relationship_with_head.replace({'Other relative':'Other', 'Other non-relatives':'Other'})

    # set index
    df.set_index(df.uniqueid, inplace=True)

    # drop columns
    df.drop(columns=['uniqueid', 'age_of_respondent', 'household_size'], inplace=True)

    return df

def get_options(filepath="./data/Train.csv"):
    """Extract options from the categorical variables instead of typing manual
    
    Args:
        filepath (str): path to the data = "./data/Train.csv"

    Return:
        cat_options (dict): dictionary with key:value of columns(str):options(list)
    """

    # load dataframe
    df = pd.read_csv(filepath)
    # extract categorical columns
    cat_cols = df.select_dtypes("object").columns
    # loop through eac to extract options and store in cat_options
    cat_options = {}
    for cat_col in cat_cols:
        cat_options[cat_col] = df[cat_col].unique()
    del cat_options['uniqueid'] # this is not needed

    return cat_options


# print(get_options())


