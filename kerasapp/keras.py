import matplotlib.pyplot as plt

def plot_loss(history, title=None):
    """_summary_

    Args:
        history (_type_): model history
        title (_type_, optional): title. Defaults to None.
    """
    if not isinstance(history, dict):
        history = history.history
    plt.plot(history['loss'])
    plt.plot(history['val_loss'])
    
    if title is not None:
        plt.title(title)
    
    plt.xlabel('Epoch')
    plt.ylabel('loss')
    plt.legend(['Training', 'Validation'], loc=0)
    
def plot_acc(history, title=None):
    """_summary_

    Args:
        history (_type_): model history
        title (_type_, optional): title. Defaults to None.
    """
    if not isinstance(history, dict):
        history = history.history
    plt.plot(history['accuracy'])
    plt.plot(history['val_accuracy'])
    
    if title is not None:
        plt.title(title)
    
    plt.xlabel('Epoch')
    plt.ylabel('acc')
    plt.legend(['Training', 'Validation'], loc=0)