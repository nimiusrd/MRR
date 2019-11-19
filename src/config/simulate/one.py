import numpy as np

config = {
    'eta': 1,  # 結合損
    'alpha': 0,  # 伝搬損失係数
    'K': np.array([0.65, 0.3]),  # 結合効率
    'L': np.array([0.0003658288643997878]),  # リング周長
    'n': 3.3938,  # 屈折率
    'lambda': np.arange(1545e-9, 1555e-9, 1e-12)  # 波長レンジ
}
