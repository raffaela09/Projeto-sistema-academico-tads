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
          9 - Consultar alunos. 
          10 - Consultar professores.
          0 - Sair.
          ''')
#-----------------------------------------------  

#cadastrar aluno
alunos = []
def cad_aluno():
    nome_aluno = input('Digite o seu nome: ')
    matricula_aluno = int(input('Digite a sua matricula: '))
    data_nasc_aluno = input('Digite a sua data de nascimento: ')
    sexo_aluno = input('Digite o seu sexo: ')
    endereco_aluno = input('Digite o seu endereço: ')
    telefone_aluno = input('Digite o seu telefone: ')
    email_aluno = input('Digite o seu e-mail: ')

    for aluno in alunos:
        if aluno['matricula'] == matricula_aluno:
            print(f'Erro: A matricula {matricula_aluno} já está cadastrada')
            return #fazer validação em outra funçao

    print(f"Aluno(a) {nome_aluno} cadastrado(a) com sucesso!")
    aluno = {'nome': nome_aluno, 'matricula': matricula_aluno, 'data_nascimento': data_nasc_aluno, 'sexo': sexo_aluno, 'endereco': endereco_aluno, 'telefone': telefone_aluno, 'email': email_aluno}
    alunos.append(aluno)
    return aluno # esse tbm
#-----------------------------------------------


#cadastrar professores
professores = []
def cad_professores():
    nome_prof = input('Digite o seu nome: ')
    disciplina_prof = input('Digite as suas disciplina separadas por virgulas: ').split(',')
    data_nasc_prof = input('Digite a sua data de nascimento: ')
    sexo_prof = input('Digite o seu sexo: ')
    endereco_prof = input('Digite o seu endereço: ')
    telefone_prof = int(input('Digite o seu telefone: '))
    email_prof = input('Digite o seu e-mail: ')
#validacao
    for professor in professores:
        if professor['email'] == email_prof:
            print(f'Erro: O e-mail {email_prof} já está cadastrada')
            return #validar em outra func


    print(f"Professor {nome_prof} cadastrado com sucesso!")
    professores.append({'nome': nome_prof, 'disciplinas': disciplina_prof, 'data_nascimento': data_nasc_prof, 'sexo': sexo_prof, 'endereco': endereco_prof, 'telefone': telefone_prof, 'email': email_prof})
    return professores #esse tbm
#-----------------------------------------------

#cadastrar disciplinas
disciplinas = []
def cad_disciplina():
    nome_disc = input('Digite o nome da disciplina: ')
    cod_disc = input('Digite o código da disciplina: ')
    carga_disc = int(input('Digite a carga horaria da disciplina: '))
    professores_disc = input('Digite o responsável pela disciplina: ')
    #validação p verificar se ja ta cadastrada
    print(f"Disciplina {nome_disc} cadastrada com sucesso!")
    disciplinas.append({'nome': nome_disc, 'codigo': cod_disc, 'carga_horaria': carga_disc, 'professor': professores_disc})
#-----------------------------------------------

#cadastrar turmas
turmas = []
def cad_turmas():
    nome_turma = input('Digite o nome da turma: ')
    cod_turma = input('Digite o código da turma: ')
    disciplina_turma = input('Digite as disciplinas da turma: ')
    professor_turma = input('Digite o professor da turma: ')
    # alunos_turma = (lista_matricula)

    print(f"Turma {nome_turma} cadastrada com sucesso!")
    turmas.append({'nome': nome_turma, 'codigo': cod_turma, 'disciplina': disciplina_turma, 'professor': professor_turma, 'alunos': []})
#-----------------------------------------------

#filtrar os professores por disciplina
def filtrar_prof_disciplina():
    disciplina_filt = input('Digite a disciplina que deseja filtrar os professores: ')
    professores_filt = [prof for prof in professores if prof['disciplina'].lower() == disciplina_filt.lower()]
    if professores_filt:
        print(f"Professores para a disciplina {disciplina_filt}:")
        for prof in professores_filt:
            print(f"- {prof['nome']}")
    else:
        print(f"Nenhum professor foi encontrado para a disciplina {disciplina_filt}")
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
               if 'alunos' not in turma:
                   turma['alunos'] = []
                   turma['alunos'].append(aluno_encontrado['matricula'])
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
        professor_encontrado_dsc['disciplinas'].append(dsc_nome)
        print(f'Professor {professor_nome} alocado para a disciplina {dsc_nome}')
    else:
        print('professor não encontrado.')
#-----------------------------------------------

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
        turma_encontrada['disciplina'] = disciplina_nome
        print(f'Disciplina {disciplina_nome} alocada para a turma {turma_encontrada["nome"]} com sucesso!!')
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


#funcao que executa o código
def executar():
    while True:
        exibir_opcoes()
        opcao = int(input('Escolha uma opção (em numeros.)'))

        if opcao == 1:
            cad_aluno()
        elif opcao == 2:
            cad_professores()
        elif opcao == 3:
            cad_disciplina()
        elif opcao == 4:
            cad_turmas()
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
        elif opcao == 0:
            print('Saindo... Até a proxima!')
            break
        else:
            print('Opção inválida. Teente novamente.')

executar()


