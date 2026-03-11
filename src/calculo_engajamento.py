#analisar -> filtrar
# Engajamento = Curtidas + Comentários + Compartilhamentos + Salvos

def calcular_engajamento(df_engaj):
    """
    Calcula engajamento como soma de curtidas, comentários,
    compartilhamentos e salvos.
    Retorna o DataFrame com a coluna 'Engajamento'.
    """
    df_engaj = df_engaj.copy()  # evita alterar o original
    df_engaj["Engajamento"] = (df_engaj["Curtidas"] + df_engaj["Coment."] + df_engaj["Compart."] + df_engaj["Salvos"])
    return df_engaj





