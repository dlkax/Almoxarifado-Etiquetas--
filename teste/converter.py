import re

with open("dados_brutos.txt", encoding="utf-8") as f:
    linhas = f.readlines()

saida = []
ignoradas = 0

for linha in linhas:
    linha = linha.strip()
    if not linha:
        continue

    # Remove parênteses, aspas, vírgulas finais
    limpa = linha.replace("(", "").replace(")", "").replace('"', "").replace("'", "").rstrip(",")

    # Divide por vírgula, tab ou múltiplos espaços
    partes = re.split(r'[,\t]| {2,}', limpa, maxsplit=1)

    if len(partes) == 2:
        codigo = partes[0].strip()
        descricao = partes[1].strip()
        if codigo and descricao:
            saida.append(f'("{codigo}","{descricao}"),')
        else:
            ignoradas += 1
    else:
        ignoradas += 1

with open("dados_convertidos.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(saida))

print(f"{len(saida)} registros convertidos.")
print(f"{ignoradas} linhas ignoradas.")
