from sklearn.metrics import classification_report

def rsi(data, window=14):
    """
    Create the Relative Strength Index
    
    Args:
        data (DataFrame): The DataFrame to calculate against
        window (int): The number of days to use in the calculation

    Returns:
        The index as a float.
    """
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))


def print_classification_report(y_test, prediction, title=""):
    """
    Print classification reports
    """
    print("--------------------------------------------------------")
    print(f"Classification Report - Original Data")
    print(classification_report(y_test, prediction))
    print("--------------------------------------------------------")