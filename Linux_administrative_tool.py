#!/usr/bin/env python3
#Auto: Edward Ramos
#Date: 11/27/2016
#GNU/Linux administrative tool Version v2.0
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
        print('''(4) NETSTAT -> Mostrar os sockets abertos em um servidor,
               bem como tabelas de roteamento e informacoes de interfaces.''')
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
        def netstat2():
            if opcao == 4:
                print('(+) NETSTAT')
                print('(MENU - PRINCIPAIS OPCOES:)')
                print('(01) netstat      -> Mostrando sockets abertos, tabelas de roteamentos e infor de interfaces.')
                print('(02) netstat -r   -> Mostra tabelas de roteamentos do kernel.')
                print('(03) netstat -i   -> Mostra todas as interfaces de rede do servidor.')
                print('(04) netstat -s   -> Mostra estatisticas de cada protocolo de rede.')
                print('(05) netstat -l   -> Mostra sockets em modo listening (portas abertas)')
                print('(06) netstat -t   -> Mostra todas as conexoes TCP.')
                print('(07) netstat -u   -> Mostra todas as oonexoes UDP.')
                print('(08) netstat -p   -> Mostra o processo que abriu a conexao.')
                print('(09) netstat -n   -> Nao faz resolucao de DNS nas conexoes.')
                opcao_netstat = input('Digite o numero da opcao: Exemplo > 01:  ')
                if opcao_netstat == '01':
                    print('(01) netstat  -> Mostrando sockets abertos, tabelas de roteamentos e informacoes de interfaces.')
                    os.system('netstat') #NETSTAT -> Mostrar os sockets abertos em um servidor,
                                         #bem como tabelas de roteamento e informacoes de interfaces.
                elif opcao_netstat == '02':
                    print('(+) Mostrando tabelas de roteamento do kernel.')
                    os.system('netstat -r') #netstat -r   -> Mostra tabelas de roteamentos do kernel
                elif opcao_netstat == '03':
                    print('(+) Mostrando todas interfaces de rede do servidor')
                    os.system('netstat -i') #Mostra todas as interfaces de rede do servidor.
                elif opcao_netstat == '04':
                    print('Mostrando estatisticas para cada protocolo de rede.')
                    os.system('netstat -s') #Mostra estatisticas para cada protocolo de rede.
                elif opcao_netstat == '05':
                    print('Mostrando sockets em modo listening (portas abertas)')
                    os.system('netstat -l') #Mostra sockets em modo listenig(portas abertas)
                elif opcao_netstat == '06':
                    print('Mostrando todas as conexoes TCP.')
                    os.system('netstat -t') #Mostra todas as conexoes TCP
                elif opcao_netstat == '07':
                    print('Mostrando toda as conexoes UDP.')
                    os.system('netstat -u') #Mostra toda as conexoes UDP
                elif opcao_netstat == '08':
                    print('Mostrando o processo que abriu a conexao.')
                    os.system('netstat -p') #Mostra o processo que abriu a conexao
                elif opcao_netstat == '09':
                    print('Nao faz resolucao de DNS nas conexoes.')
                    if __name__ == '__main__':
                        os.system('netstat -n') #Nao faz resolucao DNS nas conexoes
        netstat2()

        def sair():
            if opcao == 5:
                sys.exit('Saindo do programa')
        sair()

    MENU()
