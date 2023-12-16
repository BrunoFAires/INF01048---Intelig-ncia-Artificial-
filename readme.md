# Regressão Linear
`b`: 1
`w`: 0
`alpha`: 0.095
`num_iterations`: 100
`Melhor erro quadrático médio`: 0.2951436390499173
Após realizar diversos testes variando os parâmetros: coeficientes (b e w), taxa de aprendizado (alpha) e número de iterações foi identificado uma configuração específica que resultou no menor EQM. Porém, a diferença em relação aos demais foi bem pequena, algo na ordem de 10^-17, o que não descarta essa como a melhor configuração para o modelo fornecido em relação às demais que foram testadas. 

# Redes Neurais

## Mnist
`Classes:` 10
`Amostras:` 60000
`Tamanho das Imagens`: 28x28x1
`Acurácia:` 99.13%
`Tempo de Treinamento:` 516s
A solução encontrada para este dataset foi a alternância entre camadas convolucionais e maxpooling seguido de uma camada de flatten e duas camadas densamente conectadas.  Durante o treinamento, a acurácia se manteve na maioria das épocas acima de 99% o que gerou uma desconfiança de que isso se encaminharia para um overfitting. Entretando, não foi o que aconteceu, uma vez que o conjunto de teste retornou uma acurácia semelhante. Por conta da alta acurácia e tempo prolongado para o treinamento, imaginei que retirando uma camada convolucional e maxpooling - visando menos processamento - teria um resultado semelhante em menos tempo, conforme esperado, o tempo reduziu drasticamente (278s) e acurácia esteve em 99%.

## Fashion Mnist
`Classes:` 10
`Amostras:` 60000
`Tamanho das Imagens`: 28x28x1
`Acurácia:` 90.89%
`Tempo de Treinamento:` 430s

## Cifar-10
`Classes:` 10
`Amostras:` 50000
`Tamanho das Imagens`: 32x32x3
`Acurácia:` 63.82%
`Tempo de Treinamento:` 350s

## Cifar-100
`Classes:` 100
`Amostras:` 50000
`Tamanho das Imagens`: 32x32x3
`Acurácia:` 41.47%
`Tempo de Treinamento:` 3585s
Este foi o dataset mais complexo e desafiador, uma vez que de entrada temos imagens coloridas com tamanho de 32x32 pixels e possuindo cem classes de saída. A primeira versão teve um péssimo resultado mesmo que o tempo de treinamento fosse longo. Não havia adicionado nenhuma camada de maxpooling, então imaginei que adicionando algumas tornaria o treinamento mais rápido já que diminuiria o a quantidade de entradas, foi o que aconteceu, entretando, não obtive um resultado satisfatório com relação à acurácia. Após algumas pesquisas, vi que poderia utilizar uma camada de batch normalization para tornar o treinamento mais rápido e estável. Além disso, adicionei uma camada de dropout que é utilizada para previnir o overfitting. Após praticamente uma hora de treinamento, obtive uma melhor acurácia, estabilizando em 41.47%

