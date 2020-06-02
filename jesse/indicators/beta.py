from typing import Union

import numpy as np
import talib


def beta(candles: np.ndarray, period=5, sequential=False) -> Union[float, np.ndarray]:
    """
    BETA - Beta

    :param candles: np.ndarray
    :param sequential: bool - default=False

    :return: float | np.ndarray
    """
    if not sequential and len(candles) > 240:
        candles = candles[-240:]

    res = talib.BETA(candles[:, 3], candles[:, 4], timeperiod=period)

    if sequential:
        return res
    else:
        return None if np.isnan(res[-1]) else res[-1]