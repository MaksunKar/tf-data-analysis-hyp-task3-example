import pandas as pd
import numpy as np

import statsmodels.stats.weightstats

chat_id = 790154026


def solution(x) -> bool:
    alpha = 0.07
    _, pvalue = statsmodels.stats.weightstats.ztest(x, value=500, alternative="smaller")
    return pvalue < alpha
