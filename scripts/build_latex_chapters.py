# -*- coding: utf-8 -*-
"""
Script construtor de capítulos LaTeX para o Grande Tratado Profético de Daniel e Apocalipse.
Converte as 7 seções completas em código LaTeX robusto, limpo e profissional,
removendo glifos gregos/hebraicos puros (mantendo a transliteração latina erudita),
agrupando listas em ambientes itemize/enumerate contínuos, convertendo tabelas Markdown
em ambientes tabularx formais, tratando citações com '>' e integrando os diagramas TikZ.
"""

import os
import re

BASE_DIR = "/home/felipe/mycodes/estudos_biblicos"
SECTIONS_DIR = os.path.join(BASE_DIR, "tratado_sections")
LATEX_CAP_DIR = os.path.join(BASE_DIR, "latex", "capitulos")

CHAPTERS = [
    {
        "id": 1,
        "src": "parte1_fundamentos_babilonia_medopersia.txt",
        "out": "pilar1.tex",
        "title": "Pilar I: Fundamentos Hermenêuticos e os Primeiros Reinos Mundiais",
        "diagram": "\\input{diagramas/imperios_daniel2.tex}\n\n"
    },
    {
        "id": 2,
        "src": "parte2_grecia_roma_imperial_divisao.txt",
        "out": "pilar2.tex",
        "title": "Pilar II: Grécia Macedônica, Roma Imperial e a Divisão Ocidental",
        "diagram": ""
    },
    {
        "id": 3,
        "src": "parte3_chifre_pequeno_besta_mar_1260anos.txt",
        "out": "pilar3.tex",
        "title": "Pilar III: A Ponta Pequena, a Besta do Mar e a Supremacia de 1.260 Anos",
        "diagram": ""
    },
    {
        "id": 4,
        "src": "parte4_2300tardes_manhas_70semanas_juizo1844.txt",
        "out": "pilar4.tex",
        "title": "Pilar IV: As 2.300 Tardes e Manhãs, as 70 Semanas e o Juízo de 1844",
        "diagram": "\\input{diagramas/timeline_2300dias.tex}\n\n"
    },
    {
        "id": 5,
        "src": "parte5_setenarios_igrejas_selos_trombetas.txt",
        "out": "pilar5.tex",
        "title": "Pilar V: Os Três Setenários — As Sete Igrejas, os Sete Selos e as Sete Trombetas",
        "diagram": "\\input{diagramas/setenarios_apocalipse.tex}\n\n"
    },
    {
        "id": 6,
        "src": "parte6_tempo_do_fim_estados_unidos_marca_besta_tres_anjos.txt",
        "out": "pilar6.tex",
        "title": "Pilar VI: O Tempo do Fim, os Estados Unidos e as Três Mensagens Angélicas",
        "diagram": ""
    },
    {
        "id": 7,
        "src": "parte7_climax_pragas_segunda_vinda_milenio_nova_terra.txt",
        "out": "pilar7.tex",
        "title": "Pilar VII: O Clímax da História, as Sete Pragas, a Parúsia e a Nova Terra",
        "diagram": "\\input{diagramas/escatologia_final.tex}\n\n"
    }
]

def clean_script_characters(text):
    """
    Remove caracteres gregos ou hebraicos puros e parênteses vazios resultantes,
    mantendo intactas as transliterações latinas já presentes no texto original.
    """
    # Remove caracteres gregos (0370 a 03FF, 1F00 a 1FFF)
    text = re.sub(r'[\u0370-\u03ff\u1f00-\u1fff]+', '', text)
    # Remove caracteres hebraicos (0590 a 05FF)
    text = re.sub(r'[\u0590-\u05ff]+', '', text)
    # Limpa parênteses que ficaram vazios ou com apenas espaços/vírgulas
    text = re.sub(r'\(\s*[,;\-\–\—\:]*\s*\)', '', text)
    text = re.sub(r'\(\s*\)', '', text)
    # Limpa vírgulas ou ponto-e-vírgula órfãos antes de fechar parênteses: "(euaggelion aionion, )" -> "(euaggelion aionion)"
    text = re.sub(r'[,;]\s*\)', ')', text)
    # Limpa espaços duplos
    text = re.sub(r'[ \t]{2,}', ' ', text)
    return text

