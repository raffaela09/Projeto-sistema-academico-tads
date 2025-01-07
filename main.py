#opções do usuario
def exibir_opcoes():
    print('''Bem vindo!! Escolha uma opção:
          1 - Cadastrar aluno.
          2 - Cadastrar docente.
          3 - Cadastrar disciplina.
          4 - Cadastrar turma.
          5 - Filtrar professores por disciplina.
          6 - Matricular aluno em turma.
          7 - Alocar professor em disciplina.
          8 - Alocar disciplina em turma.
          9 - Consultar alunos cadastrados. 
          10 - Consultar professores cadastrados.
          11 - Consultar alunos matriculados em turmas.
          12 - Consultar professores alocados em disciplinas
          13 - Consultar disciplinas cadastradas em turmas.
          0 - Sair.
          ''')
#-----------------------------------------------  

#coletar os dados dos alunos
alunos = []
def coletar_dados_alunos():
    nome_aluno = input('Digite o seu nome: ')
    matricula_aluno = int(input('Digite a sua matricula: '))
    data_nasc_aluno = input('Digite a sua data de nascimento: ')
    sexo_aluno = input('Digite o seu sexo: ')
    endereco_aluno = input('Digite o seu endereço: ')
    telefone_aluno = input('Digite o seu telefone: ')
    email_aluno = input('Digite o seu e-mail: ')

    aluno_dados = {'nome': nome_aluno, 'matricula': matricula_aluno, 'data_nascimento': data_nasc_aluno, 'sexo': sexo_aluno, 'endereco': endereco_aluno, 'telefone': telefone_aluno, 'email': email_aluno}
    return aluno_dados 
#-----------------------------------------------

#validar se o aluno já está cadastrado
def ver_aluno_existente(matricula_aluno):
    for aluno in alunos:
        if aluno['matricula'] == matricula_aluno:
            return True
    return False
#-----------------------------------------------

#cadastrar alunos
def cad_alunos():
    dados_alunos = coletar_dados_alunos()
    if ver_aluno_existente(dados_alunos["matricula"]):
            print(f"Erro: A matricula {dados_alunos['matricula']} já está cadastrada")
            return
    alunos.append(dados_alunos)
    print(f'O aluno {dados_alunos['nome']} foi cadastrado com sucesso!')
#-----------------------------------------------

#responsavel por coletar dados dos professores
professores = []
def coletar_dados_professores():
    nome_prof = input('Digite o seu nome: ')
    disciplina_prof = input('Digite as suas disciplina separadas por virgulas: ').lower().split(',')
    data_nasc_prof = input('Digite a sua data de nascimento: ')
    sexo_prof = input('Digite o seu sexo: ')
    endereco_prof = input('Digite o seu endereço: ')
    telefone_prof = int(input('Digite o seu telefone: '))
    email_prof = input('Digite o seu e-mail: ')

    professores_dados = {'nome': nome_prof, 'disciplinas': disciplina_prof, 'data_nascimento': data_nasc_prof, 'sexo': sexo_prof, 'endereco': endereco_prof, 'telefone': telefone_prof, 'email': email_prof}
    return professores_dados
#-----------------------------------------------

#validação de cadastro
def ver_prof_existente(email_prof):
    for professor in professores:
        if professor['email'] == email_prof:
            return True
    return False
#-----------------------------------------------

#cadastrar professores
def cad_prof():
    dados_prof = coletar_dados_professores()
    if ver_prof_existente(dados_prof["email"]):
        print(f"Erro: O e-mail {dados_prof['email']} já está cadastrada")
        return
    professores.append(dados_prof)
    print(f"O docente {dados_prof['nome']} foi cadastrado com sucesso!")
#-----------------------------------------------

#coletar dados das disciplinas
disciplinas = []
def coletar_dados_disciplinas():
    nome_disc = input('Digite o nome da disciplina: ')
    cod_disc = input('Digite o código da disciplina: ')
    carga_disc = int(input('Digite a carga horaria da disciplina: '))
    professores_disc = input('Digite o responsável pela disciplina: ')
    
    print(f"Disciplina {nome_disc} cadastrada com sucesso!")
    disciplina_dados = {'nome': nome_disc, 'codigo': cod_disc, 'carga_horaria': carga_disc, 'professor': professores_disc}
    return disciplina_dados
