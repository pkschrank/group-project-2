# Group-Project-2

### Contributors: Philip Schrank, Tony Montgomery, & Rob Pavlik

This application analyzes the SP-500 index, creates a buy signal target variable, and predicts the success of the buy signal based on the next day positive return. Our goal is to meet or exceed a 75% balanced accuracy score.

1) Create an install package list.
2) Read and load SP-500 index data into a dataframe from YahooFinance (yf) ticker function with max data period.
3) Clean data set by dropping unnecessary columns and null values.
4) Perform Feature Engineering:
   - Moving Averages
   - RSI
   - MACD
   - Bollinger Bands
5) Perform Winsorization of data using SciKit Learn's winsorize function with upper and lower settings of .05.
6) Perform Train and Test Splits using SciKit Learn's TimeSeriesSplit function with a setting of 5 folds.
7) Perform Scaling using SciKit Learn's StandardScaler.
8) Perform data sampling using IMBlearn's RandomOverSampling and RandomUnderSampling functions.
8) Perform and display results from various Classifications.

## Technical  Indicators
The application utilizes the following technical momentum indicators to enable machine learning and to generate a buy signal:
1. Simple Moving Averages of 10, 20, 30, 50, 100, and 200 days. Moving averages are used to identify trends.
2. Moving Average Convergence Divergence (MACD) shows the relationship between the two exponential moving averages (EMA) of 26-day EMA and 12-day EMA. The signal line is 9 EMA.
3. Relative Strength Indicator which oscillates between zero and 100. Readings above 50 indicate positive and uptrend momentum while readings below 50 show negative and downtrend momentum. Readings above 70 indicate overbought conditions and readings below 30 indicate oversold conditions.
4. Bollinger Bands, developed by John Bollinger, gauge volatility to determine if an asset is over or undervalued. The center line is the 20-day SMA while the upper and lower bands are two standard deviations above and below the mid line. The lines contract when volatility is low and expand when volatility is high.

## Buy Signal Conditions
The goal is to buy low and sell high. This application generates a buy signal target variable of 1 when all of the following are true:
1. The Relative Strength Indicator (RSI) is less than 50.
2. The MACD is less than zero.
3. The last closing price is less than the Bollinger mid line.
4. For training, the the next day's percent return must be greater than zero.
When these conditions are false, the target variable is 0.