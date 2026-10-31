# -*- coding: utf-8 -*-
"""
Script de Compilação do Grande Tratado Profético Integrado de Daniel e Apocalipse.
Reúne os 7 Pilares Teológicos em um único volume absoluto em formato TXT e Markdown.
"""

import os
import sys

BASE_DIR = "/home/felipe/mycodes/estudos_biblicos"
SECTIONS_DIR = os.path.join(BASE_DIR, "tratado_sections")

OUTPUT_TXT = os.path.join(BASE_DIR, "Tratado_Profetico_Daniel_e_Apocalipse_Estudo_Absoluto.txt")
OUTPUT_MD = os.path.join(BASE_DIR, "Tratado_Profetico_Daniel_e_Apocalipse_Estudo_Absoluto.md")

PARTS = [
    ("parte1_fundamentos_babilonia_medopersia.txt", "Pilar 1: Fundamentos Hermenêuticos, Babilônia e Medo-Pérsia"),
    ("parte2_grecia_roma_imperial_divisao.txt", "Pilar 2: Grécia, Roma Imperial e a Fragmentação Europeia"),
    ("parte3_chifre_pequeno_besta_mar_1260anos.txt", "Pilar 3: A Ponta Pequena, A Besta do Mar e a Supremacia de 1.260 Anos"),
    ("parte4_2300tardes_manhas_70semanas_juizo1844.txt", "Pilar 4: As 2.300 Tardes e Manhãs, as 70 Semanas e o Juízo de 1844"),
    ("parte5_setenarios_igrejas_selos_trombetas.txt", "Pilar 5: Os Três Setenários — As Sete Igrejas, os Sete Selos e as Sete Trombetas"),
    ("parte6_tempo_do_fim_estados_unidos_marca_besta_tres_anjos.txt", "Pilar 6: O Tempo do Fim, os Estados Unidos, a Marca da Besta e as Três Mensagens Angélicas"),
    ("parte7_climax_pragas_segunda_vinda_milenio_nova_terra.txt", "Pilar 7: O Clímax da História, as Sete Pragas, a Parúsia, o Milênio e a Nova Terra"),
]

PROLOGUE = """====================================================================================================
GRANDE TRATADO PROFÉTICO INTEGRADO DE DANIEL E APOCALIPSE
====================================================================================================
A VISÃO HISTORICISTA COMPLETA, CRONOLÓGICA E TEOLÓGICA DO GRANDE CONFLITO DOS SÉCULOS
Baseado nas Sagradas Escrituras e nos Manuais Oficiais de Interpretação Profética 
da Igreja Adventista do Sétimo Dia

"O Senhor Deus nada fará sem primeiro revelar o Seu segredo aos Seus servos, os profetas." (Amós 3:7)
"Havendo Deus, antigamente, falado muitas vezes, e de muitas maneiras, aos pais, pelos profetas, a nós falou-nos nestes últimos dias pelo Filho." (Hebreus 1:1, 2)
"Temos mui firme a palavra dos profetas, à qual bem fazeis em estar atentos, como a uma luz que alumia em lugar escuro, até que o dia esclareça e a estrela da alva apareça em vossos corações." (2 Pedro 1:19)

----------------------------------------------------------------------------------------------------
PRÓLOGO: A NATUREZA, A ARQUITETURA E O PROPÓSITO DESTE TRATADO ABSOLUTO
----------------------------------------------------------------------------------------------------

Este tratado não é uma coletânea dispersa de lições fragmentadas, nem uma leitura rasa de versículos descontextualizados. Constitui uma obra de fôlego monumental, concebida para conduzir o leitor por uma jornada contínua, profunda, teologicamente densa e ininterrupta através de todas as revelações proféticas entrelaçadas dos livros de Daniel e do Apocalipse.

A hermenêutica que norteia cada parágrafo desta obra é o HISTORICISMO CLÁSSICO — o mesmo método adotado pelos apóstolos, pelos reformadores protestantes (Lutero, Calvino, Zuínglio, Melâncton, Knox, Cranmer, Isaac Newton) e amadurecido de forma definitiva pelo movimento adventista sob a orientação das Escrituras.

A arquitetura dos livros proféticos de Daniel e Apocalipse baseia-se em cinco princípios hermenêuticos invioláveis:
1. O Princípio da Recapitulação Progressiva: Cada visão retoma o mesmo arco histórico (desde a antiguidade até a consumação eterna), aprofundando detalhes políticos, espirituais, judiciais e cósmicos que não foram revelados na visão anterior;
2. O Princípio Dia-Ano (Números 14:34; Ezequiel 4:6): Nas profecias apocalípticas de caráter simbólico, um dia profético representa um ano solar literal na história;
3. A Centralidade do Santuário Celestial e do Sacerdócio de Cristo (Hebreus 8 e 9): Todas as profecias do Apocalipse e de Daniel são estruturadas em torno do ministério contínuo (*Tamid*) e da purificação final (*Yom Kippur*) operada por Jesus Cristo no templo celestial;
4. O Tema Unificador do Grande Conflito entre Cristo e Satanás: As convulsões geopolíticas, guerras e perseguições terrestres são o reflexo terreno da batalha espiritual originada no Céu e consumada no Calvário;
5. A Vitória Incondicional do Povo de Deus e a Instalação do Reino Eterno: Todos os impérios terrestres e poderes apóstatas sucumbem irrevogavelmente perante a Rocha celestial cortada sem auxílio de mãos humanas.

A seguir, apresentamos os 7 Grandes Pilares Proféticos em progressão cronológica e teológica absoluta.
====================================================================================================

"""

