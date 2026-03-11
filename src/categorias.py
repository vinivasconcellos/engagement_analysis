def categorizar_post(titulo):
    titulo = titulo.lower()
    if "gestação" in titulo or "gestante" in titulo or "saúde" in titulo or "gravidez" in titulo or "feto" in titulo  or "chá" in titulo  or "chás" in titulo or "placenta" in titulo or "pré-natal" in titulo or "maturação" in titulo or "ganho" in titulo or "desenvolvimento" in titulo or "desenv." in titulo:
        return "Gestação / Pré-natal"
    elif "amamentar" in titulo or "amamentação" in titulo or "leite" in titulo or "fórmula" in titulo:
        return "Amamentação / Leite"
    elif "bebê" in titulo or "bebês" in titulo or "como oferecer" in titulo or "protusão" in titulo or "não dar" in titulo or "reflexo" in titulo or "não incentive" in titulo or "peso" in titulo or "cérebro" in titulo or "primeiros" in titulo or "botões gustativos" in titulo or "suco" in titulo or "abacate" in titulo or "introdução alimentar" in titulo or "ia" in titulo or "banana" in titulo or "até" in titulo or "pasta" in titulo or "dieta" in titulo:
        return "Alimentação Bebê / Introdução alimentar"
    elif "aplv" in titulo or "alergia" in titulo or "dermatite" in titulo or "alergênico" in titulo:
        return "Alergias / APLV"
    elif "suplemento" in titulo or "nutrientes" in titulo or "vitamina" in titulo or "zinco" in titulo or "ômega 3" in titulo or "cálcio" in titulo:
        return "Suplementos / Nutrientes"
    elif "receita" in titulo or "mingau" in titulo or "picolé" in titulo:
        return "Receitas / Comida"
    elif titulo.startswith("q&a") or "?" in titulo:
        return "Perguntas / Q&A"
    else:
        return "Outros"