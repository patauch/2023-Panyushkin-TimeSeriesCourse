import numpy as np


def ED_distance(ts1, ts2):
    """
    Calculate the Euclidean distance.

    Parameters
    ----------
    ts1 : numpy.ndarray
        The first time series.

    ts2 : numpy.ndarray
        The second time series.

    Returns
    -------
    ed_dist : float
        Euclidean distance between ts1 and ts2.
    """
    
    ed_dist = 0
    
    ed_dist  = np.sqrt(np.sum([(a-b)**2 for a,b in zip(ts1, ts2)]))
    # INSERT YOUR CODE
    
    return ed_dist


def norm_ED_distance(ts1, ts2):
    """
    Calculate the normalized Euclidean distance.

    Parameters
    ----------
    ts1 : numpy.ndarray
        The first time series.

    ts2 : numpy.ndarray
        The second time series.

    Returns
    -------
    norm_ed_dist : float
        The normalized Euclidean distance between ts1 and ts2.
    """

    norm_ed_dist = 0

    if len(ts1) != len(ts2):
        raise ValueError("The two arrays must have the same length.")

    m = len(ts1)

    norm_ed_dist = np.sqrt(abs(2*m * (1 - (np.dot(ts1, ts2) - m * (sum(ts1)/m) * (sum(ts2)/m)) / (
        m * np.sqrt(sum(ts1**2 - (sum(ts1)/m)**2) / m) * np.sqrt(sum(ts2**2 - (sum(ts2)/m)**2) / m)))))

    return norm_ed_dist



def DTW_distance(ts1, ts2, r=None):
    """
    Calculate DTW distance.

    Parameters
    ----------
    ts1 : numpy.ndarray
        The first time series.

    ts2 : numpy.ndarray
        The second time series.

    r : float
        Warping window size.
    
    Returns
    -------
    dtw_dist : float
        DTW distance between ts1 and ts2.
    """

    dtw_dist = 0
    
    D = np.full([len(ts1)+1, len(ts2)+1], np.inf)
    D[0,0] = 0
    for i in range(1, len(ts1)+1):
        for j in range(1, len(ts2)+1):
          cost = (ts1[i-1]-ts2[j-1])**2
          D[i, j] = cost + min(D[i-1, j], D[i, j-1], D[i-1, j-1])

    return D[-1, -1]