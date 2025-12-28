import pandas as pd

def load_data(csv_path):
    # 关键修复点：sep=';'
    df = pd.read_csv(
        csv_path,
        sep=';',
        encoding='utf-8-sig'
    )

    # 清理列名（BOM / 空格）
    df.rename(columns=lambda c: c.strip(), inplace=True)

    # HAI 数据集：第一列就是时间
    time_col = df.columns[0]

    # 明确指定时间格式（避免 warning & 慢解析）
    df[time_col] = pd.to_datetime(
        df[time_col],
        format="%Y-%m-%d %H:%M:%S%z",
        errors="raise"
    )

    df.set_index(time_col, inplace=True)

    return df