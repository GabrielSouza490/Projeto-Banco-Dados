from funcoes import consulta,casdastro,editar,excluir

while True:
    print("\n===-=-Painel-=-===\n")
    print('[1]- Consultar Usuario')
    print('[2]- Cadastrar Usuario')
    print('[3]- Editar Usuario')
    print('[4]- Excluir Usuario')
    print('[5]- Sair')

    ops = input('Escolha uma opção: ')

    while ops not in ['1','2','3','4','5']:
        print('Opção Inexistente.')
        ops = input('Escolha uma opção: ')

    if ops == '1':
        consulta()
    elif ops == '2':
        casdastro()
    elif ops == '3':
        editar()
    elif ops == '4':
        excluir()
    elif ops == '5':
        print('Programa Finalizado')
        break