from fpdf import FPDF

# Criar um PDF

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Tabelas Verdade - Atividade de Lógica", ln=True, align='C')
pdf.ln(10)

pdf.set_font("Arial", '', 12)

# 1. Conjunção (AND)

pdf.multi_cell(0, 6, "1. Tabela Verdade para Conjunção (AND - E)\nProposições: P = 'Hoje é segunda-feira', Q = 'Está chovendo'\nP AND Q:\n")
pdf.multi_cell(0, 6, "P | Q | P AND Q\nV | V | V\nV | F | F\nF | V | F\nF | F | F\nObservação: Conjunção é verdadeira apenas se ambas forem verdadeiras.\n")
pdf.ln(5)

# 2. Disjunção (OR)

pdf.multi_cell(0, 6, "2. Tabela Verdade para Disjunção (OR - OU)\nProposições: R = 'A luz está acesa', S = 'A porta está aberta'\nR OR S:\n")
pdf.multi_cell(0, 6, "R | S | R OR S\nV | V | V\nV | F | V\nF | V | V\nF | F | F\nObservação: Disjunção é verdadeira se pelo menos uma proposição for verdadeira.\n")
pdf.ln(5)

# 3. Negação (NOT)

pdf.multi_cell(0, 6, "3. Tabela Verdade para Negação (NOT)\nProposição: T = 'O céu está limpo'\nNOT T:\n")
pdf.multi_cell(0, 6, "T | NOT T\nV | F\nF | V\nObservação: Negação inverte o valor lógico.\n")
pdf.ln(5)

# 4. Leis de De Morgan

pdf.multi_cell(0, 6, "4. Aplicação das Leis de De Morgan\nProposições: U = 'O computador está ligado', V = 'A internet está conectada'\nNOT (U AND V) = NOT U OR NOT V\n")
pdf.multi_cell(0, 6, "U | V | U AND V | NOT (U AND V) | NOT U | NOT V | NOT U OR NOT V\nV | V | V | F | F | F | F\nV | F | F | V | F | V | V\nF | V | F | V | V | F | V\nF | F | F | V | V | V | V\nObservação: NOT (U AND V) é equivalente a NOT U OR NOT V.\n")
pdf.ln(5)

# 5. Tautologia, Contradição e Contingência

pdf.multi_cell(0, 6, "5. Identificação de Tautologia, Contradição e Contingência\n")

# Tautologia

pdf.multi_cell(0, 6, "a) Tautologia W = P OR NOT P\nP | NOT P | P OR NOT P\nV | F | V\nF | V | V\nSempre verdadeira.\n")

# Contradição

pdf.multi_cell(0, 6, "b) Contradição X = P AND NOT P\nP | NOT P | P AND NOT P\nV | F | F\nF | V | F\nSempre falsa.\n")

# Contingência

pdf.multi_cell(0, 6, "c) Contingência Y = (P OR Q) AND (NOT Q OR R)\nP | Q | R | P OR Q | NOT Q | NOT Q OR R | Y\nV | V | V | V | F | V | V\nV | V | F | V | F | F | F\nV | F | V | V | V | V | V\nV | F | F | V | V | V | V\nF | V | V | V | F | V | V\nF | V | F | V | F | F | F\nF | F | V | F | V | V | F\nF | F | F | F | V | V | F\nNem sempre verdadeira nem sempre falsa.\n")

pdf.multi_cell(0, 6, "Trabalho Feito por Diego Buzo Prado - Engenharia de Software")

# Salvar o PDF

pdf.output("Atividade_Tabelas_Verdade.pdf")

"PDF gerado com sucesso: 'Atividade_Tabelas_Verdade.pdf'"
