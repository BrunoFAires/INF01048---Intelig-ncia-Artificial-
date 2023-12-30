import math
def compute_mse(b, w, data):
    """
    Calcula o erro quadratico medio
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :return: float - o erro quadratico medio
    """
    sum = 0

    for d in data:
        predictValue = w*d[0] + b
        diff = (predictValue - d[1])*(predictValue - d[1])
        sum += diff
    mse = sum / data.shape[0]

    return mse

def step_gradient(b, w, data, alpha):
    """
    Executa uma atualização por descida do gradiente  e retorna os valores atualizados de b e w.
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :return: float,float - os novos valores de b e w, respectivamente
    """
    dW = 0
    dB = 0

    for d in data:
        dW += d[0]*((w*d[0]+b)-d[1])
        dB += ((w*d[0]+b)-d[1])
    dB = (1/ data.shape[0]) *2 *dB
    dW = (1/ data.shape[0]) * 2*dW

    newB = b - alpha*dB
    newW = w - alpha*dW

    return newB, newW

def fit(data, b, w, alpha, num_iterations):
    """
    Para cada época/iteração, executa uma atualização por descida de
    gradiente e registra os valores atualizados de b e w.
    Ao final, retorna duas listas, uma com os b e outra com os w
    obtidos ao longo da execução (o último valor das listas deve
    corresponder à última época/iteração).

    :param data: np.array - matriz com o conjunto de dados, x na coluna 0 e y na coluna 1
    :param b: float - bias (intercepto da reta)
    :param w: float - peso (inclinacao da reta)
    :param alpha: float - taxa de aprendizado (a.k.a. tamanho do passo)
    :param num_iterations: int - numero de épocas/iterações para executar a descida de gradiente
    :return: list,list - uma lista com os b e outra com os w obtidos ao longo da execução
    """
    bRegister = [b]
    wRegister = [w]
    for i in range(num_iterations):
        newB, newW = step_gradient(b, w, data, alpha)
        bRegister.append(newB)
        wRegister.append(newW)
        w = newW
        b = newB

    return bRegister, wRegister