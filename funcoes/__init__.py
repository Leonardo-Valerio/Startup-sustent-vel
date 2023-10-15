from time import sleep
import random
def linha():
    print('-' * 100)

def cabecalho(msg):
    linha()
    print(msg.center(100))
    linha()

def exibir(listagem):
    for i in range(len(listagem)):
        print(f'{i+1} - {listagem[i]}')

def lerInt(msg):
    while True:
        num = input(msg)
        if num.isnumeric():
            valor = int(num)
            return valor
        else:
            print('ERRO, digite um número válido!')
def validarStr(txt):
    while True:
        str = input(txt)
        if len(str) < 3:
            print('ERRO, preencha esse campo com pelo menos 3 caracteres')
        else:
            return str
def validaUsario(txt):
    while True:
        str = validarStr(txt)
        if str.isalpha():
            return str
        else:
            print('erro, tem que haver letras nesse campo')



def cadastrar(cadastro,login):
    while True:
        usuarioExiste = False
        usuarioNovo = validaUsario('crie um nome do seu usario: ').lower()
        for i in cadastro:
            if i['usuario'] == usuarioNovo:
                usuarioExiste = True
        if usuarioExiste:
            print('ERRO! Nome de usuario já existente!')
        else:
            login['usuario'] = usuarioNovo
            login['senha'] = validarStr('crie sua senha: ').lower()
            cadastro.append(login.copy())
            cabecalho('cadastro efetuado com sucesso!')
            break


def validarLogin(cadastro):
    if len(cadastro) > 0:
        while True:
            usuario = validaUsario('digite seu usario: ').lower()
            senha = validarStr('digite sua senha: ').lower()
            for i in cadastro:
                if usuario == i['usuario'] and senha == i['senha']:
                    cabecalho(f'bem-vindo {i["usuario"]}!')
                    liberarUsuario = True
                    return liberarUsuario
            print('usuario ou senha invalidos, digite novamente')
    else:
        print('nenhum cadastro feito ainda, vá na opção 1 e realize um cadastro')
        liberarUsuario = False
        return liberarUsuario

def validarContinuar(msg):
    num = lerInt(msg)
    while num != 1 and num != 2:
        print('erro, digite um número entre 1 e 2')
        num = lerInt(msg)
    return num
def exibirDicionario(dicionario):
    for tipoMaterial,subtipos in dicionario.items():
        cabecalho(f'Material - {tipoMaterial}')
        for subtipo in subtipos.items():
            print(f'Subtipo - {subtipo[0]}')


def validarEscolhaDoSubtipo(dicionario):
    while True:
        linha()
        subtipo = input('digite o subtipo que deseja calcular: ').lower()
        for tiposMaterial,subtipos in dicionario.items():
            for i in subtipos.items():
                if i[0] == subtipo:
                    return subtipo
        print('ERRO, subtipo não encontrado! (não se esqueça da acentuação)')
def calcularValor(subtipo,kg,dicionario):
    for tipoMaterial, subtipos in dicionario.items():
        for i,valor in subtipos.items():
            if i == subtipo:
                multiplicacao = kg * valor
                return multiplicacao

def exibirDicionarioDeEquivalencias(dicionario,kg):

        chaves = list(dicionario.keys())
        chave_aleatoria = random.choice(chaves)
        valor_aleatorio = dicionario[chave_aleatoria]

        return f'Isso equivale a {int(valor_aleatorio * kg)} de {chave_aleatoria}'


def exibirDicionarioDePontos(dicionario):
    for tipoMaterial in dicionario.items():
        print(f'Material - {tipoMaterial[0]}')


def validarTipoDeMaterial(dicionario):
    while True:
        linha()
        tipoMaterial = input('digite o tipo de material que deseja reciclar: ').lower()
        for i in dicionario.items():
            if i[0] == tipoMaterial:
                return tipoMaterial

        print(f'Erro! tipo de material não encontrado, (se atente à acentuação)')

def calcularPontos(tipoMaterial,kg,dicionario):
    for i in dicionario.items():
        if i[0] == tipoMaterial:
            multiplicacao = i[1] * kg
            return multiplicacao


def recompensas(pontos):
    beneficio = 'Com essa quantidades de pontos você ainda não tem benefícios :('
    if pontos >=50:
        beneficio = 'Parabéns! Você ganhou acesso à participar do nosso sorteio mensal que fazemos de produtos sustentáveis'
    if pontos >=100:
        desconto = (pontos * 3) / 100
        desconto = int(desconto)
        beneficio = f'Parabéns! Você ganhou um desconto de {desconto}% em lojas parceiras que vendem produtos sustentáveis'
    if pontos >= 500:
        doacao = (pontos*2) / 100
        beneficio = f'Parabéns! Com essa quantidade de pontos 1 árvore será plantada e será doado R${doacao} para a caridade'
    if pontos >= 1000:
        beneficio = f'Parabéns! Você ganhou um passe de um dia para andar de bicicleta, retire a bicicleta num posto \n' \
                    f'de itaú mais próximo'
    if pontos >= 1500:
        beneficio = f'Parabéns! Você ganhou 1 ingresso para um evento de sustentabilidade que fazemos todos os meses\n' \
                    f', e 2 árvores serão plantadas'
    if pontos >= 2000:
        beneficio = f'Parabéns Você ganhou um acesso de 1 mês do nosso pacote premium e 2 ingresso para um evento de\n' \
                    f'sustentabilidade que fazemos todos os meses, 3 árvores serão plantadas'
    return beneficio


def carregar():
    print("Carregando", end="")
    for i in range(4):
        sleep(1)
        print(".", end="")
    print()
