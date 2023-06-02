import streamlit as st
import itertools
import pandas as pd 
import numpy as np 
from scipy.stats import pearsonr
from scipy import stats
import matplotlib.pyplot as plt 
import plotly.express as px
import matplotlib
import seaborn as sns
from sklearn.pipeline import Pipeline
from wordcloud import WordCloud
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
from scipy.stats import chi2_contingency,chi2
import statsmodels.api as sm 
from scipy.stats import spearmanr
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression 
from sklearn.naive_bayes import GaussianNB
from xgboost import XGBClassifier
from scipy.stats import anderson
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix 
from PIL import Image
matplotlib.use("Agg")

"""
import streamlit as st: This imports the Streamlit library, which is used to create interactive web apps.
import itertools: This imports the itertools library, which provides a variety of functions for working with iterators and generators.
import pandas as pd: This imports the Pandas library, which is used for data analysis and manipulation.
import numpy as np: This imports the NumPy library, which is used for scientific computing and numerical analysis.
from scipy.stats import pearsonr: This imports the Pearson correlation coefficient function from the SciPy library.
from scipy import stats: This imports the stats module from the SciPy library, which provides a variety of statistical functions.
import matplotlib.pyplot as plt: This imports the Matplotlib plotting library and assigns it the alias plt.
import plotly.express as px: This imports the Plotly Express plotting library and assigns it the alias px.
import matplotlib: This imports the Matplotlib plotting library.
import seaborn as sns: This imports the Seaborn plotting library, which provides a variety of statistical and visualization functions.
from sklearn.pipeline import Pipeline: This imports the Pipeline class from the Scikit-Learn machine learning library.
from wordcloud import WordCloud: This imports the WordCloud class from the WordCloud library, which is used to create word clouds.
from sklearn.decomposition import PCA: This imports the Principal Component Analysis (PCA) class from the Scikit-Learn machine learning library.
from sklearn.preprocessing import LabelEncoder: This imports the LabelEncoder class from the Scikit-Learn machine learning library, which is used to encode categorical data.
from sklearn import preprocessing: This imports the preprocessing module from the Scikit-Learn machine learning library, which provides a variety of data preprocessing functions.
from scipy.stats import chi2_contingency,chi2: This imports the chi-squared test functions from the SciPy library.
import statsmodels.api as sm: This imports the statsmodels library, which is used for statistical modeling and analysis.
from scipy.stats import spearmanr: This imports the Spearman rank correlation coefficient function from the SciPy library.
from sklearn.experimental import enable_iterative_imputer: This enables the experimental IterativeImputer class from the Scikit-Learn machine learning library.
from sklearn.impute import IterativeImputer: This imports the IterativeImputer class from the Scikit-Learn machine learning library, which is used to impute missing values in data.
from sklearn.pipeline import Pipeline: This imports the Pipeline class from the Scikit-Learn machine learning library.
from sklearn.linear_model import LogisticRegression: This imports the LogisticRegression class from the Scikit-Learn machine learning library, which is used for binary classification.
from sklearn.naive_bayes import GaussianNB: This imports the GaussianNB class from the Scikit-Learn machine learning library, which is used for naive Bayes classification.
from xgboost import XGBClassifier: This imports the XGBClassifier class from the XGBoost library, which is used for gradient boosted tree classification.
from scipy.stats import anderson: This imports the Anderson-Darling test function from the SciPy library.
from sklearn.tree import DecisionTreeClassifier: This imports the DecisionTreeClassifier class from the Scikit-Learn machine learning library, which is used for decision tree classification.
from sklearn.ensemble import RandomForestClassifier: This imports the RandomForestClassifier class from the Scikit-Learn machine learning library, which is used for random forest classification.
from sklearn.metrics import classification_report: This imports the classification_report function from the Scikit-Learn machine learning library, which is used to generate a report of the performance of a classification model.
from sklearn.metrics import confusion_matrix: This imports the confusion_matrix function from the Scikit-Learn machine learning library, which is used to generate a confusion matrix of the predictions made by a classification model.
from PIL import Image: This imports the Image class from the Python Imaging Library (PIL), which is used to work with images.
matplotlib.use("Agg"): This tells Matplotlib to use the Agg backend, which is a non-interactive backend that is suitable for generating images.
I hope this helps!
"""