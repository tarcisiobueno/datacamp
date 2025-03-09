# Ramp Datacamp Challenge: Learning from Positive and Unlabeled Data in NLP

**Authors:** Team 12
- Cristian Alejandro CHÁVEZ BECERRA
- Giovanni BENEDETTI DA ROSA
- Lucas PALMIRO DE FREITAS
- Tarcisio DA SILVA BUENO
- Yann Fabio NTSAMA TABETSING

## Introduction

This challenge focuses on tackling a critical problem in machine learning: training classifiers with limited labeled data. In real-world scenarios, obtaining high-quality negative labels is often challenging, making Positive-Unlabeled (PU) learning a crucial technique for various applications, including sentiment analysis, medical diagnosis, and fraud detection.

### Where does the data come from?
The dataset used in this challenge is constructed by aggregating and processing text data from multiple sources:
- **Social Media Comments**: 15,000 comments are collected from YouTube videos and Bluesky posts, sourced from reputable media outlets like *The New York Times* and *The Economist*.
- **Large Language Model (LLM) Labeling**: From the collected data, 20% of the samples are artificially labeled using Llama 3.2 (2 GB), while the remaining 80% remain unlabeled.
- **Existing Sentiment Analysis Dataset**: To increase dataset diversity, we incorporate data from the [TweetEval sentiment dataset](https://github.com/cardiffnlp/tweeteval/tree/main/datasets/sentiment). The original negative and neutral labels are reclassified as unlabeled to align with the PU learning framework.

**Train Dataset:** Contains mostly unlabbelled data, positive instances, and a few negative samples.

**Test Dataset (Evaluation):** Contains both positive and negative labels for evaluation. 

**Evaluation Metric:** F1-score

### What is the task this challenge aims to solve?
Participants must develop machine learning models capable of distinguishing between positive and negative comments using positive, unlabeled data, and very feel quality negative samples. The challenge encourages competitors to leverage innovative artificial labeling strategies, semi-supervised learning, and PU learning techniques to build robust classifiers.

### Why does it matter?
Traditional supervised learning methods rely on well-annotated datasets, which are often expensive and time-consuming to create. However, in many real-world scenarios—such as content moderation, medical diagnosis, and financial fraud detection—negative examples are either rare or difficult to label. This challenge reflects these real-world constraints and encourages the development of models that can generalize effectively with minimal supervision. 

The nature of the data used in this challenge is particularly relevant because social media platforms generate vast amounts of user-generated content with highly imbalanced sentiment distributions. Negative sentiment can be more nuanced and context-dependent, making it harder to label explicitly. Furthermore, misinformation, toxicity detection, and brand reputation management require techniques capable of handling limited labeled data while still maintaining high classification performance. By working with diverse sources and simulating realistic labeling constraints, this challenge offers a valuable opportunity to advance research in PU learning and apply it to practical NLP problems where manually annotating large datasets is infeasible.

## Getting started

### Install

To run a submission and the notebook you will need the dependencies listed
in `requirements.txt`. You can install the dependencies with the
following command-line:

```bash
pip install -U -r requirements.txt
```

If you are using `conda`, we provide an `environment.yml` file for similar
usage.

### Challenge description

Get started with the [dedicated notebook](challenge/sentiment_prediction_starting_kit.ipynb)

### Test a submission

The submissions need to be located in the `challenge/submissions` folder. For instance
for `my_submission`, it should be located in `challenge/submissions/my_submission`.

To run a specific submission, you can use the `ramp-test` command line inside the `challenge` folder:

```bash
ramp-test --submission my_submission
```
In case of a very long ramp-test, you can select a subset of the data to run it with
the '--quick-test' option (if available in problem.py)
```bash
ramp-test --submission my_submission --quick-test
```

You can get more information regarding this command line:

```bash
ramp-test --help
```

### To go further

You can find more information regarding `ramp-workflow` in the
[dedicated documentation](https://paris-saclay-cds.github.io/ramp-docs/ramp-workflow/stable/using_kits.html)
