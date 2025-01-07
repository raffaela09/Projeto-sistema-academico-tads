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

    if ver_prof_existente(email_prof):
        print(f'Erro: O e-mail {email_prof} já está cadastrada')
        return None

    professores_dados = {'nome': nome_prof, 'disciplinas': disciplina_prof, 'data_nascimento': data_nasc_prof, 'sexo': sexo_prof, 'endereco': endereco_prof, 'telefone': telefone_prof, 'email': email_prof}
    cad_prof(professores_dados)
#-----------------------------------------------

#cadastrar professores
def cad_prof(professores_dados):
    professores.append(professores_dados)
    print(f"O docente {professores_dados["nome"]} foi cadastrado com sucesso!")
#-----------------------------------------------

#validação de professor
def ver_prof_existente(email_prof):
    for professor in professores:
        if professor['email'] == email_prof:
            return True
    return False
#-----------------------------------------------

#cadastrar disciplinas
disciplinas = []
def cad_disciplina():
    nome_disc = input('Digite o nome da disciplina: ')
    cod_disc = input('Digite o código da disciplina: ')
    if disciplina_existente(cod_disc):
        print(f'A disciplina {nome_disc} já está cadastrada.')
        return None
    carga_disc = int(input('Digite a carga horaria da disciplina: '))
    professores_disc = input('Digite o responsável pela disciplina: ')

    #validação p verificar se ja ta cadastrada
    print(f"Disciplina {nome_disc} cadastrada com sucesso!")
    disciplina_dados = ({'nome': nome_disc, 'codigo': cod_disc, 'carga_horaria': carga_disc, 'professor': professores_disc})
    return disciplina_dados
#-----------------------------------------------

#validação da disciplina já existente 
def disciplina_existente(cod_disc):
   for disciplina in disciplinas:
        if disciplina['codigo'] == cod_disc:
            return True
   return False
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
    professores_filt = [prof for prof in professores if disciplina_filt in prof["disciplinas"]]
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
        print(f'Disciplina {disciplina_nome} alocada para a turma {turma_encontrada["nome"]} com sucesso!!') #arrumar aqui, ele ta substituindo a chave, e o ideal seria adicionar
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
            print(f'Turmas: {turma["nome"]} - Disciplina: {turma["disciplina"]}')
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
        print('Alinos matriculados nas turmas:')
        for turma in turmas:
            print(f'Turma: {turma["nome"]} - Codigo: {turma["codigo"]}')
            if turma["alunos"]:
                for aluno_matricula in turma["alunos"]:
                     aluno_encontrado = next((aluno for aluno in alunos if aluno['matricula'] == aluno_matricula), None)
                     if aluno_encontrado:
                        print(f"- {aluno_encontrado['nome']} (Matrícula: {aluno_encontrado['matricula']})")
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
            cad_aluno()
        elif opcao == 2:
            coletar_dados_professores()
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