EPILOGUE = """
====================================================================================================
EPÍLOGO: O PANORAMA CRONOLÓGICO INTEGRADO E A CONSUMAÇÃO DA ESPERANÇA
====================================================================================================

"Aquele que dá testemunho destas coisas diz: Certamente cedo venho. Amém; vem, Senhor Jesus!" (Apocalipse 22:20)

1. LINHA DO TEMPO HISTORICISTA UNIFICADA (605 a.C. À ETERNIDADE)
----------------------------------------------------------------------------------------------------
• 605 a.C. – Início do cativeiro babilônico e primeiro império mundial da profecia (Cabeça de ouro de Daniel 2; Leão alado de Daniel 7).
• 539 a.C. – Conquista de Babilônia por Ciro e início do Império Medo-Persa (Peito e braços de prata de Daniel 2; Urso com três costelas de Daniel 7; Carneiro com dois chifres de Daniel 8).
• 457 a.C. – Decreto do rei Artaxerxes Longímano para restaurar e reedificar Jerusalém (Esdras 7). Ponto de partida inegociável das 70 semanas (490 anos) e das 2.300 tardes e manhãs (Daniel 8:14; 9:25).
• 331 a.C. – Batalha de Gaugamela: Alexandre, o Grande, derrota Dario III e estabelece o Império Greco-Macedônio (Ventre e coxas de bronze de Daniel 2; Leopardo com quatro asas e quatro cabeças de Daniel 7; Bode com o chifre notável de Daniel 8).
• 323 a.C. – Morte de Alexandre na Babilônia; divisão do império em quatro reinos helenísticos (Diádocos: Cassandro, Lisímaco, Seleuco e Ptolomeu).
• 168 a.C. – Batalha de Pidna: Roma subjuga a Macedônia e emerge como o quarto império mundial (Pernas de ferro de Daniel 2; Besta terrível e espantosa com dentes de ferro de Daniel 7; Ponta pequena em sua fase horizontal de Daniel 8).
• 27 d.C. – Batismo de Jesus Cristo no Jordão no 15º ano de Tibério César; início do ministério do Messias ungido exatamente ao fim das 69 semanas (483 anos) de Daniel 9:25 (Lucas 3:1, 21-23).
• 31 d.C. – Crucificação expiatória de Cristo na Páscoa, na "metade da septuagésima semana" (Daniel 9:27); o sacrifício e a oblação cessam com o rasgar sobrenatural do véu do templo terrestre (Mateus 27:51). Ascensão de Cristo como Sumo Sacerdote no Santuário Celestial (Hebreus 9:11-12, 24).
• 34 d.C. – Apedrejamento do diácono Estêvão perante o Sinédrio judaico; encerramento definitivo das 70 semanas reservadas à teocracia de Israel (Daniel 9:24); o evangelho é levado oficialmente aos gentios através da conversão de Saulo de Tarso.
• 476 d.C. – Queda do Império Romano do Ocidente (deposição de Rômulo Augústulo por Odoacro); fragmentação de Roma em dez reinos tribais bárbaros (Pés e dedos de ferro e barro de Daniel 2; Dez chifres de Daniel 7).
• 538 d.C. – Expulsão dos ostrogodos de Roma pelo general Belisário e entrada em pleno vigor do decreto do imperador Justiniano que proclamou o Bispo de Roma "cabeça de todas as santas igrejas"; início dos 1.260 anos de supremacia papal (Daniel 7:25; 12:7; Apocalipse 11:2-3; 12:6, 14; 13:5).
• 1517 d.C. – Início da Reforma Protestante (Martinho Lutero afixa as 95 Teses em Wittenberg); desmascaramento do anticristo e restauração das verdades fundamentais das Escrituras.
• 1755 d.C. (1º de Novembro) – O Grande Terremoto de Lisboa; primeiro sinal cósmico preliminar do sexto selo (Apocalipse 6:12).
• 1780 d.C. (19 de Maio) – O "Dia Escuro" e a lua em sangue na América do Norte; segundo grande sinal astronômico do sexto selo (Apocalipse 6:12; Marcos 13:24).
• 1798 d.C. (15 de Fevereiro) – O general francês Louis-Alexandre Berthier invade Roma, depõe o Papa Pio VI e abole o poder temporal papal; término dos 1.260 anos proféticos e recebimento da "ferida mortal" pela besta do mar (Daniel 7:25; Apocalipse 13:3). Início oficial do "TEMPO DO FIM" (Daniel 12:4, 9).
• 1798 d.C. – Emergência simultânea da "Besta que sobe da terra" (Estados Unidos da América) com dois chifres como de cordeiro (republicanismo e protestantismo) em território despovoado (Apocalipse 13:11).
• 1833 d.C. (13 de Novembro) – A espetacular chuva de meteoros das Leônidas em toda a América do Norte; cumprimento do terceiro sinal astronômico do sexto selo ("as estrelas do céu caíram sobre a terra", Apocalipse 6:13).
• 1840 d.C. (11 de Agosto) – Capitulação do Império Otomano às potências europeias conforme a predição profética de Josiah Litch baseada na sexta trombeta (Apocalipse 9:15), validando o princípio dia-ano perante o mundo.
• 1844 d.C. (22 de Outubro) – Fim dos 2.300 anos proféticos de Daniel 8:14; início do Juízo Investigativo pré-advento no Santo dos Santos do Santuário Celestial (*Yom Kippur* antitípico); início do período da Igreja de Laodiceia (Apocalipse 3:14) e proclamação mundial da Tríplice Mensagem Angélica (Apocalipse 14:6-12).
• FUTURO PRÓXIMO – Crise final: promulgação de leis dominicais compulsórias lideradas pelos Estados Unidos da América (imagem e marca da besta, Apocalipse 13:14-17); sacudidura e selamento final dos 144.000 fiéis guardadores dos mandamentos de Deus e da fé de Jesus (Apocalipse 7:1-4; 14:12); o Alto Clamor com a descida do quarto anjo de Apocalipse 18.
• CONSUMAÇÃO – Fechamento da Porta da Graça (Apocalipse 22:11); Miguel Se levanta (Daniel 12:1); o Tempo de Angústia de Jacó sem precedentes; derramamento das Sete Últimas Pragas sobre a Babilônia impenitente (Apocalipse 16); batalha do Armagedom.
• A SEGUNDA VINDA – Ressurreição especial (Daniel 12:2; Apocalipse 1:7); gloriosa e visível descida de Cristo com todas as hostes celestes (Mateus 25:31; Apocalipse 19:11-16); a Rocha atinge os pés da estátua (Daniel 2:34-35); ressurreição geral dos justos e trasladação dos santos vivos (1 Tessalonicenses 4:16-17; 1 Coríntios 15:51-54); destruição dos ímpios vivos pelo resplendor da glória (2 Tessalonicenses 2:8).
• O MILÊNIO (1.000 ANOS NO CÉU) – A Terra vazia e em trevas profundas (*abussos* de Jeremias 4:23-26); Satanás amarrado pelas circunstâncias inelutáveis; os santos reinam com Cristo no céu exercendo o juízo confirmatório e examinando os livros celestes (Apocalipse 20:4; 1 Coríntios 6:2-3).
• PÓS-MILÊNIO – Descida da Nova Jerusalém sobre o Monte das Oliveiras fendido (Apocalipse 21:2; Zacarias 14:4-5); segunda ressurreição (ressurreição dos ímpios para condenação, Apocalipse 20:5); Satanás solto arregimenta as nações para sitiar a Cidade Santa; Sessão do Juízo do Grande Trono Branco (Apocalipse 20:11-13); todo joelho se dobra e confessa a soberania de Cristo (Filipenses 2:10-11); o fogo desce do céu e devora os rebeldes (a Segunda Morte e a aniquilação completa de Malaquias 4:1-3 e Ezequiel 28:18-19).
• A ETERNIDADE NA NOVA TERRA – Recriação perfeita da biosfera terrena (*kainos* de Apocalipse 21:1-5; 2 Pedro 3:13); comunhão corporal e tangível de Deus com o Seu povo remido (Apocalipse 21:3; Isaías 65:21-25); guarda contínua do Sábado de sábado em sábado por toda a eternidade (Isaías 66:22-23); a imunização perpétua do universo contra o mal (Naum 1:9). O Grande Conflito findou para todo o sempre: DEUS É AMOR!
====================================================================================================
"""

