import matplotlib.pyplot as plt
from load_data import load_data
from pathlib import Path

PLOTS_DIR = Path(r"E:\hai starter data\plots")
PLOTS_DIR.mkdir(parents=True, exist_ok=True)
# 如果你之前就是这样 import 的，保持不变
from eda_utils import (
    plotPerColumnDistribution,
    plotScatterMatrix, plot_SA08_time_series
)

# =========================
# 1. 读取两个数据集
# =========================
df_normal = load_data(r"E:\hai starter data\normal_20191101T200000_to_20191104T150000.csv")
df_attack = load_data(r"E:\hai starter data\abnormal_20191029T110000_to_20191101T200000.csv")

# =========================
# 2. 固定分析变量（P1-LC）
# =========================
cols_p1 = [
    "P1.B3004",   # SP
    "P1.LIT01",   # PV
    "P1.LCV01D"   # CV
]

# =========================
# normal 的基线窗口
normal_start = "2019-11-01 20:00:00+09:00"
normal_end   = "2019-11-01 21:00:00+09:00"

# attack 的 SA08 窗口
attack_start = "2019-10-29 13:40:00+09:00"
attack_end   = "2019-10-29 14:40:00+09:00"

df_n = df_normal.loc[normal_start:normal_end, cols_p1]
df_a = df_attack.loc[attack_start:attack_end, cols_p1]

# Normal
fig = plotPerColumnDistribution(df_n, 3, 3)
fig.savefig(PLOTS_DIR / "SA08_normal_distribution.png")
plt.close(fig)

fig = plotScatterMatrix(df_n, 15, 10)
fig.savefig(PLOTS_DIR / "SA08_normal_ScatterMatrix.png")
plt.close(fig)

plot_SA08_time_series(
    df=df_n,
    sp_col='P1.B3004',
    pv_col='P1.LIT01',
    cv_col='P1.LCV01D',
    out_path=PLOTS_DIR / 'SA08_normal_timeseries.png'
)

# Attack
fig = plotPerColumnDistribution(df_a, 3, 3)
fig.savefig(PLOTS_DIR / "SA08_attack_distribution.png")
plt.close(fig)

fig = plotScatterMatrix(df_a, 15, 10)
fig.savefig(PLOTS_DIR / "SA08_attack_ScatterMatrix.png")
plt.close(fig)

plot_SA08_time_series(
    df=df_a,
    sp_col='P1.B3004',
    pv_col='P1.LIT01',
    cv_col='P1.LCV01D',
    out_path=PLOTS_DIR / 'SA08_attack_timeseries.png'
)