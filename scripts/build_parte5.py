# -*- coding: utf-8 -*-
"""
Script construtor para a Parte 5 do Grande Tratado Profético de Daniel e Apocalipse
"""

import sys

output_file = "/home/felipe/mycodes/estudos_biblicos/tratado_sections/parte5_setenarios_igrejas_selos_trombetas.txt"

def write_section(content, mode="a"):
    with open(output_file, mode, encoding="utf-8") as f:
        f.write(content)

# Limpar arquivo se existir
with open(output_file, "w", encoding="utf-8") as f:
    f.write("")

print("Arquivo inicializado com sucesso.")
