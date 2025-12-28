from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
plt.rcParams.update({'font.size': 12})
from mpl_toolkits.mplot3d import Axes3D
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import math
import os


for dirname, _, filenames in os.walk(r'E:\hai starter data'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Distribution graphs (histogram/bar graph) of column data
def plotPerColumnDistribution(df, nGraphShown, nGraphPerRow):

    nunique = df.nunique()
    df = df[[col for col in df if nunique[col] > 1]]

    nRow, nCol = df.shape
    nGraphRow = math.ceil((nCol + nGraphPerRow - 1) / nGraphPerRow)

    fig = plt.figure(figsize=(6 * nGraphPerRow, 8 * nGraphRow), dpi=100)

    for i in range(min(nCol, nGraphShown)):
        ax = plt.subplot(nGraphRow, nGraphPerRow, i + 1)  # ← 必须在 for 里
        columnDf = df.iloc[:, i]

        if not np.issubdtype(columnDf.dtype, np.number):
            columnDf.value_counts().plot.bar(ax=ax)
        else:
            columnDf.hist(ax=ax)

        ax.set_title(str(df.columns[i]))  # 每个子图的变量名

    plt.tight_layout()
    return fig


# Correlation matrix
def plotCorrelationMatrix(df, graphWidth):
    filename = getattr(df, 'dataframeName', 'DataFrame')
    df = df.dropna(axis=1) # drop columns with NaN
    df = df[[col for col in df if df[col].nunique() > 1]] # keep columns where there are more than 1 unique values
    if df.shape[1] < 2:
        print(f'No correlation plots shown: The number of non-NaN or constant columns ({df.shape[1]}) is less than 2')
        return
    corr = df.corr()
    fig = plt.figure(num=None, figsize=(graphWidth, graphWidth), dpi=80)
    corrMat = plt.matshow(corr, fignum = 1)
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.gca().xaxis.tick_bottom()
    plt.colorbar(corrMat)
    plt.title(f'Correlation Matrix for {filename}', fontsize=15)
    plt.tight_layout()
    return fig

# Scatter and density plots
def plotScatterMatrix(df, plotSize, textSize):
    df = df.dropna(axis=1)
    df = df[[col for col in df if df[col].nunique() > 1]]

    ax = pd.plotting.scatter_matrix(
        df,
        figsize=(plotSize, plotSize),
        diagonal='kde'
    )

    for i in range(len(ax)):
        for j in range(len(ax)):
            ax[i, j].xaxis.label.set_size(textSize)
            ax[i, j].yaxis.label.set_size(textSize)

    fig = plt.gcf()  # 关键：获取当前 figure
    fig.suptitle(
        "Scatter Matrix (P1-LC: SP / PV / CV)",
        fontsize=16,
        y=0.98
    )
    plt.tight_layout()
    return fig

def plot_SA08_time_series(df, sp_col, pv_col, cv_col, out_path, time_col=None):
    """
    SA08 专用时间序列可视化
    SP / PV 使用左轴，CV 使用右轴
    """

    fig, ax1 = plt.subplots(figsize=(16, 6))

    # x 轴：时间 or index
    if time_col is not None:
        x = df[time_col]
        ax1.set_xlabel('Time')
    else:
        x = df.index
        ax1.set_xlabel('Sample Index')

    # SP & PV（过程量）
    ax1.plot(x, df[sp_col], label='SP (Setpoint)', linewidth=1.5)
    ax1.plot(x, df[pv_col], label='PV (Process Variable)', linewidth=1.5)
    ax1.set_ylabel('SP / PV')
    ax1.legend(loc='upper left')
    ax1.grid(True)

    # CV（控制量）——第二纵轴
    ax2 = ax1.twinx()
    ax2.plot(x, df[cv_col], label='CV (Control Variable)', linestyle='--', alpha=0.7)
    ax2.set_ylabel('CV')
    ax2.legend(loc='upper right')

    # 标题
    fig.suptitle(
        'SA08 – P1-LC Time Series (SP / PV / CV)',
        fontsize=16,
        y=0.98
    )

    # 关键：layout + 保存
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(out_path, dpi=150)
    plt.close(fig)

    return fig

def plot_time_series(
    df,
    sp_col=None,
    pv_col=None,
    cv_col=None,
    title=""
):
    fig, ax1 = plt.subplots(figsize=(16, 6))

    if sp_col is not None:
        ax1.plot(df[sp_col], label=f"SP ({sp_col})", linestyle="--")

    if pv_col is not None:
        ax1.plot(df[pv_col], label=f"PV ({pv_col})")

    ax1.set_ylabel("SP / PV")
    ax1.legend(loc="upper left")
    ax1.grid(True)

    if cv_col is not None:
        ax2 = ax1.twinx()
        ax2.step(
            df.index,
            df[cv_col],
            where="post",
            label=f"CV ({cv_col})",
            alpha=0.7
        )
        ax2.set_ylabel("CV")
        ax2.legend(loc="upper right")

    fig.suptitle(title, fontsize=15)
    plt.tight_layout()
    return fig