def conta_palavras_unicas(frase):
    palavras = frase.lower().split()
    quantidade_palavras_unicas = len(set(palavras))
    return quantidade_palavras_unicas

# Teste a sua função aqui (caso ache necessário)
frase = "banana maçã maçã maçã maçã maçã maçã maçã maçã maçã maçã maçã maçã maçã"
resultado = conta_palavras_unicas(frase)

print("Palavras únicas:", resultado)












