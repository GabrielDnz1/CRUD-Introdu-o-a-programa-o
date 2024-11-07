import os
import time
import json

def carregar_dados():
    if os.path.exists("registro.json") and os.path.getsize("registro.json") > 0:
        with open("registro.json", "r") as arquivo:
            try:
                return json.load(arquivo)
            except json.JSONDecodeError:
                limpar_console()
                print("Erro no Programa: O arquivo está corrompido!")
                time.sleep(3)
                return []
    else:
        return []

def limpar_console():
    os.system('cls' if os.name == 'nt' else 'clear') 

def verifica_se_usuario_esta_cadastrado(usuario):
    dados = carregar_dados()
    usuario_existe = any(isinstance(item, dict) and item.get("nome") == usuario 
                         for item in dados)
    return usuario_existe

def cadastrar_usuario(nome_usuario, senha_do_usuario):
    if not verifica_se_usuario_esta_cadastrado(nome_usuario):
        dados = carregar_dados()
        dados.append({"nome": nome_usuario, "senha": senha_do_usuario, "Planejamento": []})

        with open("registro.json", "w") as arquivo:
            json.dump(dados, arquivo, indent=4)

        limpar_console()
        print("Usuário cadastrado com sucesso.")
        time.sleep(3)
    else:
        limpar_console()
        print("Usuário já cadastrado, tente cadastrar outro nome de usuario.")
        time.sleep(3)

def validar_usuario(nome_usuario, senha):
    dados = carregar_dados()
    for usuario in dados:
        if nome_usuario == usuario.get("nome") and senha == usuario.get("senha"):
            return True
    return False

