#qual formato teve o maior e o menor valor médio de acordo com a métrica
import pandas as pd
def detectar_outliers_iqr(df, coluna, fator=1.5):
    Q1 = df[coluna].quantile(0.25) #25% dos dados estão abaixo. Metade da metade inferior
    Q3 = df[coluna].quantile(0.75) #75% dos dados abaixo. Metade da metade superior
    IQR = Q3 - Q1 #Ele representa onde está a maior concentração dos dados, ignorando extremos.

    limite_inferior = Q1 - fator * IQR
    limite_superior = Q3 + fator * IQR
    #mostrando os outliers
    df_outliers = df[(df[coluna] < limite_inferior) | (df[coluna] > limite_superior)]
    
    #limites = {"Q1": Q1, "Q3": Q3, "IQR": IQR, "Limite_Inferior": limite_inferior, "Limite_Superior": limite_superior}
    return df_outliers

def sem_outliers_iqr(df, coluna, fator=1.5):
    Q1 = df[coluna].quantile(0.25) #25% dos dados estão abaixo. Metade da metade inferior
    Q3 = df[coluna].quantile(0.75) #75% dos dados abaixo. Metade da metade superior
    IQR = Q3 - Q1 #Ele representa onde está a maior concentração dos dados, ignorando extremos.

    limite_inferior = Q1 - fator * IQR
    limite_superior = Q3 + fator * IQR    
    #mostrando sem outliers
    df_limpo = df[(df[coluna] >= limite_inferior) & (df[coluna] <= limite_superior)]

    #limites = {"Q1": Q1, "Q3": Q3, "IQR": IQR, "Limite_Inferior": limite_inferior, "Limite_Superior": limite_superior}
    return df_limpo