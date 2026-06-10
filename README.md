# Mission Control AI 🚀

##  Sobre o Projeto
O **Mission Control AI** é um sistema em Python desenvolvido para simular o monitoramento inteligente de uma missão espacial experimental (Global Solution 2026.1 - FIAP). O programa analisa dados estruturados de ciclos de monitoramento, calculando pontuações de risco, tendências de piora/melhora e emitindo alertas de contingência.

##  Equipe Davi Monteiro
* Davi Monteiro - RM: 573290

##  Regras de Alerta e Pontuação de Risco
Cada ciclo analisa 5 parâmetros essenciais. Cada parâmetro recebe uma classificação e uma pontuação:
* **NORMAL**: 0 pontos
* **ATENÇÃO**: 1 ponto
* **CRÍTICO**: 2 pontos

### Limites Utilizados:
1. **Temperatura:** < 18°C (Atenção) | 18°C a 30°C (Normal) | 31°C a 35°C (Atenção) | > 35°C (Crítico)
2. **Comunicação:** < 30% (Crítico) | 30% a 59% (Atenção) | >= 60% (Normal)
3. **Bateria:** < 20% (Crítico) | 20% a 49% (Atenção) | >= 50% (Normal)
4. **Oxigênio:** < 80% (Crítico) | 80% a 89% (Atenção) | >= 90% (Normal)
5. **Estabilidade:** < 40% (Crítico) | 40% a 69% (Atenção) | >= 70% (Normal)

### Classificação do Ciclo:
* **0 a 2 pontos:** MISSÃO ESTÁVEL
* **3 a 5 pontos:** MISSÃO EM ATENÇÃO
* **6 a 10 pontos:** MISSÃO CRÍTICA