def menu_usuario(usuario):
    print("1 - Cadastrar atividade")
    print("2 - Alterar Atividade")
    print("3 - Excluir Atividade")
    print("4 - Verificar agenda por Prioridade")
    print("5 - Sair")
    opcao_escolhida = input("")

    if opcao_escolhida == "1":
        limpar_console()
        print("Digite a atividade que deseja cadastrar:")
        atividade = input("").strip()
        print("Digite a descrição da atividade:")
        descricao = input("").strip()
        print("Digite a prioridade da atividade (Alta, Media, Baixa):")
        prioridade = input("").strip()
        print("Digite a data de inicio da atividade (Exemplo: dd/mm/aaaa):")
        data_de_inicio = input("").strip()
        print("Digite a data de finalização da atividade (Exemplo: dd/mm/aaaa):")
        data_de_fim = input("").strip()
        print("Digite o horario da atividade (Exemplo: 12h30):")
        horario = input("").strip()
        limpar_console()

        dados = carregar_dados()
        for pessoa in dados:
            if pessoa.get("nome") == usuario:
                if not isinstance(pessoa["Planejamento"], list):
                    pessoa["Planejamento"] = []

                pessoa["Planejamento"].append({
                    "atividade": atividade,
                    "prioridade": prioridade,
                    "descricao": descricao,
                    "data_de_inicio": data_de_inicio,
                    "data_de_fim": data_de_fim,
                    "horario": horario
                })
                print("Atividade cadastrada com sucesso.")
                time.sleep(3)
                limpar_console()
                break

        with open("registro.json", "w") as arquivo:
            json.dump(dados, arquivo, indent=4)

    elif opcao_escolhida == "2":
        limpar_console()
        dados = carregar_dados()
        for pessoa in dados:
            if pessoa.get("nome") == usuario:
                planejamento = pessoa.get("Planejamento", [])
                if not isinstance(planejamento, list):
                    planejamento = []

                if not planejamento:
                    print("| Você não tem nenhuma atividade cadastrada! |")
                    time.sleep(3)
                    break
                print("| {:<3} | {:<24} | {:<24} | {:<12} | {:<14} | {:<12} | {:<8} |".format("ID", "Atividade", "Descricao", "Prioridade", "Data de Início", "Data de Fim", "Horário"))
                print("|" + "-" * 5 + "|" + "-" * 26 + "|" + "-" * 26 + "|" + "-" * 14 + "|" + "-" * 16 + "|" + "-" * 14 + "|" + "-" * 10 + "|")
                for i, atividade in enumerate(planejamento, start=1):
                    print("| {:<3} | {:<24} | {:<24} | {:<12} | {:<14} | {:<12} | {:<8} |".format(
                        i,
                        atividade["atividade"],
                        atividade["descricao"],
                        atividade["prioridade"],
                        atividade["data_de_inicio"],
                        atividade["data_de_fim"],
                        atividade["horario"]
                    ))
                print("")

                try:
                    numero_atividade = int(input("Digite o ID da atividade você deseja alterar? (Não insira nenhum valor e tecle Enter para voltar): ")) - 1
                except ValueError:
                    limpar_console()
                    print("Voltando ao Menu Principal.")
                    time.sleep(2)
                    limpar_console()
                    continue

                if 0 <= numero_atividade < len(planejamento):
                    print("Digite a nova atividade (deixe em branco para manter):")
                    nova_atividade = input("").strip()
                    print("Digite a nova prioridade (deixe em branco para manter):")
                    nova_prioridade = input("").strip()
                    print("Digite a nova data de inicio (deixe em branco para manter):")
                    nova_data_de_inicio = input("").strip()
                    print("Digite a nova data de fim (deixe em branco para manter):")
                    nova_data_de_fim = input("").strip()
                    print("Digite o novo horário (deixe em branco para manter):")
                    novo_horario = input("").strip()
                    limpar_console()

                    if nova_atividade:
                        planejamento[numero_atividade]["atividade"] = nova_atividade
                    if nova_prioridade:
                        planejamento[numero_atividade]["prioridade"] = nova_prioridade
                    if nova_data_de_inicio:
                        planejamento[numero_atividade]["data_de_inicio"] = nova_data_de_inicio
                    if nova_data_de_fim:
                        planejamento[numero_atividade]["data_de_inicio"] = nova_data_de_fim
                    if novo_horario:
                        planejamento[numero_atividade]["horario"] = novo_horario

                    pessoa["Planejamento"] = planejamento
                    with open("registro.json", "w") as arquivo:
                        json.dump(dados, arquivo, indent=4)

                    print("Atividade alterada com sucesso!")
                    time.sleep(3)
                    limpar_console()
                else:
                    print("Número de atividade inválido.")
                    time.sleep(3)
                    limpar_console()
                break

    elif opcao_escolhida == '3':
        limpar_console()
        dados = carregar_dados()
        for pessoa in dados:
            if pessoa.get("nome") == usuario:
                planejamento = pessoa.get("Planejamento", [])
                if not isinstance(planejamento, list):
                    planejamento = []

                if not planejamento:
                    print("| Você não tem nenhuma atividade cadastrada! |")
                    time.sleep(3)
                    break

                prioridade_ordem = {"Alta": 1, "Media": 2, "Baixa": 3}
                planejamento_ordenado = sorted(planejamento, key=lambda x: prioridade_ordem.get(x["prioridade"], 3))
                print("| {:<3} | {:<24} | {:<12} | {:<14} | {:<12} | {:<8} |".format("ID", "Atividade", "Prioridade", "Data de Início", "Data de Fim", "Horário"))
                print("|" + "-" * 5 + "|" + "-" * 26 + "|" + "-" * 14 + "|" + "-" * 16 + "|" + "-" * 14 + "|" + "-" * 10 + "|")
                for i, atividade in enumerate(planejamento_ordenado, start=1):
                    print("| {:<3} | {:<24} | {:<12} | {:<14} | {:<12} | {:<8} |".format(
                        i,
                        atividade["atividade"],
                        atividade["prioridade"],
                        atividade["data_de_inicio"],
                        atividade["data_de_fim"],
                        atividade["horario"]
                    ))
                print("")

                try:
                    numero_atividade = int(input("Digite o número da atividade que deseja excluir: (Não insira nenhum valor e tecle Enter para voltar)")) - 1
                except ValueError:
                    limpar_console()
                    print("Voltando ao menu principal.")                   
                    time.sleep(2)
                    limpar_console()
                    continue

                if 0 <= numero_atividade < len(planejamento_ordenado):
                    atividade_a_excluir = planejamento_ordenado[numero_atividade]
                    planejamento.remove(atividade_a_excluir)  
                    pessoa["Planejamento"] = planejamento                        
                    limpar_console()
                    print("Atividade excluída com sucesso!")
                    time.sleep(3)
                    limpar_console()
                else:
                    limpar_console()
                    print("Número Inexistente, Voltando ao Menu principal.")
                    time.sleep(3)
                    limpar_console()

                with open("registro.json", "w") as arquivo:
                    json.dump(dados, arquivo, indent=4)
                break
    elif opcao_escolhida == '4': 
        limpar_console()
        print("Escolha a prioridade para filtrar as atividades:")
        print("1 - Alta")
        print("2 - Média")
        print("3 - Baixa")
        opcao_prioridade = input("Digite o número da sua escolha: ")
    
        prioridades = {"1": "Alta", "2": "Media", "3": "Baixa"}
        prioridade_selecionada = prioridades.get(opcao_prioridade)
    
        if prioridade_selecionada:
            limpar_console()
            dados = carregar_dados()
            for pessoa in dados:
                if pessoa.get("nome") == usuario:
                    planejamento = pessoa.get("Planejamento", [])
                    if not isinstance(planejamento, list):
                        planejamento = []
    
                    planejamento_filtrado = [atividade for atividade in planejamento if atividade["prioridade"] == prioridade_selecionada]
    
                    if not planejamento_filtrado:
                        print(f"| Você não tem atividades com prioridade {prioridade_selecionada}! |")
                        time.sleep(3)
                        limpar_console()
                        break
    
                    print("| {:<3} | {:<24} | {:<24} | {:<12} | {:<14} | {:<12} | {:<8} |".format("ID", "Atividade", "Descricao", "Prioridade", "Data de Início", "Data de Fim", "Horário"))
                    print("|" + "-" * 5 + "|" + "-" * 26 + "|" + "-" * 26 + "|" + "-" * 14 + "|" + "-" * 16 + "|" + "-" * 14 + "|" + "-" * 10 + "|")
                    for i, atividade in enumerate(planejamento_filtrado, start=1):
                        print("| {:<3} | {:<24} | {:<12} | {:<14} | {:<12} | {:<8} |".format(
                            i,
                            atividade["atividade"],
                            atividade["prioridade"],
                            atividade["data_de_inicio"],
                            atividade["data_de_fim"],
                            atividade["horario"]
                        ))
                    print("")
                    input("Pressione Enter para voltar ao menu principal.")
                    limpar_console()
                break
                
    elif opcao_escolhida == '5':
        limpar_console()
        print("Voce tem certeza que deseja sair?")
        print("1 - Sim")
        print("2 - Nao, voltar ao Menu")
        confirmacao_saida = input("")
        if confirmacao_saida == '1':
            limpar_console()
            print("Saindo do programa.")
            time.sleep(1)
            limpar_console()
            print("Saindo do programa..")
            time.sleep(1)
            limpar_console()
            print("Saindo do programa...")
            time.sleep(1)
            limpar_console()
            exit()
        elif confirmacao_saida == '2':
            limpar_console()
        else:
            limpar_console()
            print("Opcao Invalida!")
            time.sleep(3)

