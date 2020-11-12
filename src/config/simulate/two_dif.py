import numpy as np

config = {
    'eta': 1,  # 結合損
    'alpha': 52.96,  # 伝搬損失係数
    'K': np.array([0.65, 0.17, 0.43]),  # 結合効率
    'L': np.array([0.00016031, 0.0002553]),  # リング周長
    'n_eff': 3.3938,  # 実行屈折率
    'n_g': 4.2,  # 群屈折率
    'lambda': np.arange(1400e-9, 1700e-9, 1e-12)  # 波長レンジ
}
