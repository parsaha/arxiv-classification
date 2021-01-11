import json
import numpy as np
import pandas as pd
import statistics as stats
import re
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# Was downloaded on 1/1/2021 from: https://www.kaggle.com/Cornell-University/arxiv
# I happened to place the original database one directory higher
file_path = '../arxiv-metadata-oai-snapshot.json'

# TAGS
# Takes article metadata as a string and returns the arXiv shorthand for categories seperated by a space
def clean_cats(data):
    spl = data.split('"categories":')[1].split(',"license"')[0]
    return spl[1:-1]

# TITLE
# Takes article metadata as a string and returns the title (without quotation marks)
def clean_title(data):
    spl = data.split('"title":')[1].split(',"comments":')[0]
    return spl[1:-1].replace('\\n', '')

# ABSTRACT
# Takes article metadata as a string and returns abstract (without quotation marks)
def clean_ab(data):
    spl = data.split('"abstract":')[1].split(',"versions":')[0]
    return spl[3:-1].replace('\\n', '')

# CATEGORY
# Takes categories as a string (i.e. as the result of clean_cats) and returns the general category they fall under (by majority)
# Note: currently, a paper with equal tags in more than one subject is "randomly" chosen to be categorized by one of them
# https://arxiv.org/category_taxonomy
def gen_cat(cats):
    math = q_bio = cs = q_fin = stat = eess = econ = physics = 0
    gen_cat_list = ['math', 'q-bio', 'cs', 'q-fin', 'stat', 'eess', 'econ']
    physics_list = ['astro-ph', 'cond-mat', 'gr-qc', 'hep-ex', 'hep-lat', 'hep-ph', 'hep-th', 'math-ph', 'nlin', 'nucl-ex',
                   'nucl-th', 'physics', 'quant-ph']
    cat_list = cats.split(' ')
    for cat in cat_list:
        if cat.split('.')[0] == 'math':
            math+=1
        elif cat.split('.')[0] == 'q-bio':
            q_bio+=1
        elif cat.split('.')[0] == 'cs':
            cs+=1
        elif cat.split('.')[0] == 'q-fin':
            q_fin+=1
        elif cat.split('.')[0] == 'stat':
            stat+=1
        elif cat.split('.')[0] == 'eess':
            eess+=1
        elif cat.split('.')[0] == 'econ':
            econ+=1
        elif cat.split('.')[0] in physics_list:
            physics+=1
    l = [math, q_bio, cs, q_fin, stat, eess, econ, physics]
    gen_cat_list.append('physics')
    return gen_cat_list[l.index(max(l))]

# How large we want our extracted dataset to be
# In this case, 5000
THRESHOLD = int(5e3)

cat, title, ab = [], [], []

# This runs through the first N papers (where N is our threshold) and cleans them
with open(file_path) as f:
    for i in range(THRESHOLD):
        t = f.readline()
        title.append(clean_title(t))
        ab.append(clean_ab(t))
        cat.append(gen_cat(clean_cats(t)))

# We collect the cleaned components of the paper and create a dataframe from them
df = pd.DataFrame([title, ab, cat])
df = df.transpose()
df.columns = ['Title', 'Abstract', 'Category']

# Below I've commented out the line that created `arxiv_papers.csv`
# df.to_csv('arxiv_papers')

# Now we use stopwords to stem the contents of the titles and abstracts of each paper
stemmer = PorterStemmer()
words = stopwords.words("english")
df['Cleaned Title'] = df['Title'].apply(lambda x: " ".join([stemmer.stem(i) for i in re.sub("[^a-zA-Z0-9]", " ", x).split() if i not in words]).lower())
df['Cleaned Abstract'] = df['Abstract'].apply(lambda x: " ".join([stemmer.stem(i) for i in re.sub("[^a-zA-Z0-9]", " ", x).split() if i not in words]).lower())

# Below I've commented out the line that created `cleaned_papers.csv`
# df.to_csv('cleaned_papers')