def escape_latex(text):
    # Proteger caracteres reservados do LaTeX
    text = text.replace('\\', '\\textbackslash{}')
    text = text.replace('&', '\\&')
    text = text.replace('%', '\\%')
    text = text.replace('$', '\\$')
    text = text.replace('#', '\\#')
    text = text.replace('_', '\\_')
    text = text.replace('{', '\\{')
    text = text.replace('}', '\\}')
    text = text.replace('~', '\\textasciitilde{}')
    text = text.replace('^', '\\textasciicircum{}')
    text = text.replace('<', '$<$')
    text = text.replace('>', '$>$')
    text = text.replace('|', '\\textbar{}')
    return text

def format_inline(text, in_heading=False):
    """
    Escapa caracteres LaTeX e aplica negrito (**...**), itálico (*...*) e aspas tipográficas.
    Se in_heading=True, remove aspas retas/curvas para evitar conflitos com hyperref/bookmarks.
    """
    if in_heading:
        text = text.replace('"', '').replace('“', '').replace('”', '')
    escaped = escape_latex(text)
    escaped = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', escaped)
    escaped = re.sub(r'\*(.*?)\*', r'\\textit{\1}', escaped)
    if not in_heading:
        escaped = re.sub(r'"([^"]*)"', r"``\1''", escaped)
        # Se sobrar alguma aspa dupla isolada, substitui por ''
        escaped = escaped.replace('"', "''")
    return escaped

def render_markdown_table(table_lines):
    """
    Converte uma lista de linhas de tabela Markdown (| col1 | col2 | ...)
    em um ambiente tabularx elegante com booktabs.
    """
    rows = []
    for line in table_lines:
        s = line.strip()
        if s.startswith('|') and s.endswith('|'):
            s = s[1:-1]
        cells = [c.strip() for c in s.split('|')]
        # Verificar se é linha separadora (ex: :--- | :---)
        if all(re.match(r'^[:\-\s]+$', c) for c in cells if c):
            continue
        rows.append(cells)

    if not rows:
        return ""

    num_cols = max(len(r) for r in rows)
    if num_cols == 3:
        col_spec = ">{\\raggedright\\arraybackslash}p{0.24\\textwidth} >{\\raggedright\\arraybackslash}X >{\\raggedright\\arraybackslash}X"
    elif num_cols == 5:
        col_spec = ">{\\raggedright\\arraybackslash}p{0.14\\textwidth} >{\\raggedright\\arraybackslash}X >{\\raggedright\\arraybackslash}X >{\\raggedright\\arraybackslash}X >{\\raggedright\\arraybackslash}X"
    else:
        col_spec = " ".join([">{\\raggedright\\arraybackslash}X"] * num_cols)

    out = []
    out.append("\n\\begin{table}[htbp]")
    out.append("\\centering")
    out.append("\\footnotesize")
    out.append("\\setlength{\\tabcolsep}{5pt}")
    out.append("\\renewcommand{\\arraystretch}{1.25}")
    out.append(f"\\begin{{tabularx}}{{\\textwidth}}{{{col_spec}}}")
    out.append("\\toprule")

    # Header
    header = rows[0]
    while len(header) < num_cols:
        header.append("")
    header_formatted = [f"\\textbf{{{format_inline(c)}}}" for c in header]
    out.append(" & ".join(header_formatted) + " \\\\")
    out.append("\\midrule")

    # Body
    for r in rows[1:]:
        while len(r) < num_cols:
            r.append("")
        row_formatted = [format_inline(c) for c in r[:num_cols]]
        out.append(" & ".join(row_formatted) + " \\\\")
        out.append("\\addlinespace[3pt]")

    out.append("\\bottomrule")
    out.append("\\end{tabularx}")
    out.append("\\end{table}\n")
    return "\n".join(out)

