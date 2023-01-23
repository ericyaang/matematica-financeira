import pandas as pd


def br_holidays():
    """ Acessa a planilha de feriados nacionais pela ANBIMA


    Returns:
        dataframe: lista de feriados até 2071
    """

    df = pd.read_excel(
        r"https://www.anbima.com.br/feriados/arqs/feriados_nacionais.xls"
    )
    holidays = list(df["Data"][0 : len(df) - 10])
    holidays = [holidays[i].date() for i in range(len(holidays))]
    return holidays


feriados = br_holidays()
