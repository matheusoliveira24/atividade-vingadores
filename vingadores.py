import os
import time
import enum

class Vingador:
    lista_vingadores = []
    lista_poderes = [
        ""
    ]
    
    class categoria_vingadores:
        HUMANO = "Humano"
        META_HUMANO = "Meta-humano"
        ALIENIGENA = "Alienígena"
        DEUS = "Deus"
        ANDROIDE = "Androide"
    
    def __init__(self, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_de_forca):
        self.nome_heroi = nome_heroi
        self.nome_real = nome_real
        self.categoria = categoria
        self.poderes = poderes
        self.poder_principal = poder_principal
        self.fraquezas = fraquezas
        self.nivel_de_forca = nivel_de_forca
        self.convocado = False
        self.tornozeleira = False
        self.chip_gps = False
        
        # Adicionar automaticamente à lista de Vingadores
        Vingador.lista_vingadores.append(self)

    def __str__(self):
        return f'{self.nome_heroi.ljust(20)} | {self.nome_real.ljust(20)} | {self.categoria.ljust(20)} | ' \
               f'{"Convocado" if self.convocado else "Não Convocado".ljust(20)} | ' \
               f'{"Tornozeleira Aplicada" if self.tornozeleira else "Sem Tornozeleira".ljust(20)} | ' \
               f'{"Chip GPS Aplicado" if self.chip_gps else "Sem Chip GPS".ljust(20)}'