def compile_tratado():
    print("Iniciando verificação e compilação dos 7 Pilares...")
    
    missing = []
    for filename, title in PARTS:
        path = os.path.join(SECTIONS_DIR, filename)
        if not os.path.exists(path) or os.path.getsize(path) < 1000:
            missing.append((filename, title))
            
    if missing:
        print(f"Atenção: Os seguintes arquivos ainda não estão prontos: {missing}")
        return False
        
    print("Todos os 7 arquivos estão prontos! Lendo seções...")
    
    full_content = PROLOGUE
    
    for filename, title in PARTS:
        path = os.path.join(SECTIONS_DIR, filename)
        size = os.path.getsize(path)
        print(f" - Lendo {filename} ({size:,} bytes)...")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            
        full_content += f"\n\n{'='*100}\n{title.upper()}\n{'='*100}\n\n"
        full_content += content
        full_content += "\n\n"
        
    full_content += EPILOGUE
    
    print(f"Gravando arquivo TXT mestre em: {OUTPUT_TXT}...")
    with open(OUTPUT_TXT, "w", encoding="utf-8") as f:
        f.write(full_content)
        
    print(f"Gravando arquivo Markdown mestre em: {OUTPUT_MD}...")
    with open(OUTPUT_MD, "w", encoding="utf-8") as f:
        f.write(full_content)
        
    txt_size = os.path.getsize(OUTPUT_TXT)
    word_count = len(full_content.split())
    lines_count = len(full_content.splitlines())
    
    print("="*60)
    print("COMPILAÇÃO CONCLUÍDA COM SUCESSO ABSOLUTO!")
    print(f" - Tamanho do Tratado TXT: {txt_size:,} bytes (~{txt_size/(1024*1024):.2f} MB)")
    print(f" - Contagem total de palavras: {word_count:,}")
    print(f" - Linhas totais: {lines_count:,}")
    print("="*60)
    return True

if __name__ == "__main__":
    compile_tratado()
