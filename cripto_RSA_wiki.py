# Esse código em python foi criado utilizando como base o código em java
# dessa página: https://pt.wikipedia.org/wiki/RSA_(sistema_criptogr%C3%A1fico)
# Alguns dos métodos em java não existiam em python e por isso foram implementados.

# Aqui esta pedindo para o usuario digitar a frase que será usada para ser criptografada
msg = input("Digite a mensagem para ser cifrada: ")

# As variaveis  "p" e "q" estão recebendo dois valores primos. Esses valores são desse tamanho porque
# quando estava traduzindo o código para python percebi que o algoritmo da página só funcionava com numeros primos muito grande.
# E esses números primos foram gerados utilizando um método do proprio java.
# a probabildade de se gerar esses dois valores novamente e quase zero,  o codigo da pagina do wiki por ser numeros muito grande
p = 164135779097971035236649394475230357278124915621463293023273902303843044950480319453250999410547280560670263768266230090357428490127143984896307355671461126842835184246788114540659957680623493680565155659511124829731008615236795830881171750793725202846786842109262329001165158003382102429709172276498886649237
q = 165389069375624129124577679709984943001855396081760280865108442322540011434157863851597806985830199973407482928708466843496515818984177087383252332296569666141995823588509348478221423227524702243540578982478075990264543614670612433554095388893676099391497610075467259800940201232785702162863296854607662897521


# Aqui foi implementado um método que descobre o maior divisor comum entre dois números.

def computeGCD(x, y):
    if x > y:
        small = y
    else:
        small = x

    for i in range(1, small+1):
        if((x % i == 0) and (y % i == 0)):
            resu = i

    return resu

# isso faz parte do algoritimo
# Compute a função totiente phi(n) = (p -1) (q -1)


def totientePhi():
    return (p - 1) * (q - 1)

# utilizado para encontrar os valores que são primos entre si
# isso faz parte do algoritimo.
# Escolha um inteiro  "e"  , 1 < "e" < phi(n) ,  "e" e phi(n) sejam primos entre si.

def primosEntreSi(m):
    e = 3
    while computeGCD(e, m) > 1:
        e += 2
    return e

# Esse método foi implementado para fazer o mod inverso isso foi encontrado na internet
def modInverse(a, m):
    m0 = m
    y = 0
    x = 1

    if (m == 1):
        return 0

    while (a > 1):

        # q é quociente

        q = a // m
        t = m
        # m é resto agora, processo # igual ao algoritmo de Euclides
        m = a % m
        a = t
        t = y

        # Atualiza x e y
        y = x - q * y
        x = t

    # Torna x positivo
    if (x < 0):
        x = x + m0

    return x


n = p * q  # isso faz parte do algoritimo
m = totientePhi() # utilização da Função totiente de Euler
e = primosEntreSi(m) # tira os primos entre eles
d = modInverse(e, m) # faz o mod inverso

# exibe os valores na tela
print("p: {}".format(p))  # valor primo
print("q: {}".format(q))  # valor primo
# Utilizado em conjunto com as chaves publica e privada
print("n: {}".format(n))
print("e: {}".format(e))  # A chave pública: o par (n,e)
print("d: {}".format(d))  # chave privada: a tripla (p,q,d)

# Converte numero decimal em um valor binario exemplo: (exemplo: 198 -> 11000110)
def getBinaryOfNumber(vlr):
    return "{0:08b}".format(vlr)


print("\n\n")

# mensagem cifrada - RSA_encrypt()
def mensagemCigrada():
    # Esta convertendo o texto para uma lista de valores da tabela ascii
    # e convertendo os valores numericos para suas forma binarias (exemplo: 198 -> 11000110)
    # Após isso todos os valores da lista são unidos formando um unico valor binario(exemplo: 198 -> 11000110; 153 -> 10011001; FICA: 1100011011000110)
    # Após isso o valor binario é convertido para o seu equivalente do tipo decimal. (exmp: 1100011011000110 -> 50886 )
    decimalFromBinary = int(
        "".join([getBinaryOfNumber(ord(l)) for l in msg]), 2)

    # Aqui foi  utilizando o método proprio do python para fazer a exponenciação de um numero e
    # tirar o mod do valor. Como os valores eram extremamente grandes não foi possivel utilizar um método implementado por conta propria.
    # Faz parte do algoritimo para encriptografar
    msgcifrada = pow(decimalFromBinary, e, n)

    return msgcifrada


msgCifrada = mensagemCigrada()
print("\n\n")


print("Mensagem  Cifrada: {}".format(msgCifrada))

# mensagem decifrada - RSA_encrypt()
def mensagemDecifrada():
    # Faz parte do algoritimo para desincriptografar, 
    msgdecifrada = pow(msgCifrada, d, n)

    # Aqui está convertendo um valor decimal para a sua forma binaria.
    binaryFromDecimal = "{0:08b}".format(msgdecifrada)

    # aqui está verificando se tamanho do número é divisivel por 8. Caso não seja é adicionado
    # 0 no inicio do número até que ele seja divisivel por 8

    while len(binaryFromDecimal) % 8 != 0:
        binaryFromDecimal = "0{}".format(binaryFromDecimal)

    # Aqui está quebrando a string em blocos de 8 em um array onde cada posição tem uma string de 0 e 1 referente a um caractere.
    # Esse valor 8 é equivalente a 1 byte de 8 bits.
    # Exemplo (01000001 -> 65)
    arraDeBits = [int(binaryFromDecimal[i*8:8*(i+1)], 2)
                  for i, _ in enumerate(range(int(len(binaryFromDecimal)/8)))]

    # Aqui está exibindo cada valor referente da tabela ASCII
    print("Valores da tabela ASCII:", arraDeBits)

    # Aqui está convertendo cada valor numerico da tabela ASCII para sua forma de caracteres, unindo um array de strings.
    resu = "".join([chr(caractere) for caractere in arraDeBits])

    return resu


msgdecifrada = mensagemDecifrada()

print("Mensagem Decifrada: {}".format(msgdecifrada))



