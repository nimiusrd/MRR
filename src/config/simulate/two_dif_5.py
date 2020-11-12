import numpy as np

config = {
    'eta': 1,  # 結合損
    'alpha': 52.96,  # 伝搬損失係数
    'K': np.array([0.5, 0.5, 0.5]),  # 結合効率
    'L': np.array([0.00041881, 0.00020872]),  # リング周長
    'n_eff': 3.3938,  # 実行屈折率
    'n_g': 4.2,  # 群屈折率
    'lambda': np.arange(1540e-9, 1560e-9, 1e-12)  # 波長レンジ
}
