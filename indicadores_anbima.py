import pandas as pd
from datetime import datetime

url = "https://www.anbima.com.br/informacoes/indicadores/"
df = pd.read_html(url, thousands=".", decimal=",")[2]

data_coleta = df.head(1).iloc[0][0]
data_coleta = data_coleta.split("Data e Hora da Última Atualização: ")
data_coleta = data_coleta[1].split(" - ")[0]
data_coleta = datetime.strptime(data_coleta, "%d/%m/%Y")

df["data_coleta"] = data_coleta

df = df.dropna()
df = df.loc[1:]
df["descricao"] = df[1].copy()
df[1] = pd.to_datetime(df[1], format="%d/%m/%Y", errors="coerce")
df[1] = df[1].fillna(df["data_coleta"])
df[0] = df[0].str[:-1]

df = df.rename(columns={0: "indice", 1: "data_referencia", 2: "valor"})
