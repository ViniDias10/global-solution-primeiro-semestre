# Estrutura de dados principal 

ocorrencias_id = {}       
ocorrencias_lista = []      
fila_analise = []          
historico_att = []        
hierarquia = {}

# Simulação de dados fictícios

dados_iniciais = [
    {"id": "001", "categoria": "iluminação", "descricao": "Poste apagado na rua principal", "local": "Rua A", "dia_abertura": 1, "status": "aberta"},
    {"id": "002", "categoria": "acessibilidade", "descricao": "Calçada esburacada", "local": "Rua B", "dia_abertura": 2, "status": "em análise"},
    {"id": "003", "categoria": "limpeza", "descricao": "Lixo acumulado na praça", "local": "Praça Central", "dia_abertura": 2, "status": "concluída"},
    {"id": "004", "categoria": "conservação", "descricao": "Banco quebrado", "local": "Praça Central", "dia_abertura": 3, "status": "aberta"},
    {"id": "005", "categoria": "iluminação", "descricao": "Fiação exposta", "local": "Rua C", "dia_abertura": 4, "status": "em análise"},
    {"id": "006", "categoria": "acessibilidade", "descricao": "Falta de rampa", "local": "Av. Principal", "dia_abertura": 5, "status": "aberta"},
    {"id": "007", "categoria": "limpeza", "descricao": "Bueiro entupido", "local": "Rua D", "dia_abertura": 6, "status": "em análise"},
    {"id": "008", "categoria": "conservação", "descricao": "Pichação no muro da escola", "local": "Escola Municipal", "dia_abertura": 7, "status": "concluída"},
    {"id": "009", "categoria": "iluminação", "descricao": "Lâmpada piscando", "local": "Rua E", "dia_abertura": 8, "status": "aberta"},
    {"id": "010", "categoria": "acessibilidade", "descricao": "Sinal sonoro quebrado", "local": "Av. Principal", "dia_abertura": 9, "status": "aberta"},
    {"id": "011", "categoria": "limpeza", "descricao": "Mato alto no terreno", "local": "Terreno Baldio", "dia_abertura": 10, "status": "em análise"},
    {"id": "012", "categoria": "conservação", "descricao": "Placa de rua caída", "local": "Rua F", "dia_abertura": 11, "status": "concluída"},
    {"id": "013", "categoria": "", "descricao": "Buraco na rua", "local": "Rua G", "dia_abertura": 12, "status": "aberta"}
]


# Função de inicialização do sistema

def iniciar_sistema():
    bairro_nome = "Vila Aurora"
    hierarquia[bairro_nome] = {}

    for ocorrencia in dados_iniciais:
        categoria = ocorrencia["categoria"]
        if categoria != "":
            if categoria not in hierarquia[bairro_nome]:
                hierarquia[bairro_nome][categoria] = []
            hierarquia[bairro_nome][categoria].append(ocorrencia["id"])

        ocorrencias_id[ocorrencia["id"]] = ocorrencia
        ocorrencias_lista.append(ocorrencia)

        if ocorrencia["status"] == "aberta":
            fila_analise.append(ocorrencia["id"])


iniciar_sistema()
print(f"Sistema iniciado com {len(ocorrencias_lista)} registros.")
print(f"Demandas aguardando na fila de análise: {len(fila_analise)}")



# Validação de dados

CATEGORIAS_VALIDAS = ["iluminação", "acessibilidade", "limpeza", "conservação"]
STATUS_VALIDOS = ["aberta", "em análise", "concluída"]



# Função de validação de dados e tratamento de inconsistência

def auditar_registros_inconsistentes():
    print("\n--- AUDITORIA DE DADOS INICIAIS ---")
    inconsistencias = 0
    for ocorrencia in ocorrencias_lista:
        if (ocorrencia["categoria"] not in CATEGORIAS_VALIDAS) or (not ocorrencia["descricao"]) or (not ocorrencia["local"]):
            inconsistencias += 1
            print(f"[ALERTA DE INCONSISTÊNCIA] Registro ID '{ocorrencia['id']}' possui dados ausentes ou categoria inválida ('{ocorrencia['categoria']}').")
            ocorrencia["categoria"] = "conservação"
            hierarquia["Vila Aurora"]["conservação"].append(ocorrencia["id"])
            print(f" -> Correção aplicada: ID '{ocorrencia['id']}' reclassificado para 'conservação'.")
            
    if inconsistencias == 0:
        print("Nenhuma inconsistência encontrada.")



