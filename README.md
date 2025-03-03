## Datacamp Challenge: Learning from Positive and Unlabeled Data in NLP

Participants must build a Positive-Unlabeled (PU) learning model that can identify positive and negative social media comments. The challenge is to train the model without explicit negative labels, using only positive labels, unlabeled data, and artificially labeled samples. The goal is to classify comments as accurately as possible despite the missing negative labels in training.

### Dataset Building
To build this dataset we proceed as follows:
1. Data Collection: We gather 15,000 comments from YouTube videos and Bluesky posts sourced from well-known media platforms like The New York Times, The economist, ...
1. Data Labelling with LLM: With the 15,000 comments from each API sources 20% are artificially labeled, 80% remain unlabeled, using Llama 3.2 (2 GB).
1.  We merge this data with an existing Twitter sentiment analysis dataset to enrich diversity(https://github.com/cardiffnlp/tweeteval/tree/main/datasets/sentiment), changing negative and neutral labels and set as unlabeled

### Train Dataset
Contains unlabbelled data and few positive instances.

### Test Dataset (Evaluation)
Contains both positive and negative labels for evaluation. The model must classify negative samples correctly despite training only on positive, unlabeled, and artificially labeled data.

### Evaluation Metric 
F1-score

## Project Structure