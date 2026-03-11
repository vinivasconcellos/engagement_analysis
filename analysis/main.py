import pandas as pd
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from limpeza_dados import converter_k, formatar_mes
from calculo_engajamento import calcular_engajamento
from medias import media_por_grupo
from medias_grupo import resumo_max_min_por_grupo
from categorias import categorizar_post
from outliers import detectar_outliers_iqr, sem_outliers_iqr

BASE_DIR = Path(__file__).resolve().parents[1]
arquivo = BASE_DIR / "data" / "Posts_2025.xlsx"
df_postagens2025 = pd.read_excel(arquivo)

# tratamento
colunas = ["Curtidas", "Coment.", "Compart.", "Salvos", "Visualiz.", "Alcance", "Visitas", "Seguid."]
for col in colunas:
    df_postagens2025[col] = df_postagens2025[col].apply(converter_k)
# print(df_postagens2025)

df_postagens2025 = formatar_mes(df_postagens2025)
# print(df_postagens2025.head())
# print(df_postagens2025.info())

# filtragem
colunas = ["Curtidas", "Coment.", "Compart.", "Salvos", "Visualiz.", "Alcance", "Visitas", "Seguid.", "Engajamento"]

#cálculo engajamento:
df_postagens2025 = calcular_engajamento(df_postagens2025)
#print(df_postagens2025)

#médias
df_medias = media_por_grupo(df_postagens2025, colunas)
#print(df_medias.round(2))

#qual formato teve o maior e o menor valor médio de acordo com a métrica
df_resumo = resumo_max_min_por_grupo(df_postagens2025, colunas, grupo="Formato")
#print(df_resumo.round(2))

#categorias

df_postagens2025["Categoria"] = df_postagens2025["Título / Tema do Post"].map(categorizar_post)
#print(df_postagens2025)
df_postagens2025.to_excel("postagens_categorizadas_2025.xlsx", index=False)

#outliers
#Detectar outliers de engajamento
outliers_eng = detectar_outliers_iqr(df_postagens2025, coluna="Engajamento")
print("Outliers de Engajamento:")
print(outliers_eng)

#Top categorias presentes nos outliers
top_categorias_outliers_eng = (outliers_eng["Categoria"].value_counts().reset_index())
top_categorias_outliers_eng.columns = ["Categoria", "Qtd_Outliers"]
print(top_categorias_outliers_eng)
#####################
#métricas sem outliers
# quais formatos tiveram melhor engajamento por categoria retirando os outliers

df_analise_categoria_tema_eng_s = sem_outliers_iqr(df_postagens2025, coluna="Engajamento")
print(df_analise_categoria_tema_eng_s)

# quais formatos tiveram melhor engajamento por categoria com outlier
analise_categoria_tema_eng = df_postagens2025[["Formato", "Categoria", "Engajamento"]].groupby(["Categoria", "Formato"]).mean().round(2).sort_values(by=["Categoria", "Engajamento"], ascending=[True, False])

# quais formatos tiveram melhor engajamento por categoria sem outlier
analise_categoria_tema_eng_s = df_analise_categoria_tema_eng_s[["Formato", "Categoria", "Engajamento"]].groupby(["Categoria", "Formato"]).mean().round(2).sort_values(by=["Categoria", "Engajamento"], ascending=[True, False])

# mostrando os dois resultados para comparação
analise_categoria_tema_eng_s = analise_categoria_tema_eng_s.rename(columns={"Engajamento": "Eng_Without_Outliers"})
analise_categoria_tema_eng = analise_categoria_tema_eng.rename(columns={"Engajamento": "Eng_With_Outliers"})
df_cat_eng_s_c = analise_categoria_tema_eng.merge(analise_categoria_tema_eng_s, on=["Categoria", "Formato"], how="outer")
df_cat_eng_s_c = df_cat_eng_s_c.fillna(0)

print(df_cat_eng_s_c.sort_values(by=["Categoria", "Eng_Without_Outliers"], ascending=[True, False])) #mostrar em imagem

BASE_DIR = Path(__file__).resolve().parents[1]

pasta_imagem="images"
pasta_imagem = BASE_DIR / pasta_imagem
pasta_imagem.mkdir(parents=True, exist_ok=True)

df_imagem = df_cat_eng_s_c.sort_values(by=["Categoria", "Eng_Without_Outliers"], ascending=[True, False]).reset_index()

fig, ax = plt.subplots(figsize=(12, 6))
ax.axis('tight')
ax.axis('off')

tabela = ax.table(
    cellText=df_imagem.round(2).values,
    colLabels=df_imagem.columns,
    loc='center',
    colWidths=[0.29, 0.08, 0.13, 0.13])

tabela.auto_set_font_size(False)
tabela.set_fontsize(10)
tabela.scale(1.2, 1.2)

caminho_imagem = pasta_imagem / "comparison_with_and_without_outliers_categories_posts.png"

plt.savefig(caminho_imagem, bbox_inches="tight", dpi=300)

plt.close()

# Média de engajamento por categoria sem outliers
df_media_eng_cat_s = df_analise_categoria_tema_eng_s[["Categoria", "Engajamento"]].groupby(["Categoria"]).mean()
df_media_eng_cat_s = df_analise_categoria_tema_eng_s[["Categoria", "Engajamento"]].groupby(["Categoria"]).mean().sort_values(by=["Engajamento", "Categoria"], ascending=[False, True])
df_media_eng_cat_s = df_media_eng_cat_s.reset_index()
df_media_eng_cat_s.columns = ["Categoria", "Media_Eng_Without_Outliers"]

# Média de engajamento por categoria com outliers
df_media_eng_cat = df_postagens2025[["Categoria", "Engajamento"]].groupby(["Categoria"]).mean()
df_media_eng_cat = df_postagens2025[["Categoria", "Engajamento"]].groupby(["Categoria"]).mean().sort_values(by=["Engajamento", "Categoria"], ascending=[False, True])
df_media_eng_cat = df_media_eng_cat.reset_index()
df_media_eng_cat.columns = ["Categoria", "Media_Eng_With_Outliers"]

df_tot = df_media_eng_cat.merge(df_media_eng_cat_s, on=["Categoria"], how="outer")
df_tot = df_tot.fillna(0)
df_tot = df_tot.sort_values(by="Media_Eng_Without_Outliers", ascending=False)
print("Ordem decrescente de engajamento sem outliers:")
print(df_tot.round(2))
df_tot = df_tot.sort_values(by="Media_Eng_With_Outliers", ascending=False)
print("Ordem decrescente de engajamento com outliers:")
print(df_tot.round(2))
####################