# Função para cadastro de uma nova ocorrência com validação

def cadastrar_ocorrencia(id, categoria, descricao, local, dia_abertura, status="aberta"):
    print(f"\nTentando cadastrar ocorrência ID '{id}'...")
    
    categoria = categoria.strip().lower()
    status = status.strip().lower()

    if id in ocorrencias_id or not id:
        print(f"[ERRO] O ID '{id}' já existe no sistema ou é inválido.")
        return False
    
    if not descricao.strip() or not local.strip():
        print("[ERRO] Descrição e Local são campos obrigatórios.")
        return False

    if categoria not in CATEGORIAS_VALIDAS:
        print(f"[ERRO] Categoria '{categoria}' inválida. Use: {CATEGORIAS_VALIDAS}")
        return False
    elif status not in STATUS_VALIDOS:
        print(f"[ERRO] Status '{status}' inválido. Use: {STATUS_VALIDOS}")
        return False
    else:
        nova_ocorrencia = {
            "id": id,
            "categoria": categoria,
            "descricao": descricao.strip(),
            "local": local.strip(),
            "dia_abertura": dia_abertura,
            "status": status
        }

        ocorrencias_id[id] = nova_ocorrencia
        ocorrencias_lista.append(nova_ocorrencia)
        hierarquia["Vila Aurora"][categoria].append(id)

        if status == "aberta":
            fila_analise.append(id)

        print(f"[SUCESSO] Ocorrência '{id}' ({categoria}) cadastrada e adicionada às estruturas!")
        return True

auditar_registros_inconsistentes()

cadastrar_ocorrencia("014", "segurança", "Falta de policiamento", "Praça Central", 13)

cadastrar_ocorrencia("014", "iluminação", "Refletor queimado na quadra", "Praça Central", 13, "aberta")



# Função para consultar id

def consultar_id(id):
    print(f"\n--- CONSULTA POR ID: '{id}' ---")
    if id in ocorrencias_id:
        ocorrencia = ocorrencias_id[id]
        print(f"ID: {ocorrencia['id']} | Categoria: {ocorrencia['categoria'].upper()} | Status: {ocorrencia['status'].upper()}")
        print(f"Local: {ocorrencia['local']} (Dia {ocorrencia['dia_abertura']}) | Descrição: {ocorrencia['descricao']}")
    else:
        print(f"[AVISO] Nenhuma ocorrência encontrada com o ID '{id}'.")


# Função para filtrar as ocorrências por um critério específico

def filtrar_ocorrencias(categoria=None, status=None):
    print(f"\n--- FILTRO DE OCORRÊNCIAS (Categoria: {categoria} | Status: {status}) ---")
    encontradas = 0
    for ocorrencia in ocorrencias_lista:
        condicao_categoria = (categoria is None) or (ocorrencia["categoria"] == categoria.lower())
        condicao_status = (status is None) or (ocorrencia["status"] == status.lower())
        
        if condicao_categoria and condicao_status:
            encontradas += 1
            print(f"[{ocorrencia['id']}] {ocorrencia['categoria'].capitalize()} - {ocorrencia['local']} | Status: {ocorrencia['status'].upper()} ({ocorrencia['descricao']})")
            
    if encontradas == 0:
        print("Nenhuma ocorrência corresponde aos filtros informados.")


# Função para atualizar o status de uma ocorrência

def atualizar_status(id, novo_status, dia_evento, observacao=""):
    novo_status = novo_status.strip().lower()
    
    if id not in ocorrencias_id:
        print(f"[ERRO] Não foi possível atualizar: ID '{id}' não encontrado.")
        return False
    if novo_status not in STATUS_VALIDOS:
        print(f"[ERRO] Status '{novo_status}' inválido. Escolha entre: {STATUS_VALIDOS}")
        return False

    ocorrencia = ocorrencias_id[id]
    status_anterior = ocorrencia["status"]
    
    if status_anterior == novo_status:
        print(f"[AVISO] A ocorrência '{id}' já está com o status '{novo_status}'.")
        return False

    ocorrencia["status"] = novo_status
    
    if status_anterior == "aberta" and id in fila_analise:
        fila_analise.remove(id)
        
    if novo_status == "concluída":
        ocorrencia["dia_conclusao"] = dia_evento

    evento_att = {
        "id": id,
        "de": status_anterior,
        "para": novo_status,
        "dia": dia_evento,
        "obs": observacao
    }
    historico_att.append(evento_att)
    print(f"[ATUALIZADO] ID '{id}': '{status_anterior}' -> '{novo_status}' (Dia {dia_evento}).")
    return True


