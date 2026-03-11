import pandas as pd

def resumo_max_min_por_grupo(df_postagens2025, colunas, grupo="Formato"):
    """
    Retorna, para cada métrica, qual grupo (ex: Formato)
    teve o maior e o menor valor médio
    """
    
    medias = (df_postagens2025.groupby(grupo)[colunas].mean().reset_index())

    resultados = []

    for coluna in colunas:
        idx_max = medias[coluna].idxmax()
        idx_min = medias[coluna].idxmin()

        resultados.append({
            "Metrica": coluna,
            "Maior_Grupo": medias.loc[idx_max, grupo],
            "Maior_Valor": medias.loc[idx_max, coluna],
            "Menor_Grupo": medias.loc[idx_min, grupo],
            "Menor_Valor": medias.loc[idx_min, coluna],
        })

    return pd.DataFrame(resultados)

