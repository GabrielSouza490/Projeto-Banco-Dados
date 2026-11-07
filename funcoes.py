from database import conexao

def consulta():
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM participantes")
    participantes = cursor.fetchall()

    print("\n==-==-== PARTICIPANTES ==-==-==")

    for participantes in participantes:
        print(f"\nID: {participantes[0]}")
        print(f"Nome: {participantes[1]}")
        print(f"Prática de atividade física: {participantes[2]} ")
        print(f"Qual atividade física: {participantes[3]}")
        print(f"Possui dor: {participantes[4]} ")
        print(f"Local da dor: {participantes[5]} ")
        print(f"-----------------------------------")
    cursor.close()

def casdastro():
    cursor = conexao.cursor()
    print("\n =-=-=-= CADASTRO =-=-=-=")

    nome = input("Nome: ").capitalize()
    idade = input("Idade: ")

    while not idade.isdigit() or len(idade) > 3:
        print("Digite uma idade válida.")
        idade = input("Idade: ")

    idade = int(idade)

    pratica_atividade = input("Realiza atividade física? [Sim/Nao]: ").upper()

    while pratica_atividade not in ['SIM', 'NAO']:
        print("Digite apensas Sim ou Nao")
        pratica_atividade = input("Realiza atividade física? [Sim/Nao]: ").upper()


    qual_atividade = input("Qual atividade realiza? ").capitalize()

    possui_dor = input("Possui dor? [Sim/Nao]: ").upper()

    while possui_dor not in ['SIM', 'NAO']:
        print("Digite apensas Sim ou Nao")
        possui_dor = input("Possui dor? [Sim/Nao]: ").upper()


    local_dor = input("Onde causa mais incômodo? ").capitalize()

#Comando deve ser digitado seguindo o que estiver sido informado na tabela criada no SQL, não do python
    comando = """
    INSERT INTO participantes
    (nome, idade, atividade_fisica, tipo_atividade, dores, onde_tem_dor)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
#Nome dos valores devem seguir o nome das variaveis criadas
    valores = (nome, idade, pratica_atividade, qual_atividade, possui_dor, local_dor)

    cursor.execute(comando, valores)

    conexao.commit()

    cursor.close()

    print("\nParticipante cadastrado!")



def editar():
    cursor = conexao.cursor()

    print("\n=-=-= Editar Usúario =-=-=")

    id_usuario = int(input("Digite o ID do Usúario: "))

    comando = "SELECT id FROM participantes WHERE id = %s"

    cursor.execute(comando, (id_usuario,))

    resultado = cursor.fetchone()

    if resultado is None:
        print("Usúario não encontrado!")
        cursor.close()
        return

    print("[1] - Alterar nome")
    print("[2] - Alterar pratica atividade")
    print("[3] - Alterar tipo de atividade")
    print("[4] - Alterar se exite dor")
    print("[5] - Alterar local da dor")
    print("[6] - Voltar")

    escolha = input("Escolha: ")

    if escolha == "1":
        confirmar = input("Realmente deseja alterar? [S/N] ").upper()

        while confirmar not in ['S', 'N']:
            print("Apenas S ou N")
            confirmar = input("Realmente deseja alterar? [S/N] ").upper()

        if confirmar == "N":
            cursor.close()
            return

        elif confirmar == "S":
            novo_nome = input("Digite o nome: ").capitalize()

            comando = """
            UPDATE participantes
            SET nome = %s
            WHERE id = %s
            """
        valores = (novo_nome, id_usuario)

    elif escolha == "2":
        confirmar = input("Realmente deseja alterar? [S/N] ").upper()

        while confirmar not in ['S', 'N']:
            print("Apenas S ou N")
            confirmar = input("Realmente deseja alterar? [S/N] ").upper()

        if confirmar == "N":
            cursor.close()
            return

        elif confirmar == "S":
            nova_atividade = input("Realiza atividade física? [Sim/Nao] ").upper()

            while nova_atividade not in ["SIM", "NAO"]:
                print("Digite apenas Sim ou Nao")
                nova_atividade = input("Realiza atividade física? [Sim/Nao] ").upper()

        comando = """
        UPDATE participantes
        SET atividade_fisica = %s
        WHERE id = %s
        """

        valores = (nova_atividade, id_usuario)


    elif escolha == "3":
        confirmar = input("Realmente deseja alterar? [S/N] ").upper()

        while confirmar not in ['S', 'N']:
            print("Apenas S ou N")
            confirmar = input("Realmente deseja alterar? [S/N] ").upper()

        if confirmar == "N":
            cursor.close()
            return

        elif confirmar == "S":
            novo_tipo = input("Qual atividade realiza? ").capitalize()

        comando = """
        UPDATE participantes
        SET tipo_atividade = %s
        WHERE id = %s
        """

        valores = (novo_tipo, id_usuario)


    elif escolha == "4":
        confirmar = input("Realmente deseja alterar? [S/N] ").upper()

        while confirmar not in ['S', 'N']:
            print("Apenas S ou N")
            confirmar = input("Realmente deseja alterar? [S/N] ").upper()

        if confirmar == "N":
            cursor.close()
            return

        elif confirmar == "S":
            nova_dor = input("Possui dor? [Sim/Nao] ").upper()

            while nova_dor not in ["SIM", "NAO"]:
                print("Digite apenas Sim ou Nao")
                nova_dor = input("Possui dor? [Sim/Nao] ").upper()

        comando = """
        UPDATE participantes
        SET dores = %s
        WHERE id =%s
        """
        valores = (nova_dor, id_usuario)

    elif escolha == "5":
        confirmar = input("Realmente deseja alterar? [S/N] ").upper()

        while confirmar not in ['S', 'N']:
            print("Apenas S ou N")
            confirmar = input("Realmente deseja alterar? [S/N] ").upper()

        if confirmar == "N":
            cursor.close()
            return

        elif confirmar == "S":
            novo_local = input("Onde causa mais incômodo? ").capitalize()

        comando = """
        UPDATE participantes
        SET onde_tem_dor = %s
        WHERE id = %s
        """
        valores = (novo_local, id_usuario)


    elif escolha == "6":
        cursor.close()
        return

    cursor.execute(comando, valores)
    conexao.commit()

    print("\nUsuário atualizado!")
    cursor.close()



def excluir():
    cursor = conexao.cursor()
    print("\n=-=-= Excluir Usuário =-=-=")

    id_usuario = int(input("Digite o ID do usuáriu: "))

    cursor.execute("SELECT * FROM participantes WHERE id = %s",(id_usuario,))

    resultado = cursor.fetchone()

    if resultado is None:
        print("Usuário não existe")
        cursor.close()
        return

    print(f"\nID: {resultado[0]}")
    print(f"Nome: {resultado[1]}")

    confirmar = input("Realmente deseja excluir? [S/N] ").upper()

    while confirmar not in ['S', 'N']:
        print("Apenas S ou N")
        confirmar = input("Realmente deseja alterar? [S/N] ").upper()

    if confirmar == "N":
        cursor.close()
        return

    elif confirmar == "S":
        comando = "DELETE FROM participantes WHERE id = %s"

        cursor.execute(comando,(id_usuario,))
        conexao.commit()

        print("Usuário Excluido!")

    cursor.close

