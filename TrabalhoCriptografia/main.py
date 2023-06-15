def criptografar(palavra):
    
    palavra_invertida = palavra[::-1]
    
    numeros = []

    for letra in palavra_invertida:
        numero = ord(letra.lower()) - ord('a') + 1 + 10
        numeros.append(numero)

    return ' '.join(map(str, numeros))


def descriptografar(criptografada):

    numeros = criptografada.split()
    letras = []

    for numero in numeros:
        letra = chr(int(numero) + ord('a') - 1 - 10)
        letras.append(letra)

    palavra = ''.join(letras[::-1])
    
    return palavra

palavra_original = "banana"
print("Palavra Original:", palavra_original)
palavra_criptografada = criptografar(palavra_original)
print("Palavra criptografada:", palavra_criptografada)

palavra_descriptografada = descriptografar(palavra_criptografada)
print("Palavra descriptografada:", palavra_descriptografada)