# ==========================================
# Mission Control AI - Global Solution 2026.1
# ==========================================


NOME_MISSAO = "Orion Test Alpha"
NOME_EQUIPE = "Davi Monteiro"


areas_monitoradas = [
    "Temperatura interna",
    "Comunicação com a base",
    "Sistema de energia",
    "Suporte de oxigênio",
    "Estabilidade operacional"
]


# Ordem: [temperatura, comunicacao, bateria, oxigenio, estabilidade]
dados_missao = [
    [24, 92, 88, 96, 90],  # Ciclo 1 - Estável
    [27, 80, 72, 94, 85],  # Ciclo 2 - Estável
    [31, 65, 58, 91, 70],  # Ciclo 3 - Atenção
    [36, 42, 38, 87, 55],  # Ciclo 4 - Crítico
    [39, 28, 19, 78, 35],  # Ciclo 5 - Crítico extremo
    [34, 55, 32, 82, 50]   # Ciclo 6 - Tentativa de recuperação
]

# ==========================================
# Funções de Análise de Parâmetros
# Retornam uma tupla: (Status, Pontos de Risco)
# ==========================================

def analisar_temperatura(t):
    if 18 <= t <= 30: return "NORMAL", 0
    elif t < 18 or (30 < t <= 35): return "ATENÇÃO", 1
    else: return "CRÍTICO", 2

def analisar_comunicacao(c):
    if c >= 60: return "NORMAL", 0
    elif 30 <= c <= 59: return "ATENÇÃO", 1
    else: return "CRÍTICO", 2

def analisar_bateria(b):
    if b >= 50: return "NORMAL", 0
    elif 20 <= b <= 49: return "ATENÇÃO", 1
    else: return "CRÍTICO", 2

def analisar_oxigenio(o):
    if o >= 90: return "NORMAL", 0
    elif 80 <= o <= 89: return "ATENÇÃO", 1
    else: return "CRÍTICO", 2

def analisar_estabilidade(e):
    if e >= 70: return "NORMAL", 0
    elif 40 <= e <= 69: return "ATENÇÃO", 1
    else: return "CRÍTICO", 2

# ==========================================
# Funções de Lógica de Negócio
# ==========================================

def classificar_ciclo(pontos):
    if pontos <= 2: return "MISSÃO ESTÁVEL"
    elif pontos <= 5: return "MISSÃO EM ATENÇÃO"
    else: return "MISSÃO CRÍTICA"

def analisar_tendencia(risco_inicial, risco_final):
    if risco_final > risco_inicial:
        return "A missão apresentou tendência de piora."
    elif risco_final < risco_inicial:
        return "A missão apresentou tendência de melhora."
    else:
        return "A missão permaneceu estável em relação ao início."

def identificar_area_mais_afetada(pontuacoes_acumuladas):
    maior_pontuacao = max(pontuacoes_acumuladas)
    indice_maior = pontuacoes_acumuladas.index(maior_pontuacao)
    return areas_monitoradas[indice_maior]

def gerar_recomendacao(classificacao):
    if classificacao == "MISSÃO ESTÁVEL":
        return "Manter operação normal e continuar monitoramento."
    elif classificacao == "MISSÃO EM ATENÇÃO":
        return "Monitorar sistemas em atenção e preparar plano de contingência."
    else:
        return "Ativar modo de segurança e priorizar suporte à vida, energia e comunicação."

# ==========================================
# Função Principal (Relatório e Execução)
# ==========================================

