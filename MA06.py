import matplotlib.pyplot as plt
from load_data import load_data
from pathlib import Path

PLOTS_DIR = Path(r"E:\hai starter data\plots")
PLOTS_DIR.mkdir(parents=True, exist_ok=True)
# 如果你之前就是这样 import 的，保持不变
import eda_utils


# =========================
# 1. 读取两个数据集
# =========================
df_normal = load_data(r"E:\hai starter data\normal_20191101T200000_to_20191104T150000.csv")
df_attack = load_data(r"E:\hai starter data\abnormal_20191029T110000_to_20191101T200000.csv")
# =========================
# normal 的基线窗口
normal_start = "2019-11-01 20:40:00+09:00"
normal_end   = "2019-11-01 21:00:00+09:00"

# attack 的 SA08 窗口
attack_start = "2019-11-01 09:20:00+09:00"
attack_end   = "2019-11-01 09:40:00+09:00"

df_n = df_normal.loc[normal_start:normal_end]
df_a = df_attack.loc[attack_start:attack_end]


def plot_MA06_time_series(out_dir):

    # ---- P1-LC (SA08) ----
    fig1 = eda_utils.plot_time_series(
        df_n,
        sp_col="P1.B3004",
        pv_col="P1.LIT01",
        cv_col="P1.LCV01D",
        title="MA06 – P1-LC (SP–PV)"
    )
    fig1.savefig(out_dir / "MA06_SA08_normal_timeseries.png")

    # ---- P3-LC (SA14) ----
    fig2 = eda_utils.plot_time_series(
        df_n,
        sp_col=None,
        pv_col="P3.LT01",
        cv_col="P3.LCP01D",
        title="MA06 – P3-LC (SP–CV)"
    )
    fig2.savefig(out_dir / "MA06_SA14_normal_timeseries.png")

    # ---- P1-LC (SA08) ----
    fig3 = eda_utils.plot_time_series(
        df_a,
        sp_col="P1.B3004",
        pv_col="P1.LIT01",
        cv_col="P1.LCV01D",
        title="MA06 – P1-LC (SP–PV)"
    )
    fig3.savefig(out_dir / "MA06_SA08_attack_timeseries.png")

    # ---- P3-LC (SA14) ----
    fig4 = eda_utils.plot_time_series(
        df_a,
        sp_col=None,
        pv_col="P3.LT01",
        cv_col="P3.LCP01D",
        title="MA06 – P3-LC (SP–CV)"
    )
    fig4.savefig(out_dir / "MA06_SA14_attack_timeseries.png")

# =========================
# 2. 调用函数（关键）
# =========================
plot_MA06_time_series(PLOTS_DIR)