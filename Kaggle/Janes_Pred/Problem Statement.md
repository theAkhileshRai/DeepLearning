# Data Description
This dataset contains an anonymized set of features, feature_{0...129}, representing real stock market data.
Each row in the dataset represents a trading opportunity, for which you will be predicting an action value: 1 to make the trade and 0 to pass on it.
Each trade has an associated weight and resp, which together represents a return on the trade.
The date column is an integer which represents the day of the trade, while ts_id represents a time ordering.
In addition to anonymized feature values, you are provided with metadata about the features in features.csv.

In the training set, train.csv, you are provided a resp value, as well as several other resp_{1,2,3,4} values that represent returns over different time horizons.
These variables are not included in the test set. 
Trades with weight = 0 were intentionally included in the dataset for completeness, although such trades will not contribute towards the scoring evaluation.

