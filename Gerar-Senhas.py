import secrets
import string

def gerar_senha(tamanho=20):

    letras = string.ascii_letters #Letras do alfabeto
    numeros = string.digits #Números
    caracteres = string.punctuation #Caracteres especiais
    pool = letras + numeros + caracteres
    while True:
        senha = "".join(secrets.choice(pool) for i in range(tamanho))

        tem_letras = any(c.isupper() for c in senha)
        tem_numeros = any(c.isdigit() for c in senha)
        tem_caracteres = any(c in caracteres for c in senha)

        if tem_letras and tem_numeros and tem_caracteres:
            return senha
if __name__ == '__main__':
    print(f"Sua chave mestra: {gerar_senha()}")
