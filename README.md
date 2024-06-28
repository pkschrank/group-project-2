# Group-Project-2
### Contributors: Philip Schrank, Tony Montgomery, & Rob Pavlik

This is our attempt at creating some code that looks at the NYSE and ranks each sector based on it's performance over a set amount of time, then displays the top 3 performing stocks within that sector. We also attempt to have the code predict the performance for the next transaction.

1) Create a list of Sectors and upload the data for each as its own csv file
2) Create a dictionary to store all the sector data
3) Loop thru and load each sectors data into the dictionary
4) Create a Function to read and preprocess data
    Calculate n-Day percent return feature
    Calculate 3-day rolling average on n-Day return feature
    Calculate polynominal features across averages
    Calculate ratio features across averages
    Drop NaNs
5) Run Preprocess Function on each stock and store in a dictionary
6) Confirm shapes
7) Concatinate all df's into one
8) Display Columns
9) Loop through stocks to drop unnecessary columns
10) Display df
