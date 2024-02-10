import random
from typing import Tuple
from ..othello.gamestate import GameState
from ..othello.board import Board
from .minimax import minimax_move

# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state) -> Tuple[int, int]:
    """
    Returns a move for the given game state
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada 
    # Remova-o e coloque uma chamada para o minimax_move (que vc implementara' no modulo minimax).
    # A chamada a minimax_move deve receber sua funcao evaluate como parametro.

    return minimax_move(state, max_depth=5, eval_func=evaluate_custom)


def evaluate_custom(state, player:str) -> float:
    """
    Evaluates an othello state from the point of view of the given player. 
    If the state is terminal, returns its utility. 
    If non-terminal, returns an estimate of its value based on your custom heuristic
    :param state: state to evaluate (instance of GameState)
    :param player: player to evaluate the state for (B or W)
    """
    max_player = player
    min_player = 'B' if player == 'W' else 'W'
    max_player_mobility = len(state.board.legal_moves(player))
    min_player_mobility = len(state.board.legal_moves(min_player))

    total_mobility = max_player_mobility +  min_player_mobility
    
    if total_mobility != 0:
        return 100 * (max_player_mobility - min_player_mobility) / total_mobility
    else:
        return 0  # Or you can return a special value to indicate the condition when both players have no legal moves.

