import numpy as np

config = {
    'eta': 1,  # 結合損
    'alpha': 52.96,  # 伝搬損失係数
    'K': np.array([0.27282724535989045, 0.04693990781883589, 0.010208462553120745, 0.043015763400347906, 0.5575367660570303]),  # 結合率
    'L': np.array([1.69898049e-04, 5.66326831e-05, 5.66326831e-05, 1.69898049e-04]),  # リング周長
    'n_eff': 3.3938,  # 実行屈折率
    'n_g': 4.2,  # 群屈折率
    'center_wavelength': 1550e-9,
    # 'lambda': np.arange(1535e-9, 1565e-9, 1e-12)
}
