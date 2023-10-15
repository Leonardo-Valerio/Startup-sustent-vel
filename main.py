from funcoes import *
result = 0
interacao = 0
cadastro = []
login = {}
menuCadastro = ['CADASTRAR', 'LOGAR', 'ENTRAR SEM LOGIN']
exibir(menuCadastro)
escolha = lerInt('digite o número da opção que deseja: ')
while True:
    if escolha == 1:
        cabecalho('CADASTRO')
        cadastrar(cadastro, login)
    elif escolha == 2:
        cabecalho('LOGIN')
        liberarUsuario = validarLogin(cadastro)
        if liberarUsuario:
            break
    elif escolha == 3:
        cabecalho('ENTRANDO SEM LOGIN')
        break
    else:
        linha()
        exibir(menuCadastro)
        linha()
        print('O número tem que ser de acordo com as opções listadas acima')
    linha()
    exibir(menuCadastro)
    linha()
    escolha = lerInt('digite o número da opção que deseja: ')
cabecalho('DASHBOARD')
dashboard = ['CALCULAR PREÇO MÉDIA DE LIXO POR KG','CALCULO MÉDIO DE ECONOMIA DE CO2 POR KG','CALCULAR PONTOS A RECEBER POR KG RECICLADOS','SAIR']
exibir(dashboard)
linha()
opcao = lerInt('digite a opção desejada: ')
while True:
    if opcao == 1:
        cabecalho(dashboard[0])
        print('Aqui você consegue calcular em média o quanto que \n'
              'uma sucata pagaria no seu lixo, dessa forma todos\n'
              'ganham, você, a sucata e principalmente o meio ambiente!\n'
              'basta você digitar o subtipo do material que deseja descartar\n'
              'e o peso dele, assim calcularemos com base no preço médio\n'
              'que as sucatas pagam no Brasil por cda material por Kg')
        linha()
        carregar()
        resultado = 0
        while True:
            materiais = {'plastico': {'pet': 0.20,'pvc': 0.10, 'polipropileno': 0.10},
                        'vidro' : {'vidro claro': 0.20,'vidro colorido': 0.10},
                        'papel': {'papelão': 0.05,'papel':0.03},
                        'metais': {'alumínio': 1,'cobre': 3,'ferro': 2},
                        'eletronicos': {'placas mães': 5, 'placas de circuito': 4 , 'baterias de lítio': 3}}
            exibirDicionario(materiais)
            subtipo = validarEscolhaDoSubtipo(materiais)
            kg = lerInt('digite a média do peso desse material:(Números inteiro em Kg)  ')
            resultado+= calcularValor(subtipo,kg,materiais)
            continuar = validarContinuar('deseaja adicionar mais um material para descartar? (1 para sim, 2 para não) ')
            if continuar == 2:
                cabecalho(f'VOCÊ RECEBERIA EM MÉDIA: R${resultado:.2f}')
                break
    elif opcao == 2:
        dados = {
            'árvores poupadas por ano' : 0.045,
            'minutos de voo por passageiro em um avião': 0.66,
            'dias de consumo de eletricidade em uma casa média': 0.0625,
            'horas de TV assistidas': 20,
            'km não dirigidos por um carro médio': 4.16,
            'garrafas de água de 500ml produzidas': 8.34,
            'dias de consumo de água por pessoa': 0.25,
            'Kg em quantidade de lixo em Aterros': 1,
            'Hamburgueres de carne economizadas': 0.28
        }
        materiais = {
                    'plastico': {'pet': 1.5, 'pvc': 2, 'polipropileno': 1.8},
                     'vidro': {'vidro claro': 0.3, 'vidro colorido': 0.27},
                     'papel': {'papelão': 1.1, 'papel': 1.7},
                     'metais': {'alumínio': 9, 'cobre': 4, 'ferro': 1.5},
                     'eletronicos': {'placas mães': 5, 'placas de circuito': 4, 'baterias de lítio': 3}
        }
        linha()
        print('Aqui você consegue calcular em média o quanto que \n'
              'você ou sua empresa estaria economizando em CO2\n'
              'para ajudar a salvar o planeta Terra!\n'
              'basta você digitar qual subtipo de material você deseja\n'
              'e o peso que você estaria reciclando ele')
        linha()
        carregar()
        resultado = 0
        while True:
            exibirDicionario(materiais)
            subtipo = validarEscolhaDoSubtipo(materiais)
            kg = lerInt('digite a média do peso desse material:(Números inteiro em Kg)  ')
            resultado += calcularValor(subtipo,kg,materiais)
            continuar = validarContinuar('deseja adicionar mais um material para reciclagem? (1 para sim, 2 para não) ')
            if continuar == 2:
                equivalente = exibirDicionarioDeEquivalencias(dados,resultado)
                cabecalho(f'{resultado:.2f}Kg ECONOMIZADOS DE C02, A NATUREZA AGRADECE!\n'
                          f'Curiosidade - {equivalente}')
                break

    elif opcao == 3:
        cabecalho(dashboard[2])
        print('Aqui você consegue calcular quantos pontos você ganhará \n'
              'de acordo com o que e quanto você está reciclando\n'
              'com esses pontos você terá alguns benefícios\n'
              'basta você digitar qual tipo de material você deseja\n'
              'e o peso que você irá reciclando ele\n')
        linha()
        carregar()
        if interacao == 0:
            result = 0

        while True:
            linha()
            materiais = {'plástico': 5,
                        'vidro': 7,
                        'papel': 3,
                        'metais': 10,
                        'eletrônicos': 20}
            exibirDicionarioDePontos(materiais)
            tipoMaterial = validarTipoDeMaterial(materiais)
            kg = lerInt('digite a média do peso desse material:(Números inteiro em Kg)  ')
            result += calcularPontos(tipoMaterial,kg,materiais)
            continuar = validarContinuar('deseaja adicionar mais um material para reciclagem? (1 para sim, 2 para não) ')

            if continuar == 2:
                cabecalho(f'TOTAL: {result:.2f}')
                converter = validarContinuar('deseja converter os pontos agora? (1 para sim, 2 para não) ')
                if converter == 1:
                    cabecalho(recompensas(result))
                    result = 0
                    interacao = 0
                else:
                    interacao+=1
                break


    elif opcao == 4:
        cabecalho('SAINDO...')
        break
    else:
        linha()
        exibir(dashboard)
        linha()
        print('O número tem que ser de acordo com as opções listadas acima')

    linha()
    exibir(dashboard)
    linha()
    opcao = lerInt('digite a opção desejada: ')
