# Drayan Silva Magalhães, João Vitor Zambão, Lucas Gabriel Nunes Geremias, Lucca Lucchin de Campos Costa 

import os
from lexical import *
from parser_ll import ParserLL1

# Declaração de função pra análise
def analisar_expressao(exp:str):
    tokens = analisador_lexico_mef(exp)
    if isinstance(tokens, str):  # erro léxico
        return "inválida"
    
    parser = ParserLL1(tokens)
    resultado = parser.parser_ll1()
 
    if resultado[:4] == "Erro":
        return "inválida"
    else:
        return "válida" 

def get_all_filepaths(path: str) -> list:
    """
    Retorna uma lista com todos os caminhos de arquivos contidos no diretório especificado
    e seus subdiretórios.
    
    Args:
        path: Caminho do diretório a ser explorado.
        
    Returns:
        Lista de strings com os caminhos completos para cada arquivo encontrado.
    """
    file_paths = []
    
    for root, _, files in os.walk(path):
        for file in files:
            full_path = os.path.join(root, file)
            file_paths.append(full_path)
    
    return file_paths


def parse_all_files(uploaded:str) -> None:
  uploaded_keys:list = get_all_filepaths(uploaded)

  for fname in uploaded_keys:
    with open(fname, 'r', encoding='utf-8') as f:
      content = f.readlines()
      num:int = int(str(content[0]).strip())
      acc:int = 0
    #   print(f"--- START FILE `{fname}` ---")
    #   print(f"File contains {num} expressions.")

      content = content[1:]

    #   print(f"---")
    #   print(f"[ PARSING ]:\n")
      for line in content:
        if acc == num:
          break
        line = line.strip()
        resultado = analisar_expressao(line)
        print(f"{resultado}")
        acc += 1

    #   print(f"\n--- EOF {fname} ---")

def parse_file(file:str) -> None:
  with open(file, 'r', encoding='utf-8') as f:
    content = f.readlines()
    num:int = int(str(content[0]).strip())
    acc:int = 0
  #   print(f"--- START FILE `{file}` ---")
  #   print(f"File contains {num} expressions.")

    content = content[1:]

  #   print(f"---")
  #   print(f"[ PARSING ]:\n")
    for line in content:
      if acc == num:
        break
      line = line.strip()
      resultado = analisar_expressao(line)
      print(f"{resultado}")
      acc += 1

  #   print(f"\n--- EOF {file} ---")