# Função para exibir as últimas atualizações

def exibir_historico_att(limite=5):
    print(f"\n--- ÚLTIMAS {limite} ATUALIZAÇÕES (PILHA LIFO) ---")
    if not historico_att:
        print("Nenhum evento registrado no histórico.")
        return
  
    for evento in reversed(historico_att[-limite:]):
        print(f"Dia {evento['dia']:02d} | ID {evento['id']}: {evento['de']} -> {evento['para']} | Obs: {evento['obs']}")


# Dados Fictícios registros

eventos_passados = [
    {"id": "002", "de": "aberta", "para": "em análise", "dia": 3, "obs": "Equipe técnica designada."},
    {"id": "003", "de": "aberta", "para": "em análise", "dia": 3, "obs": "Coleta agendada."},
    {"id": "003", "de": "em análise", "para": "concluída", "dia": 4, "obs": "Praça limpa."},
    {"id": "005", "de": "aberta", "para": "em análise", "dia": 5, "obs": "Vistoria elétrica solicitada."},
    {"id": "007", "de": "aberta", "para": "em análise", "dia": 7, "obs": "Caminhão hidrojato acionado."},
    {"id": "008", "de": "aberta", "para": "em análise", "dia": 8, "obs": "Material de pintura separado."},
    {"id": "008", "de": "em análise", "para": "concluída", "dia": 10, "obs": "Muro restaurado."},
    {"id": "011", "de": "aberta", "para": "em análise", "dia": 11, "obs": "Notificação ao proprietário."},
    {"id": "012", "de": "aberta", "para": "em análise", "dia": 12, "obs": "Nova placa fabricada."},
    {"id": "012", "de": "em análise", "para": "concluída", "dia": 13, "obs": "Placa reinstalada."}
]

historico_att.extend(eventos_passados)

ocorrencias_id["003"]["dia_conclusao"] = 4
ocorrencias_id["008"]["dia_conclusao"] = 10
ocorrencias_id["012"]["dia_conclusao"] = 13

consultar_id("014")
filtrar_ocorrencias(categoria="iluminação", status="aberta")

print("\nExecutando atualização em tempo real:")
atualizar_status("014", "em análise", dia_evento=14, observacao="Ordem de serviço emitida para troca do refletor.")
exibir_historico_att(5)


#Função para construir a Matriz (Categorias x Status) e calcular indicadores

def exibir_indicadores():
    print("\n" + "="*65)
    print("        NEIGHBORHOOD ACTION DASHBOARD - VILA AURORA")
    print("="*65)

    total_ocorrencias = len(ocorrencias_lista)
    if total_ocorrencias == 0:
        print("Nenhuma ocorrência cadastrada para gerar indicadores.")
        return
    
    matriz_resumo = [[0 for _ in STATUS_VALIDOS] for _ in CATEGORIAS_VALIDAS]

    categorias_totais = [0] * len(CATEGORIAS_VALIDAS)
    status_totais = [0] * len(STATUS_VALIDOS)

    soma_dias_conclusao = 0
    qtd_concluidas = 0

    for ocorrencia in ocorrencias_lista:
        categoria = ocorrencia["categoria"]
        status = ocorrencia["status"]

        if categoria in CATEGORIAS_VALIDAS and status in STATUS_VALIDOS:
            idx_linha = CATEGORIAS_VALIDAS.index(categoria)
            idx_coluna = STATUS_VALIDOS.index(status)

            matriz_resumo[idx_linha][idx_coluna] += 1
            categorias_totais[idx_linha] += 1
            status_totais[idx_coluna] += 1

        if status == "concluída" and "dia_conclusao" in ocorrencia:
            tempo_resolucao = ocorrencia["dia_conclusao"] - ocorrencia["dia_abertura"]
            soma_dias_conclusao += tempo_resolucao
            qtd_concluidas += 1

    print("\n[1] MATRIZ DE DISTRIBUIÇÃO (CATEGORIA x STATUS)")
    print(f"{'CATEGORIA':<16} | {'ABERTA':<8} | {'EM ANÁLISE':<11} | {'CONCLUÍDA':<10} | {'TOTAL (%)'}")
    print("-" * 65)

    for i, categoria in enumerate(CATEGORIAS_VALIDAS):
        aberta = matriz_resumo[i][0]
        analise = matriz_resumo[i][1]
        concluida = matriz_resumo[i][2]
        tot_cat = categorias_totais[i]
        perc_cat = (tot_cat / total_ocorrencias) * 100
        print(f"{categoria.capitalize():<16} | {aberta:<8} | {analise:<11} | {concluida:<10} | {tot_cat} ({perc_cat:.1f}%)")

    print("-" * 65)

    print("\n[2] INDICADORES GERAIS E PROPORÇÕES POR SITUAÇÃO")
    print(f"Total de Ocorrências Registradas: {total_ocorrencias}")
    for j, status in enumerate(STATUS_VALIDOS):
        perc_status = (status_totais[j] / total_ocorrencias) * 100
        print(f" - {status.capitalize():<12}: {status_totais[j]:02d} ocorrências ({perc_status:.1f}%)")

    tempo_medio = (soma_dias_conclusao / qtd_concluidas) if qtd_concluidas > 0 else 0
    print(f"\n[3] EFICIÊNCIA E ATENDIMENTO")
    print(f" - Demandas pendentes na Fila de Análise: {len(fila_analise)}")
    print(f" - Tempo médio simulado de conclusão: {tempo_medio:.1f} dias (baseado em {qtd_concluidas} demandas concluídas)")
    print("="*65)



