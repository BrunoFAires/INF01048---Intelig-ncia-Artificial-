# Relatório trabalho 4
## Integrantes
Bruno Ferreira Aires - 00323680 - Turma B<br>
Clayton Kaua Oliveira Barcelos - 00334132 Turma A<br>
Henrique Bernardes Felizzola - 00311458 Turma A<br>
# Avaliação
## Tic-Tac-Toe (Misere)
A partir do desenvolvimento do nosso agente, foi possível perceber alguns pontos interessantes.<br> 
Primeiramente, quando iniciávamos a partida o agente sempre ganhava. Porém, quando o agente começava as partidas elas, majoritariamente, terminaram empatadas. Em relação às jogadas aleatórias, o agente acabou ganhando todas as partidadas(foram executadas 50 partidas). Por fim, competindo consigo mesmo, todas as 50 partidas terminaram empatadas.
## Othello
### Desenvolvemos as seguintes Heurísticas para o trabalho:
- Contagem de peças:
  - Calcula a diferença no número de peças de cada jogador no tabuleiro. O jogador que tiver o maior número de peças terá uim melhor desempenho.
- Valor posicional
  - Esta heurística atribui valores a cada posição no tabuleiro com base na sua importância estratégica considerando a qualidade de cada posição do tabuleiro.
- Mobilidade
  - Considera o número de movimentos legais disponíveis para cada jogador, sendo que quanto mais posições disponíveis, melhor é a posição do jogador.<br>


No geral, todas as heurísticas tiveram um bom desempenho considerando o delay padrão(5 segundos) e 5 de profundidade. Porém, a heurística que rodou em menor tempo foi a de Valor Posicional. Acreditamos que isso se dá pelo fato dela priorizar ocupar as posições mais vantajosas como os cantos, por exemplo.<br>
O uso de ferramentas de IA generativa não foi muito relevante. Utilizamos, basicamente, para realizar a verificação de erros de sintaxe e geração de pseudo-códigos. Para a heurística customizada, por exemplo, utilizamos o seguinte paper para o desenvolvimento da mesma: https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf
