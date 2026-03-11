def media_por_grupo(df_postagens2025, colunas, grupo="Formato"):
    """
    Calcula média das colunas informadas agrupadas por um campo
    """
    return (df_postagens2025.groupby(grupo)[colunas].mean().reset_index())




