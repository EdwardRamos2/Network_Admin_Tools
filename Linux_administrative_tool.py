#!/usr/bin/env python3
#Autor: Edward Ramos
#Date: 11/27/2016
#GNU/Linux administrative tool Version v2.2
import os , sys , subprocess
try:
    import nmap
except:
    sys.exit('[!] Install the nmap library: pip install python-nmap')
print(sys.version) # parentheses needed > python 3. 
print(sys.version_info)
if __name__ == '__main__':
    def MENU(): #MENU
        while True:
            print(" _   _      _                      _        _       _           _       ")
            print("| \ | | ___| |___      _____  _ __| | __   / \   __| |_ __ ___ (_)_ __  ")
            print("|  \| |/ _ \ __\ \ /\ / / _ \| '__| |/ /  / _ \ / _` | '_ ` _ \| | '_ \ ")
            print("| |\  |  __/ |_ \ V  V / (_) | |  |   <  / ___ \ (_| | | | | | | | | | |")
            print("|_| \_|\___|\__| \_/\_/ \___/|_|  |_|\_\/_/   \_\__,_|_| |_| |_|_|_| |_|")
            print("                                                                        ")
            print('\033[42;1;33m'+'(+) ManguePy_Admin_Redes v2.2\n'+ '\033[0;0m')
            print('---------------Escolha a opcao desejada!---------------------\n')
            print('\033[1;31m'+'(1) MOSTRAR USUARIOS CONECTADOS NO MOMENTO'+'\033[0;0m')
            print('\033[1;31m'+'(2) MOSTRAR OS LOGINS BEM-SUCEDIDOS NO SISTEMA'+'\033[0;0m')
            print('\033[1;31m'+'(3) MOSTRAR PROCESSOS CORRENTES DO SISTEMA'+'\033[0;0m')
            print('\033[1;31m'+'''(4) NETSTAT -> Mostrar os sockets abertos em um servidor,
               bem como tabelas de roteamento e informacoes de interfaces.'''+'\033[0;0m')
            print('\033[1;31m'+'(5) NMAP - (“Network Mapper”) '+'\033[0;0m')
            print('\033[1;31m'+'(6) EXIT'+'\033[0;0m')
            try:
                opcao = int(input('Digite numero da opcao: '))
            except:
                print('[!] Necessario informar uma opcao! EXEMPLO: 01')
                sys.exit('Saindo por falta de opcao!')
            def user_conectados():
                if opcao == 1:
                    print('(+) Usuarios Conectados no momento!')
                    usuarios = subprocess.call(['who']) #Who -> Mostra user conectados no momento em que o comando e executado
                    print(usuarios)
            def lastlog1():
                if opcao == 2:
                    print('Logins bem-sucedidos no sistema!')
                    logins_sucedidos = subprocess.call(['who'])
                    print(logins_sucedidos) #Mostra os logins bem-sucedidos no sistema operacional
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
                    try:
                        opcao_ps = input('Digite o numero da opcao: Exemplo: 01 ')
                    except:
                        print('[!] Necessario informar uma opcao! EXEMPLO: 01')
                        sys.exit('Saindo por falta de opcao!')
                    if opcao_ps == '01':
                        print('Processos correntes')
                        ps_pro = subprocess.call(['ps'])
                        print(ps_pro) #Mostra os processos correntes do sistema operacional.
                    elif opcao_ps == '02':
                        print('Mostrando todos os processos, inclusive os nao associados a um terminal.')
                        ps_pro1 = subprocess.call(['ps', '-e']) #Mostra todos os processos, inclusive os nao associados a um terminal (daemon).
                        print(ps_pro1)
                    elif opcao_ps == '03':
                        print('Mostrando saida formatada, com todos os atributos dos processos')
                        ps_pro2 = subprocess.call(['ps','-f'])
                        print(ps_pro2) #Formata a saida com todos os atributos dos processos.
                    elif opcao_ps == '04':
                        print('Mostrando todos os processos.')
                        ps_pro3 = subprocess.call(['ps','-a']) #Mostra todos os processos.
                        print(ps_pro3)
                    elif opcao_ps == '05':
                        print('Mostrando o usuario que iniciou o processo.')
                        ps_pro4 = subprocess.call(['ps','-u']) #Mostra o usuario que iniciou o processo.
                        print(ps_pro4)
                    elif opcao_ps == '06':
                        print('Mostrando todos os processos associados a um terminal.')
                        ps_pro5 = subprocess.call(['ps','x']) #Mostra todos os processos associados a um terminal.
                        print(ps_pro5)
                    elif opcao_ps == '07':
                        print('Mostrando todos os processos juntos com os nao associados, com saida formatada.')
                        ps_pro6 = subprocess.call(['ps','-ef']) #Mostra todos os processos juntos com os nao associados, com saida formatada.
                        print(ps_pro6)
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
                    print('(10) netstat -ntlup -> Extra')
                    try:
                        opcao_netstat = input('Digite o numero da opcao: Exemplo > 01:  ')
                    except:
                        print('[!] Necessario informar uma opcao! EXEMPLO: 01')
                        sys.exit('Saindo por falta de opcao!')
                    if opcao_netstat == '01':
                        print('(01) netstat  -> Mostrando sockets abertos, tabelas de roteamentos e informacoes de interfaces.')
                        net_pro1 = subprocess.call(['netstat']) #NETSTAT -> Mostrar os sockets abertos em um servidor,
                        print(net_pro1)                     #bem como tabelas de roteamento e informacoes de interfaces.
                    elif opcao_netstat == '02':
                        print('(+) Mostrando tabelas de roteamento do kernel.')
                        net_pro2 = subprocess.call(['netstat','-r']) #netstat -r   -> Mostra tabelas de roteamentos do kernel
                        print(net_pro2)
                    elif opcao_netstat == '03':
                        print('(+) Mostrando todas interfaces de rede do servidor')
                        net_pro3 = subprocess.call(['netstat','-i']) #Mostra todas as interfaces de rede do servidor.
                        print(net_pro3)
                    elif opcao_netstat == '04':
                        print('Mostrando estatisticas para cada protocolo de rede.')
                        net_pro4 = subprocess.call(['netstat','-s']) #Mostra estatisticas para cada protocolo de rede.
                        print(net_pro4)
                    elif opcao_netstat == '05':
                        print('Mostrando sockets em modo listening (portas abertas)')
                        net_pro5 = subprocess.call(['netstat','-l']) #Mostra sockets em modo listenig(portas abertas)
                        print(net_pro5)
                    elif opcao_netstat == '06':
                        print('Mostrando todas as conexoes TCP.')
                        net_pro6 = subprocess.call(['netstat','-t']) #Mostra todas as conexoes TCP
                        print(net_pro6)
                    elif opcao_netstat == '07':
                        print('Mostrando toda as conexoes UDP.')
                        net_pro7 = subprocess.call(['netstat','-u']) #Mostra toda as conexoes UDP
                        print(net_pro7)
                    elif opcao_netstat == '08':
                        print('Mostrando o processo que abriu a conexao.')
                        net_pro8 = subprocess.call(['netstat','-p']) #Mostra o processo que abriu a conexao
                        print(net_pro8)
                    elif opcao_netstat == '09':
                        print('Nao faz resolucao de DNS nas conexoes.')
                        net_pro9 = subprocess.call(['netstat','-n'])  #Nao faz resolucao DNS nas conexoes
                        print(net_pro9)
                    elif opcao_netstat == '10':
                        print('Extra')
                        net_pro10 = subprocess.call(['netstat','-ntlup']) #Extra
                        print(net_pro10)
            def nmap_scan():
                if opcao == 5:
                    print('Técnicas de verificação básica: ')
                    print('(01) Scan um objetivo                   ->  nmap [target]')
                    print('(02) Scan de múltiplos objetivos        ->  nmap [target1,target2,etc]')
                    print('(03) Scan em uma lista de objetivos     –>  nmap-IL [list.txt]')
                    print('(04) Scan uma variedade de hospedeiros  –>  nmap [range of IP addresses]')
                    print('(05) Realizar uma exploração agressiva  –>  nmap -A [target]')
            def sair():
                if opcao == 6:
                    sys.exit('Saindo do programa')
            sair()
            user_conectados()
            lastlog1()
            mostrarprocessos()
            netstat2()
            nmap_scan()
    MENU()
