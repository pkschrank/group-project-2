from sklearn.metrics import classification_report, balanced_accuracy_score

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


def print_classification_report(y_test, prediction, title="Classification Report - Original Data"):
    """
    Print the formatted classification report
    """
    
    print("--------------------------------------------------------")
    print(title)
    print(classification_report(y_test, prediction))
    print("--------------------------------------------------------")

def print_balanced_accuracy_report(y_train, y_test, train_pred, test_pred, title="Balanced Accuracy Scores"):
    """
    Print the formatted balanced accuracy report
    """
    print(title)
    print("--------------------------------------------------------")
    x = balanced_accuracy_score(y_train, train_pred)
    y = balanced_accuracy_score(y_test, test_pred)
    print(x,'training score')
    print(y,'testing score')
    print(round((x-y), 16),'variance')