class Interface():
    animacao = True

    @staticmethod
    def animacaoLinhas(testiculo, duracao):
        for ch in testiculo:
            time.sleep(duracao)
            print(ch, end="", flush=True)

    @staticmethod
    def menu():
        if Interface.animacao == True:
            Interface.animacaoLinhas(''' 

████████╗██╗░░██╗███████╗  ██╗░░░░░███████╗░██████╗░███████╗███╗░░██╗██████╗░░█████╗░██████╗░██╗░░░██╗
╚══██╔══╝██║░░██║██╔════╝  ██║░░░░░██╔════╝██╔════╝░██╔════╝████╗░██║██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝
░░░██║░░░███████║█████╗░░  ██║░░░░░█████╗░░██║░░██╗░█████╗░░██╔██╗██║██║░░██║███████║██████╔╝░╚████╔╝░
░░░██║░░░██╔══██║██╔══╝░░  ██║░░░░░██╔══╝░░██║░░╚██╗██╔══╝░░██║╚████║██║░░██║██╔══██║██╔══██╗░░╚██╔╝░░
░░░██║░░░██║░░██║███████╗  ███████╗███████╗╚██████╔╝███████╗██║░╚███║██████╔╝██║░░██║██║░░██║░░░██║░░░
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚══════╝╚══════╝░╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░

            ░█████╗░██╗░░░██╗███████╗███╗░░██╗░██████╗░███████╗██████╗░░██████╗
            ██╔══██╗██║░░░██║██╔════╝████╗░██║██╔════╝░██╔════╝██╔══██╗██╔════╝
            ███████║╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██╗░█████╗░░██████╔╝╚█████╗░
            ██╔══██║░╚████╔╝░██╔══╝░░██║╚████║██║░░╚██╗██╔══╝░░██╔══██╗░╚═══██╗
            ██║░░██║░░╚██╔╝░░███████╗██║░╚███║╚██████╔╝███████╗██║░░██║██████╔╝
            ╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═════╝░
''', 0.01)

        Interface.animacao = False
        print('\n')
        print('Seja bem-viado! Escolha uma das opções abaixo\n')
        print('1. Cadastrar vingador')
        print('2. Ver lista de vingadores ')
        print('3. Convocar vingador')
        print('4. Aplicar tornozeleira')
        print('5. Aplicar chip GPS')
        print('6. Emitir mandado de prisão')
        print('7. Sair')
        Interface.ler_opcao_usuario(Interface.Cadastro, Interface.listar_vingadores, Interface.convocar_vingador, 
                                     Interface.aplicar_tornozeleira, Interface.aplicar_chip_gps, Interface.emitir_mandado, Interface.sair)

    @staticmethod
    def VoltarMenu():
        input("\nPressione Enter para voltar ao menu...")
        os.system("cls")
        Interface.menu()

    @staticmethod
    def Cadastro():
        nome_heroi = input('Nome do herói: ')
        nome_real = input('Nome real: ')
        categoria = input('Categoria (Humano, Meta-humano, Androide, Deidade, Alienígena): ')

        if categoria not in [Vingador.categoria_vingadores.HUMANO, Vingador.categoria_vingadores.META_HUMANO, 
                             Vingador.categoria_vingadores.ANDROIDE, Vingador.categoria_vingadores.DEUS, 
                             Vingador.categoria_vingadores.ALIENIGENA]:
            print("Categoria inválida! Tente novamente.")
            Interface.Cadastro()
            return

        poderes = input('Poderes (separados por vírgula): ').split(",")
        poder_principal = input('Poder principal: ')
        fraquezas = input('Fraquezas (separadas por vírgula): ').split(",")
        nivel_forca = int(input('Nível de força (0 a 10000): '))

        if nivel_forca < 0 or nivel_forca > 10000:
            print("Nível de força inválido!")
            Interface.Cadastro()
            return
        
        vingador = Vingador(nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca)
        Vingador.lista_vingadores.append(vingador)
        print(f'Vingador {nome_heroi} cadastrado com sucesso!')
        Interface.VoltarMenu()

    @staticmethod
    def listar_vingadores():
        if not Vingador.lista_vingadores:
            print("Nenhum vingador cadastrado.")
        else:
            print(f'{"Nome do Herói".ljust(20)} | {"Nome Real".ljust(20)} | {"Categoria".ljust(20)} | '
                  f'{"Convocado".ljust(20)} | {"Tornozeleira".ljust(20)} | {"Chip GPS".ljust(20)}')
            for vingador in Vingador.lista_vingadores:
                print(vingador)
            Interface.VoltarMenu()

    @staticmethod
    def convocar_vingador():
        nome = input("Digite o nome do herói ou nome real do vingador para convocar: ")
        vingador_encontrado = None
        for vingador in Vingador.lista_vingadores:
            if vingador.nome_heroi.lower() == nome.lower() or vingador.nome_real.lower() == nome.lower():
                vingador_encontrado = vingador
                break
        if vingador_encontrado:
            vingador_encontrado.convocado = True
            print(f'{vingador_encontrado.nome_heroi} foi convocado com sucesso!')
        else:
            print("Vingador não encontrado.")
        Interface.VoltarMenu()

    @staticmethod
    def aplicar_tornozeleira():
        nome = input("Digite o nome do herói ou nome real do vingador para aplicar a tornozeleira: ")
        vingador_encontrado = None
        for vingador in Vingador.lista_vingadores:
            if vingador.nome_heroi.lower() == nome.lower() or vingador.nome_real.lower() == nome.lower():
                vingador_encontrado = vingador
                break
        if vingador_encontrado:
            if not vingador_encontrado.convocado:
                print(f"{vingador_encontrado.nome_heroi} precisa ser convocado antes de aplicar a tornozeleira!")
            else:
                vingador_encontrado.tornozeleira = True
                if vingador_encontrado.nome_heroi.lower() == "thor" or vingador_encontrado.nome_heroi.lower() == "hulk":
                    print(f"{vingador_encontrado.nome_heroi} resiste à tornozeleira!")
                else:
                    print(f"Tornozeleira aplicada em {vingador_encontrado.nome_heroi}.")
        else:
            print("Vingador não encontrado.")
        Interface.VoltarMenu()

    @staticmethod
    def aplicar_chip_gps():
        nome = input("Digite o nome do herói ou nome real do vingador para aplicar o chip GPS: ")
        vingador_encontrado = None
        for vingador in Vingador.lista_vingadores:
            if vingador.nome_heroi.lower() == nome.lower() or vingador.nome_real.lower() == nome.lower():
                vingador_encontrado = vingador
                break
        if vingador_encontrado:
            if not vingador_encontrado.tornozeleira:
                print(f"A tornozeleira precisa ser aplicada em {vingador_encontrado.nome_heroi} antes do chip GPS!")
            else:
                vingador_encontrado.chip_gps = True
                print(f"Chip GPS aplicado em {vingador_encontrado.nome_heroi}.")
        else:
            print("Vingador não encontrado.")
        Interface.VoltarMenu()

    @staticmethod
    def emitir_mandado():
        nome = input("Digite o nome do herói ou nome real do vingador para emitir mandado: ")
        vingador_encontrado = None
        for vingador in Vingador.lista_vingadores:
            if vingador.nome_heroi.lower() == nome.lower() or vingador.nome_real.lower() == nome.lower():
                vingador_encontrado = vingador
                break
        if vingador_encontrado:
            print(f"Mandado de prisão emitido para {vingador_encontrado.nome_heroi}.")
        else:
            print("Vingador não encontrado.")
        Interface.VoltarMenu()

    @staticmethod
    def sair():
        print("Encerrando o programa...")
        time.sleep(1)
        exit()

    @staticmethod
    def ler_opcao_usuario(*metodos):
        opcao = input("\nDigite aqui: ")
        os.system('cls')
        try:
            if opcao.isdigit() and 1 <= int(opcao) <= len(metodos):
                metodos[int(opcao) - 1]()
            else:
                print("Opção inválida. Tente novamente.")
                Interface.VoltarMenu()
        except:
            print("Opção inválida. Tente novamente.")
            Interface.VoltarMenu()
            
