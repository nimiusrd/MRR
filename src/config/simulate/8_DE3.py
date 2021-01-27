import numpy as np

config = {
    'eta': 1,  # 結合損
    'alpha': 52.96,  # 伝搬損失係数
    'K': np.array([
        0.8400832770266392,
        0.17319482448332713,
        0.16010136571995537,
        0.3288659798549909,
        0.4482236869176462,
        0.5138058562180989,
        0.11521410467738435,
        0.05052718117665428,
        0.38656852113171847
    ]),  # 結合率
    'L': np.array([
        0.0002548470740762567,
        5.663268312805705e-05,
        0.0002548470740762567,
        0.0002548470740762567,
        0.0002548470740762567,
        0.0002548470740762567,
        5.663268312805705e-05,
        5.663268312805705e-05
    ]),  # リング周長
    'n_eff': 3.3938,  # 実行屈折率
    'n_g': 4.2,  # 群屈折率
    'center_wavelength': 1550e-9,
    # 'lambda': np.arange(1520e-9, 1560e-9, 1e-12)
    # 'lambda': np.arange(1545e-9, 1555e-9, 1e-12)
}
