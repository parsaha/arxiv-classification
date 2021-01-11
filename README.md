# arxiv-classification
## Introduction
The arXiv houses academic papers in a range of subjects, including math and physics. The goal of this project is to use Natural Language Processing (NLP) to determine how well the title and/or abstract of an academic paper from the arXiv acts as an indicator for which academic subject the paper addresses.  

Part of the interest of this project is in the idea of taking sources that are jargon-heavy with high variety and seeing how well traditional NLP classification holds up. Investigating the effectiveness of different methods against data of this variety could prove useful in applications outside of academic papers and recommendation systems. 
## Source
The dataset used for this project came from [this Kaggle dataset](https://www.kaggle.com/Cornell-University/arxiv) of metadata for 1.7M+ papers on the arxiv. The version that this project is based upon was downloaded on 1/1/2021. 
## Methods 
### Cleaning the Data
There were a few things to consider initially before even attempting to categorize any of the papers:
* For convinience, we extract the tags that correspond to the academic subjects the paper falls under, the title of the paper, and the abstract, as these are the components we need. 
* Many scientific papers like those on the arXiv have mathematical typesetting within their titles and/or abstracts. This means <img src="https://latex.codecogs.com/svg.latex?\pi" title="\pi" /> in a paper would show up in the data as `$\\\\pi$`. 
* Since there are papers with more than one tag in different subjects, the models are tested based on whether they can accurately predict the most common one (i.e. the subject that the majority of tags belong to). One issue that comes up here is the fact that plenty of papers have more than one subject have the highest occurance among the tags (e.g. a paper with two tags in physics and two tags in mathematics); in each model, it is explicitly mentioned whether the model chooses to address this situation by having the "correct" subject be chosen at random among the most popular tags, or to simply clean the data so that such papers are not even part of the data used. 


## Notes
* Currently, the `category` part of the extracted data that is used to determine the accuracy of the classifications is randomly chosen between the categories of the most common tags for each paper. 
* The `arxiv-metadata-oai-snapshot.json` dataset has been placed one directory higher than the rest of the project.


## TODO
* Move data cleaning functions to python files and then import into notebook demonstrating data cleaning 
* make notebook for cleaning and EDA 




## References
* https://www.kaggle.com/Cornell-University/arxiv
* https://github.com/jupyter/help/issues/201
* https://arxiv.org/category_taxonomy
* https://towardsdatascience.com/multi-class-text-classification-with-sklearn-and-nltk-in-python-a-software-engineering-use-case-779d4a28ba5
* https://www.blopig.com/blog/2017/07/using-random-forests-in-python-with-scikit-learn/
* https://stackabuse.com/text-classification-with-python-and-scikit-learn/
