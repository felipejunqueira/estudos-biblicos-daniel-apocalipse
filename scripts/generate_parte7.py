# -*- coding: utf-8 -*-
"""
Gerador da PARTE 7 do Grande Tratado Profético de Daniel e Apocalipse:
'O Clímax da História — As Sete Pragas, A Segunda Vinda Visível, O Milênio no Céu e o Triunfo da Nova Terra'
"""

import os
import sys

# Garante importação dos módulos locais
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from build_parte7_ch1 import get_chapter_1
from build_parte7_ch2 import get_chapter_2
from build_parte7_ch3 import get_chapter_3
from build_parte7_ch4 import get_chapter_4
from build_parte7_ch5 import get_chapter_5
from build_parte7_ch6 import get_chapter_6

output_path = "/home/felipe/mycodes/estudos_biblicos/tratado_sections/parte7_climax_pragas_segunda_vinda_milenio_nova_terra.txt"
os.makedirs(os.path.dirname(output_path), exist_ok=True)

print("Compilando a Parte 7 do Grande Tratado Profético...")

full_text = (
    get_chapter_1() + "\n" +
    get_chapter_2() + "\n" +
    get_chapter_3() + "\n" +
    get_chapter_4() + "\n" +
    get_chapter_5() + "\n" +
    get_chapter_6()
)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(full_text)

size_bytes = os.path.getsize(output_path)
lines_count = len(full_text.splitlines())
words_count = len(full_text.split())

print(f"Arquivo gerado com sucesso em: {output_path}")
print(f"Estatísticas:")
print(f" - Tamanho: {size_bytes:,} bytes")
print(f" - Linhas: {lines_count:,}")
print(f" - Palavras: {words_count:,}")
