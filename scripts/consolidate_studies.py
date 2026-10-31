#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Script de Consolidação e Harmonização Final dos Estudos Bíblicos
Orquestrador Chefe e Auditor de Qualidade Máxima (Gemini 4 Argon Max)
"""

import glob
import os
import re

BASE_DIR = "/home/felipe/mycodes/estudos_biblicos"
DANIEL_DIR = os.path.join(BASE_DIR, "transcricoes_daniel")
APOC_DIR = os.path.join(BASE_DIR, "transcricoes_apocalipse")

DANIEL_OUT = os.path.join(BASE_DIR, "Estudo_Biblico_Daniel_Transcricao_Completa.txt")
APOC_OUT = os.path.join(BASE_DIR, "Estudo_Biblico_Apocalipse_Transcricao_Completa.txt")

DANIEL_HEADER = """================================================================================
GUIA DE ESTUDO BÍBLICO: BÍBLIA FÁCIL - PROFECIAS DE DANIEL
Autor: Pr. Arilton Cordeiro de Oliveira
Rede Novo Tempo de Comunicação / Casa Publicadora Brasileira
TRANSCRIÇÃO COMPLETA, INTEGRAL, LITERAL E AUDITADA (84 PÁGINAS)
================================================================================
"""

APOC_HEADER = """================================================================================
GUIA DE ESTUDO BÍBLICO: BÍBLIA FÁCIL - O LIVRO DO APOCALIPSE
Autor: Pr. Arilton Cordeiro de Oliveira
Rede Novo Tempo de Comunicação / Casa Publicadora Brasileira
TRANSCRIÇÃO COMPLETA, INTEGRAL, LITERAL E AUDITADA (101 PÁGINAS)
================================================================================
"""

def clean_and_harmonize(text, is_first_sec=False, is_sec_10=False):
    lines = text.splitlines()
    
    # Se não for a primeira seção e começar com banner "===" de seção, remover banner
    if not is_first_sec:
        if lines and lines[0].startswith("==="):
            for i in range(1, min(15, len(lines))):
                if lines[i].startswith("==="):
                    lines = lines[i+1:]
                    break
    else:
        # Na primeira seção, se tiver banner de "SEÇÃO 01", remover o banner de seção
        if lines and lines[0].startswith("==="):
            for i in range(1, min(10, len(lines))):
                if lines[i].startswith("==="):
                    lines = lines[i+1:]
                    break

    # Limpar linhas em branco iniciais
    while lines and not lines[0].strip():
        lines.pop(0)

    harmonized_lines = []
    for line in lines:
        # Harmonizar marcadores de perguntas: ● ou • para ■
        line = re.sub(r"^[ \t]*[●•][ \t]+(\d+\.)", r"■ \1", line)
        # Harmonizar tags de página: === PÁGINA XX === -> [PÁGINA XX]
        line = re.sub(r"^===\s*PÁGINA\s+(\d+)\s*===", r"[PÁGINA \1]", line, flags=re.IGNORECASE)
        # Padronizar tags de página [PAGINA XX] para [PÁGINA XX]
        line = re.sub(r"^\[PAGINA\s+(\d+)\]", r"[PÁGINA \1]", line, flags=re.IGNORECASE)
        harmonized_lines.append(line)

    return "\n".join(harmonized_lines).strip()

def consolidate_daniel():
    print("=== Consolidando Estudo de Daniel ===")
    sec_files = sorted(glob.glob(os.path.join(DANIEL_DIR, "sec_*_transcrito.txt")))
    assert len(sec_files) == 10, f"Daniel: esperava 10 seções, encontrou {len(sec_files)}"
    
    parts = [DANIEL_HEADER.strip()]
    for idx, f in enumerate(sec_files, start=1):
        with open(f, "r", encoding="utf-8") as fp:
            content = fp.read()
        cleaned = clean_and_harmonize(content, is_first_sec=(idx==1), is_sec_10=(idx==10))
        
        separator = f"\n\n{'='*80}\n" if idx > 1 else "\n\n"
        parts.append(separator + cleaned)
        print(f"  Adicionada seção {idx:02d}: {os.path.basename(f)} ({len(cleaned)} caracteres)")

    full_text = "\n".join(parts) + "\n"
    with open(DANIEL_OUT, "w", encoding="utf-8") as fp:
        fp.write(full_text)
    
    print(f"-> Arquivo consolidado gravado: {DANIEL_OUT}")
    print(f"   Tamanho total: {len(full_text)} caracteres, {len(full_text.splitlines())} linhas, {os.path.getsize(DANIEL_OUT)} bytes.\n")
    return full_text

def consolidate_apocalipse():
    print("=== Consolidando Estudo de Apocalipse ===")
    sec_files = sorted(glob.glob(os.path.join(APOC_DIR, "sec_*_transcrito.txt")))
    assert len(sec_files) == 10, f"Apocalipse: esperava 10 seções, encontrou {len(sec_files)}"
    
    parts = [APOC_HEADER.strip()]
    for idx, f in enumerate(sec_files, start=1):
        with open(f, "r", encoding="utf-8") as fp:
            content = fp.read()
        cleaned = clean_and_harmonize(content, is_first_sec=(idx==1), is_sec_10=(idx==10))
        
        separator = f"\n\n{'='*80}\n" if idx > 1 else "\n\n"
        parts.append(separator + cleaned)
        print(f"  Adicionada seção {idx:02d}: {os.path.basename(f)} ({len(cleaned)} caracteres)")

    full_text = "\n".join(parts) + "\n"
    with open(APOC_OUT, "w", encoding="utf-8") as fp:
        fp.write(full_text)
        
    print(f"-> Arquivo consolidado gravado: {APOC_OUT}")
    print(f"   Tamanho total: {len(full_text)} caracteres, {len(full_text.splitlines())} linhas, {os.path.getsize(APOC_OUT)} bytes.\n")
    return full_text

if __name__ == "__main__":
    consolidate_daniel()
    consolidate_apocalipse()
