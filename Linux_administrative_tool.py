#!/usr/bin/env python3
#Auto: Edward Ramos
#Date: 11/27/2016
#GNU / Linux administrative tool Version v1.0
import os , sys
try:
    import nmap
except:
    sys.exit('[!] Install the nmap library: pip install python-nmap')

if __name__ == '__main__':
    def MENU(): #MENU
        print('(+) ManguePy_Admin_Redes v1.0\n')
        print('Escolha a opcao desejada!')
        print('(1) MOSTRAR USUARIOS CONECTADOS NO MOMENTO')
        print('(2) MOSTRAR OS LOGINS BEM-SUCEDIDOS NO SISTEMA')
        print('(3) MOSTRAR PROCESSOS CORRENTES DO SISTEMA')
        print('(5) EXIT')
        opcao = int(input('Digite numero da opcao: '))
        def user_conectados():
            if opcao == 1:
                print('(+) Usuarios Conectados no momento!')
                os.system('who') #Who -> Mostra user conectados no momento em que o comando e executado
        user_conectados()
        def lastlog1():
            if opcao == 2:
                print('Logins bem-sucedidos no sistema!')
                os.system('lastlog') #Mostra os logins bem-sucedidos no sistema operacional
        lastlog1()
        def mostrarprocessos():
            if opcao == 3:
                print('(+) Processos correntes do sistema!')
                print('(MENU PS - PRINCIPAIS OPCOES:)')
                print('(01) ps     -> Processos correntes')
                print('(02) ps -e  -> Mostra todos os processos, inclusive os nao associados a um terminal (daemon).')
                print('(03) ps -f  -> Formata a saida com todos os atributos dos processos.')
                print('(04) ps -a  -> Mostra todos os processos.')
                print('(05) ps -u  -> Mostra o usuario que iniciou o processo.')
                print('(06) ps -x  -> Mostra processos associados a um terminal')
                print('(07) ps -ef -> Mostra todos os processos juntos com os nao associados, com saida formatada.')
                opcao_ps = input('Digite o numero da opcao: Exemplo: 01 ')
                if opcao_ps == '01':
                    print('Processos correntes')
                    os.system('ps') #Mostra os processos correntes do sistema operacional.
                elif opcao_ps == '02':
                    print('Mostrando todos os processos, inclusive os nao associados a um terminal.')
                    os.system('ps -e') #Mostra todos os processos, inclusive os nao associados a um terminal (daemon).
                elif opcao_ps == '03':
                    print('Mostrando saida formatada, com todos os atributos dos processos')
                    os.system('ps -f') #Formata a saida com todos os atributos dos processos.
                elif opcao_ps == '04':
                    print('Mostrando todos os processos.')
                    os.system('ps -a') #Mostra todos os processos.
                elif opcao_ps == '05':
                    print('Mostrando o usuario que iniciou o processo.')
                    os.system('ps -u') #Mostra o usuario que iniciou o processo.
                elif opcao_ps == '06':
                    print('Mostrando todos os processos associados a um terminal.')
                    os.system('ps -x') #Mostra todos os processos associados a um terminal.
                elif opcao_ps == '07':
                    print('Mostrando todos os processos juntos com os nao associados, com saida formatada.')
                    os.system('ps -ef') #Mostra todos os processos juntos com os nao associados, com saida formatada.

        mostrarprocessos()
        def sair():
            if opcao == 5:
                sys.exit('Saindo do programa')
        sair()

    MENU()
