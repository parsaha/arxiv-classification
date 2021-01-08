# arxiv-classification
## Introduction
The arXiv houses academic papers in a range of subjects, including math and physics. The goal of this project is to use Natural Language Processing (NLP) to determine how well the title and/or abstract of an academic paper from the arXiv acts as an indicator for which academic subject the paper addresses.  
## Source
The dataset used for this project came from [this Kaggle dataset](https://www.kaggle.com/Cornell-University/arxiv) of metadata for 1.7M+ papers on the arxiv. 
## Methods 
### Cleaning the Data
There were a few things to consider initially before even attempting to categorize any of the papers:
* For convinience, we extract the tags that correspond to the academic subjects the paper falls under, the title of the paper, and the abstract, as these are the components we need. 
* Many scientific papers like those on the arXiv have mathematical typesetting within their titles and/or abstracts. This means <img src="https://latex.codecogs.com/svg.latex?\pi" title="\pi" /> in a paper would show up in the data as `$\\\\pi$`. 






## References
* https://www.kaggle.com/Cornell-University/arxiv
* https://github.com/jupyter/help/issues/201
* https://arxiv.org/category_taxonomy
* https://towardsdatascience.com/multi-class-text-classification-with-sklearn-and-nltk-in-python-a-software-engineering-use-case-779d4a28ba5
* https://www.blopig.com/blog/2017/07/using-random-forests-in-python-with-scikit-learn/
* https://stackabuse.com/text-classification-with-python-and-scikit-learn/