def menu_hub(usuario):
    while True:
        prioridade_ordem = {"Alta": 1, "Media": 2, "Baixa": 3}
        dados = carregar_dados()
        for pessoa in dados:
            if pessoa.get("nome") == usuario:
                planejamento = pessoa.get("Planejamento", [])
                if not isinstance(planejamento, list):
                    planejamento = []

                print(f"Olá, {usuario}! Bem-vindo ao seu planejador de estudos!\n")

                if not planejamento:
                    print("| Você não tem nenhuma atividade cadastrada! |\n")
                else:
                    planejamento_ordenado = sorted(planejamento, key=lambda x: prioridade_ordem.get(x["prioridade"], 3))
                    print("| {:<3} | {:<24} | {:<24} | {:<12} | {:<14} | {:<12} | {:<8} |".format("ID", "Atividade", "Descricao", "Prioridade", "Data de Início", "Data de Fim", "Horário"))
                    print("|" + "-" * 5 + "|" + "-" * 26 + "|" + "-" * 26 + "|" + "-" * 14 + "|" + "-" * 16 + "|" + "-" * 14 + "|" + "-" * 10 + "|")
                    for i, atividade in enumerate(planejamento_ordenado, start=1):
                        print("| {:<3} | {:<24} | {:<24} | {:<12} | {:<14} | {:<12} | {:<8} |".format(
                            i,
                            atividade["atividade"],
                            atividade["descricao"],
                            atividade["prioridade"],
                            atividade["data_de_inicio"],
                            atividade["data_de_fim"],
                            atividade["horario"]
                        ))
                    print("")

                menu_usuario(usuario)

def login():
    while True:
        limpar_console()
        print("Olá! Por favor, escolha uma opção:")
        print("1 - Fazer login")
        print("2 - Cadastrar novo usuário")
        print("3 - Sair")
        escolha = input("Digite o número da sua escolha: ")

        if escolha == "1":
            limpar_console()
            print("Digite seu nome de usuário:")
            nome_usuario = input("").strip()
            print("Digite sua senha:")
            senha = input("").strip()

            if validar_usuario(nome_usuario, senha):
                limpar_console()
                print("Login realizado com sucesso.")
                time.sleep(3)
                limpar_console()
                menu_hub(nome_usuario)
            else:
                limpar_console()
                print("Nome de usuário ou senha incorretos.")
                time.sleep(3)

        elif escolha == "2":
            limpar_console()
            print("Digite seu nome de usuário:")
            nome_usuario = input("").strip()
            print("Digite sua senha:")
            senha = input("").strip()
            cadastrar_usuario(nome_usuario, senha)

        elif escolha == "3":
            limpar_console()
            print("Saindo do programa.")
            time.sleep(1)
            limpar_console()
            print("Saindo do programa..")
            time.sleep(1)
            limpar_console()
            print("Saindo do programa...")
            time.sleep(1)
            break

        else:
            limpar_console()
            print("Opção inválida, tente novamente.")
            time.sleep(2)

login()