#-----------------------------------------------

#validação da disciplina já existente 
def disciplina_existente(cod_disc):
   for disciplina in disciplinas:
        if disciplina['codigo'] == cod_disc:
            return True
   return False
#-----------------------------------------------   

#cadastrar disciplinas
def cad_disciplina():
    dados_disciplina = coletar_dados_disciplinas()
    if disciplina_existente(dados_disciplina["codigo"]):
        print(f'A disciplina {dados_disciplina['nome']} já está cadastrada.')
        return 
    disciplinas.append(dados_disciplina)
    print(f'A disciplina {dados_disciplina["nome"]} foi cadastrada com sucesso!')
#-----------------------------------------------  
  
#coletar dados da turma
turmas = []
def coletar_dados_turmas():
    nome_turma = input('Digite o nome da turma: ')
    cod_turma = input('Digite o código da turma: ')
    disciplina_turma = input('Digite as disciplinas da turma: ')
    professor_turma = input('Digite o professor da turma: ')
    # alunos_turma = (lista_matricula)
    turma_dados = {'nome': nome_turma, 'codigo': cod_turma, 'disciplina': disciplina_turma, 'professor': professor_turma, 'alunos': []}
    return turma_dados
#-----------------------------------------------

#verificar se a turma ja esta cadastrada
def turma_existente(cod_turma):
    for turma in turmas:
        if turma['codigo'] == cod_turma:
            return True
    return False
#-----------------------------------------------

#cadastrar turma
def cad_turma():
    dados_turma = coletar_dados_turmas()
    if turma_existente(dados_turma["codigo"]):
        print(f'A disciplina {dados_turma['nome']} já está cadastrada!')
        return
    turmas.append(dados_turma)
    print(f'A turma {dados_turma["nome"]} foi cadastrada com sucesso!')

#-----------------------------------------------s


#filtrar os professores por disciplina
def filtrar_prof_disciplina():
    disciplina_filt = input('Digite a disciplina que deseja filtrar os professores: ')
    professores_filt = [prof for prof in professores if disciplina_filt in prof["disciplinas"]]
    if professores_filt:
        print(f"Professores para a disciplina {disciplina_filt}:")
        for prof in professores_filt:
            print(f"- {prof['nome']}")
    else:
        print(f"Nenhum professor cadastrado foi encontrado para a disciplina {disciplina_filt}")
#-----------------------------------------------

#matricular aluno em turmas
turma_alunos = []
def mat_aluno_turmas():
    mat_aluno = int(input('Digite a matricula do aluno: '))
    turma_cod_al = input('Digite o codigo da turma: ') 

    aluno_encontrado = None
    for aluno in alunos:
        if aluno['matricula'] == mat_aluno:
            aluno_encontrado = aluno
            break

    if aluno_encontrado:
       for turma in turmas:
           if turma['codigo'] == turma_cod_al:
                   turma['alunos'].append(aluno_encontrado)
                   print(f'Aluno {aluno_encontrado["nome"]} matriculado na turma {turma_cod_al} com sucesso!')
                   return
    else:
        print('Aluno não encontrado.')
#-----------------------------------------------

#professoress alocados em disciplinas
def alocar_prof_dsc():
    professor_nome = input('Digite o nome do professor: ')
    dsc_nome = input('Digite o nome da disciplina: ')

    professor_encontrado_dsc = None
    for professor in professores:
        if professor['nome'].lower() == professor_nome.lower():
            professor_encontrado_dsc = professor
            break
    if professor_encontrado_dsc:
        if not disciplina_foi_cad(dsc_nome):
            print('A disciplina não está cadastrada.')
            return
        professor_encontrado_dsc['disciplinas'].append(dsc_nome)
        print(f'Professor {professor_nome} alocado para a disciplina {dsc_nome}')
    else:
        print('professor não encontrado.')
#-----------------------------------------------

