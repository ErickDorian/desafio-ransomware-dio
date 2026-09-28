import os
import pyaes

arquivo_cript = "teste.txt.ransomwaretroll"
chave = b"testeransomwares"

if not os.path.exists(arquivo_cript):
    print(f"Arquivo não encontrado: {arquivo_cript}")
    exit(1)

with open(arquivo_cript, "rb") as f:
    dados_cript = f.read()

aes = pyaes.AESModeOfOperationCTR(chave)
dados_originais = aes.decrypt(dados_cript)

os.remove(arquivo_cript)

with open("teste.txt", "wb") as f:
    f.write(dados_originais)

print("Arquivo restaurado: teste.txt")

if os.path.exists("teste.txt.backup"):
    os.remove("teste.txt.backup")
    print("Backup removido")