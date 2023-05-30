import datetime
import uuid
import os
import numpy as np

def unique_filename(type='uuid'):
    if type == 'datetime':
        filename = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
    else: # type = 'uuid'
        filename = str(uuid.uuid4())
    return filename

def makenewfold(prefix='output_', type='datetime'):
    suffix = unique_filename(type)
    foldname = prefix + suffix
    os.makedirs(foldname)
    return foldname

def save_history_history(fname, history_history, fold=''):
    np.save(os.path.join(fold, fname), history_history)