def gerar_relatorio_final():
    print("="*50)
    print(" MISSION CONTROL AI ".center(50, "="))
    print("="*50)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("="*50)

    pontuacoes_por_area = [0, 0, 0, 0, 0]
    historico_risco_ciclos = []
    
    
    soma_t = soma_c = soma_b = soma_o = soma_e = 0

 
    for i in range(len(dados_missao)):
        ciclo = dados_missao[i]
        t, c, b, o, e = ciclo[0], ciclo[1], ciclo[2], ciclo[3], ciclo[4]
        
        soma_t += t
        soma_c += c
        soma_b += b
        soma_o += o
        soma_e += e

      
        status_t, pts_t = analisar_temperatura(t)
        status_c, pts_c = analisar_comunicacao(c)
        status_b, pts_b = analisar_bateria(b)
        status_o, pts_o = analisar_oxigenio(o)
        status_e, pts_e = analisar_estabilidade(e)

       
        pontuacoes_por_area[0] += pts_t
        pontuacoes_por_area[1] += pts_c
        pontuacoes_por_area[2] += pts_b
        pontuacoes_por_area[3] += pts_o
        pontuacoes_por_area[4] += pts_e

       
        pontuacao_ciclo = pts_t + pts_c + pts_b + pts_o + pts_e
        historico_risco_ciclos.append(pontuacao_ciclo)
        classificacao = classificar_ciclo(pontuacao_ciclo)

      
        print(f"\nCICLO {i + 1}")
        print(f"Temperatura:  {t}°C | {status_t}")
        print(f"Comunicação:  {c}%   | {status_c}")
        print(f"Bateria:      {b}%   | {status_b}")
        print(f"Oxigênio:     {o}%   | {status_o}")
        print(f"Estabilidade: {e}%   | {status_e}")
        print(f"Pontuação de risco do ciclo: {pontuacao_ciclo}")
        print(f"Classificação do ciclo: {classificacao}")
        print(f"Recomendação: {gerar_recomendacao(classificacao)}")

  
    qtd_ciclos = len(dados_missao)
    maior_risco = max(historico_risco_ciclos)
    ciclo_mais_critico = historico_risco_ciclos.index(maior_risco) + 1
    risco_medio = sum(historico_risco_ciclos) / qtd_ciclos
    qtd_ciclos_criticos = sum(1 for risco in historico_risco_ciclos if risco >= 6)
    
    tendencia = analisar_tendencia(historico_risco_ciclos[0], historico_risco_ciclos[-1])
    area_mais_afetada = identificar_area_mais_afetada(pontuacoes_por_area)

    print("\n" + "="*50)
    print(" RELATÓRIO FINAL DA MISSÃO ".center(50, "="))
    print("="*50)
    print(f"Missão: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {qtd_ciclos}\n")

    print(f"Média de temperatura: {soma_t/qtd_ciclos:.2f}°C")
    print(f"Média de comunicação: {soma_c/qtd_ciclos:.2f}%")
    print(f"Média de bateria: {soma_b/qtd_ciclos:.2f}%")
    print(f"Média de oxigênio: {soma_o/qtd_ciclos:.2f}%")
    print(f"Média de estabilidade: {soma_e/qtd_ciclos:.2f}%\n")

    print(f"Ciclo mais crítico: Ciclo {ciclo_mais_critico}")
    print(f"Maior pontuação de risco: {maior_risco}")
    print(f"Risco médio da missão: {risco_medio:.2f}")
    print(f"Quantidade de ciclos críticos: {qtd_ciclos_criticos}\n")

    print("Tendência da missão:")
    print(tendencia, "\n")

    print("Pontuação acumulada por área:")
    for i in range(5):
        print(f"- {areas_monitoradas[i]}: {pontuacoes_por_area[i]} pontos")

    print(f"\nÁrea mais afetada:\n> {area_mais_afetada}\n")

    classificacao_final = classificar_ciclo(risco_medio)
    print(f"Classificação final da missão (Média): \n{classificacao_final}\n")

    print("Conclusão:")
    if tendencia == "A missão apresentou tendência de piora.":
        print("A missão apresentou instabilidade relevante. Recomenda-se revisão imediata dos protocolos de contingência na área mais afetada.")
    else:
        print("A missão conseguiu manter parâmetros aceitáveis de recuperação. Continuar protocolos padrão.")
    print("="*50)

# Executar o programa
if __name__ == "__main__":
    gerar_relatorio_final()