# Menu interativo

def menu_principal():
    while True:
        print("\n--- MENU DO SISTEMA COMUNITÁRIO ---")
        print("1. Exibir Dashboard de Indicadores (Matriz e Estatísticas)")
        print("2. Listar todas as ocorrências")
        print("3. Consultar ocorrência por ID")
        print("4. Filtrar ocorrências (por Categoria e/ou Status)")
        print("5. Cadastrar nova ocorrência")
        print("6. Atualizar status de uma ocorrência")
        print("7. Ver histórico recente de alterações")
        print("8. Ver Fila de Análise pendente")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            exibir_indicadores()

        elif opcao == "2":
            filtrar_ocorrencias()

        elif opcao == "3":
            id_busca = input("Digite o ID da ocorrência (ex: 001): ").strip()
            consultar_id(id_busca)

        elif opcao == "4":
            print(f"Categorias disponíveis: {CATEGORIAS_VALIDAS}")
            categoria = input("Filtrar por categoria (ou Enter para ignorar): ").strip()
            print(f"Status disponíveis: {STATUS_VALIDOS}")
            status = input("Filtrar por status (ou Enter para ignorar): ").strip()
            filtrar_ocorrencias(categoria if categoria else None, status if status else None)

        elif opcao == "5":
            id_novo = input("Novo ID (ex: 015): ").strip()
            print(f"Categorias: {CATEGORIAS_VALIDAS}")
            categoria_nova = input("Categoria: ").strip()
            descricao_nova = input("Descrição do problema: ").strip()
            local_novo = input("Local genérico (ex: Praça Central): ").strip()
            dia_str = input("Dia simulado de abertura (número inteiro): ").strip()
            
            if dia_str.isdigit():
                cadastrar_ocorrencia(id_novo, categoria_nova, descricao_nova, local_novo, int(dia_str))
            else:
                print("[ERRO] O dia de abertura deve ser um número inteiro válido.")

        elif opcao == "6":
            id_att = input("ID da ocorrência a atualizar: ").strip()
            print(f"Status possíveis: {STATUS_VALIDOS}")
            novo_status = input("Novo status: ").strip()
            dia_str = input("Dia simulado da atualização (número inteiro): ").strip()
            obs = input("Observação breve: ").strip()
            
            if dia_str.isdigit():
                atualizar_status(id_att, novo_status, int(dia_str), obs)
            else:
                print("[ERRO] O dia deve ser um número inteiro válido.")

        elif opcao == "7":
            exibir_historico_att(8)

        elif opcao == "8":
            print(f"\n--- FILA DE ANÁLISE PENDENTE ---")
            if fila_analise:
                print("Próximos IDs a serem examinados:", " -> ".join(fila_analise))
            else:
                print("Nenhuma demanda aguardando análise na fila!")

        elif opcao == "0":
            print("Encerrando o Neighborhood Action Dashboard. Até logo!")
            break

        else:
            print("[ERRO] Opção inválida. Tente novamente.")

exibir_indicadores()
menu_principal()

