import numpy as np

config = {
    'eta': 1,  # 結合損
    'a': np.array([1, 1]),  # 減衰定数
    'K': np.array([0.65, 0.17, 0.43]),  # 結合効率
    'L': np.array([2e-4, 2e-4]),  # リング周長
    'n': 3.3938,  # 屈折率
    'lambda': np.arange(1545e-9, 1555e-9, 1e-12)  # 波長レンジ
}