#validação pra conferir se a disciplina esta cadastrada
def disciplina_foi_cad(disciplina_nome):
        disciplina_encontrada = False
        for disciplina in disciplinas:
            if disciplina["nome"].lower() == disciplina_nome.lower():
                disciplina_encontrada = True
                break
        return disciplina_encontrada

#disciplinas alocadas em turma
def alocar_disc_turma():
    turma_cod_dsc = input('Digite o código da turma: ')
    disciplina_nome = input('Digite o nome da disciplina: ')

    turma_encontrada = None
    for turma in turmas:
        if turma['codigo'].lower() == turma_cod_dsc.lower():
            turma_encontrada = turma
            break
        
    if turma_encontrada:
        if not disciplina_foi_cad(disciplina_nome):
            print('A disciplina não está cadastrada.')
            return
        if disciplina_nome not in turma_encontrada["disciplina"]:
            turma_encontrada['disciplinas'] = []  
        if disciplina_nome not in turma_encontrada["disciplinas"]:
            turma_encontrada["disciplinas"].append(disciplina_nome)
            print(f'Disciplina {disciplina_nome} foi alocada para a turma {turma_encontrada["nome"]} com sucesso!')
        else:
                print(f'A disciplina {disciplina_nome} já está alocada nessa turma.')
    else:
        print('Turma não encontrada.')
#-----------------------------------------------


#consultar alunos
def consultar_alunos():
    if alunos:
        print('Alunos cadastrados: ')
        for aluno in alunos:
            print(f'{aluno["nome"]} - Matricula: {aluno["matricula"]}')
    else:
        print('Nenhum aluno cadastrado.')
#-----------------------------------------------

#consultar professores
def consultar_professores():
    if professores:
        print('Professores cadastrados:')
        for professor in professores:
            print(f'{professor["nome"]} - E-mail: {professor["email"]}')
            print(f'Disciplinas: {", ".join(professor["disciplinas"])}')
    else:
        print('Nenhum professor cadastrado.')
#-----------------------------------------------

#consultar disciplinas por turmas
def consultar_dsc_turmas():
    if turmas:
        print('Disciplinas cadastradas nas turmas:')
        for turma in turmas:
            print(f'Turmas: {turma["nome"]} - Disciplina: {turma["disciplina"]}, {turma["disciplinas"]}')
#-----------------------------------------------

#consultar profs em disciplinas
def consultar_prof_dsc():
    if professores:
        print('Professores alocados nas disciplinas:')
        for professor in professores:
            print(f'Disciplina: {professor["disciplinas"]}')
            print(f'Responsavel: {professor["nome"]} - Email: {professor["email"]}')
            print()
    else:
        print('Não houve nenhuma alocação de professores.')
#-----------------------------------------------

#funcao pra consultar alunos em turmas
def consultar_alunos_turmas():
    if turmas:
        print('Alunos matriculados nas turmas:')
        for turma in turmas:
            print(f'Turma: {turma["nome"]} - Codigo: {turma["codigo"]}')
            if turma["alunos"]:
                for aluno in turma["alunos"]:
                        print(f"- {aluno['nome']} (Matricula: {aluno['matricula']})")
            else:
                print('Nenhum aluno matriculado.')
    else:
        print('Nenhuma turma cadastrada.')


#funcao que executa o código
def executar():
    while True:
        exibir_opcoes()
        opcao = int(input('Escolha uma opção (em numeros.) '))

        if opcao == 1:
            cad_alunos()
        elif opcao == 2:
            cad_prof()
        elif opcao == 3:
            cad_disciplina()
        elif opcao == 4:
            cad_turma()
        elif opcao == 5:
            filtrar_prof_disciplina()
        elif opcao == 6:
            mat_aluno_turmas()
        elif opcao == 7:
            alocar_prof_dsc()
        elif opcao == 8:
            alocar_disc_turma()
        elif opcao == 9:
            consultar_alunos()
        elif opcao == 10:
            consultar_professores()
        elif opcao == 11:
            consultar_alunos_turmas()
        elif opcao == 12:
            consultar_prof_dsc()
        elif opcao == 13:
            consultar_dsc_turmas()
        elif opcao == 0:
            print('Saindo... Até a proxima!')
            break
        else:
            print('Opção inválida. Teente novamente.')

executar()