def convert_section_to_latex(raw_text, chapter_title, diagram_code=""):
    # Limpa caracteres gregos/hebraicos puros
    raw_text = clean_script_characters(raw_text)
    lines = raw_text.splitlines()
    
    latex_output = []
    latex_output.append(f"\\chapter{{{chapter_title}}}\n")
    if diagram_code:
        latex_output.append(diagram_code)
        
    in_itemize = False
    in_enumerate = False
    table_buffer = []
    skip_header = True

    def close_lists():
        nonlocal in_itemize, in_enumerate
        res = []
        if in_itemize:
            res.append("\\end{itemize}\n")
            in_itemize = False
        if in_enumerate:
            res.append("\\end{enumerate}\n")
            in_enumerate = False
        return res

    def flush_table():
        nonlocal table_buffer
        if not table_buffer:
            return []
        res = [render_markdown_table(table_buffer)]
        table_buffer = []
        return res

    for line in lines:
        stripped = line.strip()

        # Detectar linhas de tabela Markdown
        if stripped.startswith('|') and stripped.endswith('|') and stripped.count('|') >= 2:
            latex_output.extend(close_lists())
            table_buffer.append(stripped)
            continue
        else:
            if table_buffer:
                latex_output.extend(flush_table())

        # Pular linhas de separação estética ASCII (=== ou ---)
        if re.match(r'^[=\-]{3,}$', stripped):
            continue

        # Pular marcadores de FIM DA PARTE no final dos arquivos
        if re.match(r'^#*\s*FIM\s+DA\s+PARTE', stripped, re.IGNORECASE):
            continue

        # Verificar prefixo Markdown (#, ##, ###, ####, #####)
        md_match = re.match(r'^(#{1,6})\s+(.*)$', stripped)
        md_level = len(md_match.group(1)) if md_match else 0
        clean_stripped = md_match.group(2).strip() if md_match else stripped

        # Pular o título inicial repetido no topo do arquivo original
        if skip_header and ("GRANDE TRATADO PROFÉTICO" in clean_stripped.upper() or ("PARTE" in clean_stripped.upper() and any(x in clean_stripped.upper() for x in ["1:", "2:", "3:", "4:", "5:", "6:", "VII:"]))):
            continue
        elif clean_stripped:
            skip_header = False

        if not stripped:
            latex_output.extend(close_lists())
            latex_output.append("")
            continue

        # Tratar Títulos Especiais de Introdução / Conclusão / Síntese
        if re.match(r'^(?:INTRODUÇÃO\s+GERAL|CONCLUSÃO\s+GERAL|SÍNTESE\s+ANALÍTICA)(.*)$', clean_stripped, re.IGNORECASE):
            latex_output.extend(close_lists())
            sec_clean = format_inline(clean_stripped, in_heading=True)
            latex_output.append(f"\n\\section{{{sec_clean}}}\n")
            continue

        # Tratar Seções (SEÇÃO I: ... ou CAPÍTULO 1: ...)
        sec_match = re.match(r'^(?:SEÇÃO|CAPÍTULO)\s+([IVX0-9]+)[:\.\-]\s*(.*)$', clean_stripped, re.IGNORECASE)
        if sec_match:
            latex_output.extend(close_lists())
            sec_name = sec_match.group(2).strip()
            sec_clean = format_inline(sec_name, in_heading=True)
            latex_output.append(f"\n\\section{{{sec_clean}}}\n")
            continue

        # Tratar Subseções numéricas (1.1. O Princípio... ou 2.1 A Natureza...)
        subsec_match = re.match(r'^([0-9]+\.[0-9]+)\.?\s*(.*)$', clean_stripped)
        if subsec_match:
            latex_output.extend(close_lists())
            sub_name = subsec_match.group(2).strip()
            sub_clean = format_inline(sub_name, in_heading=True)
            latex_output.append(f"\n\\subsection{{{sub_clean}}}\n")
            continue

        # Tratar cabeçalhos Markdown #### e ##### (como em parte6)
        if md_level == 4:
            latex_output.extend(close_lists())
            # Remove eventual número inicial "1. " para deixar o \subsection numerar automaticamente
            sub_name = re.sub(r'^\d+\.\s*', '', clean_stripped)
            sub_clean = format_inline(sub_name, in_heading=True)
            latex_output.append(f"\n\\subsection{{{sub_clean}}}\n")
            continue
        elif md_level >= 5:
            latex_output.extend(close_lists())
            subsub_clean = format_inline(clean_stripped, in_heading=True)
            latex_output.append(f"\n\\subsubsection*{{{subsub_clean}}}\n")
            continue

        # Sub-subseções ou cabeçalhos temáticos como "a) O Título Cristológico:"
        subsubsec_match = re.match(r'^([a-z]\)|\d+\.)\s+([A-ZÀ-Ú][^:]{2,60}:)(.*)$', stripped)
        if subsubsec_match and not (stripped.startswith(('1.', '2.', '3.', '4.', '5.', '6.', '7.', '8.', '9.')) and in_enumerate):
            latex_output.extend(close_lists())
            title = subsubsec_match.group(2).rstrip(':')
            rest = subsubsec_match.group(3).strip()
            t_clean = format_inline(title, in_heading=True)
            latex_output.append(f"\n\\subsubsection*{{{t_clean}}}")
            if rest:
                r_clean = format_inline(rest)
                latex_output.append(r_clean)
            continue

        # Blockquotes iniciados com '>'
        if stripped.startswith('>'):
            latex_output.extend(close_lists())
            q_content = stripped.lstrip('>').strip()
            # Remover asteriscos externos se toda a citação estiver em itálico
            q_clean = format_inline(q_content)
            latex_output.append(f"\n\\begin{{quote}}\n\\itshape {q_clean}\n\\end{{quote}}\n")
            continue

        # Citações bíblicas destacadas (entre aspas no início e fim com mais de 30 caracteres)
        if stripped.startswith('"') and stripped.endswith('"') and len(stripped) > 30:
            latex_output.extend(close_lists())
            content = stripped[1:-1]
            c_clean = format_inline(content)
            latex_output.append(f"\n\\begin{{quote}}\n\\itshape ``{c_clean}''\n\\end{{quote}}\n")
            continue

        # Listas com marcadores (- item, * item, • item)
        if stripped.startswith(('- ', '* ', '• ')):
            if in_enumerate:
                latex_output.extend(close_lists())
            if not in_itemize:
                latex_output.append("\\begin{itemize}")
                in_itemize = True
            item_text = stripped[2:].strip()
            item_clean = format_inline(item_text)
            latex_output.append(f"  \\item {item_clean}")
            continue

        # Listas numeradas (1. item, 2. item)
        num_match = re.match(r'^(\d+)\.\s+(.*)$', stripped)
        if num_match and len(num_match.group(2)) < 350:
            if in_itemize:
                latex_output.extend(close_lists())
            if not in_enumerate:
                latex_output.append("\\begin{enumerate}")
                in_enumerate = True
            item_text = num_match.group(2).strip()
            item_clean = format_inline(item_text)
            latex_output.append(f"  \\item {item_clean}")
            continue

        # Se for texto normal, fecha listas abertas
        latex_output.extend(close_lists())

        # Parágrafo normal
        p_clean = format_inline(stripped)
        latex_output.append(p_clean)

    if table_buffer:
        latex_output.extend(flush_table())
    latex_output.extend(close_lists())
    return "\n".join(latex_output)

def build_all():
    os.makedirs(LATEX_CAP_DIR, exist_ok=True)
    print("Iniciando geração completa e robusta dos capítulos LaTeX...")

    for ch in CHAPTERS:
        src_path = os.path.join(SECTIONS_DIR, ch["src"])
        out_path = os.path.join(LATEX_CAP_DIR, ch["out"])

        print(f"Processando {ch['src']} -> {ch['out']}...")
        with open(src_path, "r", encoding="utf-8") as f:
            raw_text = f.read()

        latex_code = convert_section_to_latex(raw_text, ch["title"], ch["diagram"])

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(latex_code)

        size = os.path.getsize(out_path)
        print(f" - Salvo com sucesso: {out_path} ({size:,} bytes)")

    print("Todos os 7 capítulos LaTeX foram construídos com sucesso!")

if __name__ == "__main__":
    build_all()
