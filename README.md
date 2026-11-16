# Neighborhood Action Dashboard — Global Solution 2026.2 (CitizenTech)

Protótipo funcional de um painel comunitário desenvolvido em Python puro para registrar, organizar, consultar e acompanhar demandas de infraestrutura e conservação no bairro simulado **Vila Aurora**.

## 👥 Integrantes da Equipe
* **Vinicius Medeiros Dias** — RM 576229
* **Vitor Matheus Dalcanale** — RM 576820
* **Lucas Bernardes Santana** — RM 575192
* **Isabelle Marques** — RM 575268
* **Nathan Kaique Soares Gomes** — RM 575192

---

## 🏙️ Contexto, Problema e Público Beneficiado
* **Comunidade Simulada:** Bairro Vila Aurora.
* **Problema:** Problemas cotidianos de infraestrutura urbana (iluminação pública, acessibilidade, limpeza e conservação de espaços coletivos) costumam ser relatados de forma dispersa pelos moradores, dificultando a definição de prioridades e o acompanhamento do andamento das solicitações.
* **Público Beneficiado:** Moradores da comunidade, lideranças locais e equipes de zeladoria comunitária que necessitam de transparência, organização e indicadores claros sobre as demandas do bairro.
* **Origem dos Dados:** Os dados simulados (12 ocorrências iniciais + 1 registro inconsistente + 10 eventos históricos) estão **embutidos diretamente no código-fonte (`src/sistema.py`)** em estruturas nativas, dispensando o uso da pasta `data/` e arquivos CSV/TXT externos.

---

## 📁 Estrutura do Repositório
```text
├── README.md              # Documentação principal do projeto
├── src/
│   └── sistema.py         # Código-fonte completo em Python puro (dados embutidos)
└── docs/
    ├── relatorio.pdf      # Relatório técnico detalhado (4 a 8 páginas)
    ├── link_video.txt     # Endereço completo do vídeo no YouTube
    └── uso_ia.md          # Registro transparente do apoio de Inteligência Artificial
```

## 🗂️ Estruturas de Dados Utilizadas e Justificativas

1. **Dicionário (`ocorrencias_id` - Tabela Hash):** Armazena as ocorrências indexadas pelo código único (`id`), garantindo consulta direta e instantânea O(1) na busca por identificador.
2. **Lista (`ocorrencias_lista`):** Mantém a coleção sequencial completa de registros para permitir percursos lineares em filtros combinados e cálculos de indicadores.
3. **Fila FIFO (`fila_analise`):** Organiza os IDs das demandas com status `"aberta"` por ordem de chegada (*First In, First Out*), assegurando justiça e ordem cronológica na triagem.
4. **Pilha LIFO (`historico_att`):** Registra as mudanças de status cronologicamente e permite visualizar os eventos mais recentes a partir do topo (*Last In, First Out*).
5. **Hierarquia (`hierarquia`):** Estrutura aninhada no formato `Bairro ("Vila Aurora") -> Categoria -> Lista de IDs`, facilitando o agrupamento temático das demandas da região.
6. **Matriz Bidimensional (`matriz_resumo`):** Lista de listas $4 \times 3$ cruzando **Categorias (linhas)** $\times$ **Status (colunas)** para sintetizar a distribuição quantitativa do painel.

## ⚙️ Regras Lógicas e Expressões Booleanas
O sistema utiliza estruturas condicionais (`if`, `elif`, `else`) e operadores booleanos (`and`, `or`, `not`) para garantir a integridade dos dados:

* **Auditoria de Inconsistências:** Na inicialização, o registro `"013"` (sem categoria definida) é detectado e reclassificado automaticamente para `"conservação"`.
* **Exemplo de Expressão Booleana Documentada (Auditoria):**

```python
if (ocorrencia["categoria"] not in CATEGORIAS_VALIDAS) or (not ocorrencia["descricao"]) or (not ocorrencia["local"]):
```

  *Explicação:* A condição avalia três possíveis falhas simultaneamente usando o operador `or`. Se a categoria não pertencer à lista permitida (`not in`), **OU** a descrição estiver vazia (`not`), **OU** o local estiver vazio (`not`), o sistema bloqueia a entrada ou dispara o alerta de inconsistência, impedindo que dados incompletos distorçam os indicadores.
* **Filtros Combinados:** Utiliza o operador `and` (`if condicao_categoria and condicao_status:`) para retornar apenas registros que satisfaçam ambos os critérios informados pelo usuário.

## 📊 Indicadores Implementados e Interpretação

* **Totais e Proporções:** Quantidade absoluta e percentual de ocorrências por categoria e por situação (`aberta`, `em análise`, `concluída`), calculados por meio de laços e acumuladores.
* **Tempo Médio Simulado de Conclusão:** Calculado a partir da diferença entre os dias de encerramento e abertura das demandas finalizadas
* **Pendências na Fila:** Contagem dinâmica de demandas aguardando triagem (`len(fila_analise)`).
* **Interpretação dos Resultados:** No cenário inicial simulado (14 ocorrências após o cadastro de demonstração), observa-se equilíbrio entre as demandas de **Iluminação** e **Conservação** (28,6% cada), apontando necessidade prioritária de manutenção elétrica e estrutural nas vias e praças, com tempo médio de resolução de **2,3 dias** nas demandas concluídas.

## ▶️ Como Executar
Certifique-se de ter o **Python 3** instalado. No terminal, a partir da pasta raiz do repositório, execute:

```bash
python src/sistema.py
```

### Exemplo de Uso e Saída no Terminal
Ao iniciar, o sistema realiza a auditoria automática do registro `013`, testa o cadastro da ocorrência `014`, atualiza seu status para `"em análise"`, exibe o dashboard inicial e abre o menu interativo:

```text
[ALERTA DE INCONSISTÊNCIA] Registro ID '013' possui dados ausentes ou categoria inválida ('').
 -> Correção aplicada: ID '013' reclassificado para 'conservação'.
[SUCESSO] Ocorrência '014' (iluminação) cadastrada e adicionada às estruturas!
[ATUALIZADO] ID '014': 'aberta' -> 'em análise' (Dia 14).
```


## 🔒 Acessibilidade, Inclusão e Privacidade

* **Privacidade (LGPD):** Nenhum dado pessoal, CPF, telefone ou endereço residencial exato é coletado. Todas as ocorrências utilizam localidades públicas genéricas (ex: *"Praça Central"*, *"Rua A"*).
* **Acessibilidade e Inclusão:** A categoria dedicada de **Acessibilidade** prioriza demandas como rampas, calçadas e sinais sonoros. A interface textual utiliza rótulos claros, separadores visuais e mensagens de erro explicativas para facilitar a leitura por leitores de tela.

---

## 🎥 Vídeo de Apresentação

* **Link do YouTube (Não Listado):** []

---

## 🧠 Conclusões, Limitações e Aprendizados

* **Aprendizados:** O projeto consolidou a aplicação prática de estruturas de dados nativas e lógica booleana na resolução de problemas urbanos reais sem dependência de bibliotecas externas.
* **Limitações:** Por operar inteiramente em memória RAM (sem persistência em banco de dados ou arquivos externos), os novos cadastros realizados durante a execução são reiniciados ao encerrar o programa.
