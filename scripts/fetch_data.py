import requests
import pandas as pd

# 例: e-Gov APIなどから取得（架空URL）
response = requests.get(
    "https://api.e-stat.go.jp/rest/3.0/app/getStatsData?appId=&lang=J&statsDataId=0003348425&metaGetFlg=Y&cntGetFlg=N&explanationGetFlg=Y&annotationGetFlg=Y&sectionHeaderFlg=1&replaceSpChars=0"
)

data = response.json()

# 保存（rawデータ）
df = pd.DataFrame(data)
df.to_csv("data/raw.csv", index=False)
