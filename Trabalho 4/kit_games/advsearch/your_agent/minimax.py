import random
from typing import Tuple, Callable



def minimax_move(state, max_depth:int, eval_func:Callable) -> Tuple[int, int]:
    """
    Returns a move computed by the minimax algorithm with alpha-beta pruning for the given game state.
    :param state: state to make the move (instance of GameState)
    :param max_depth: maximum depth of search (-1 = unlimited)
    :param eval_func: the function to evaluate a terminal or leaf state (when search is interrupted at max_depth)
                    This function should take a GameState object and a string identifying the player,
                    and should return a float value representing the utility of the state for the player.
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """

    def max_value(state, alpha: float, beta: float, depth: int, initial) -> float:
        if depth == 0 or state.is_terminal():
            return eval_func(state, initial.player)

        max_eval = float('-inf')
        for move in state.legal_moves():
            new_state = state.next_state(move)
            eval_score = min_value(new_state, alpha, beta, depth - 1, initial)
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, max_eval)
            if beta <= alpha:
                break  # Beta cutoff
        return max_eval

    def min_value(state, alpha: float, beta: float, depth: int, initial) -> float:
        if depth == 0 or state.is_terminal():
            return eval_func(state, initial.player)

        min_eval = float('inf')
        for move in state.legal_moves():
            new_state = state.next_state(move)
            eval_score = max_value(new_state, alpha, beta, depth - 1, initial)
            min_eval = min(min_eval, eval_score)
            beta = min(beta, min_eval)
            if beta <= alpha:
                break  # Alpha cutoff
        return min_eval

    best_move = None
    best_score = float('-inf')
    alpha = float('-inf')
    beta = float('inf')

    for move in state.legal_moves():
        new_state = state.next_state(move)
        eval_score = min_value(new_state, alpha, beta, max_depth - 1, state)
        if eval_score > best_score:
            best_score = eval_score
            best_move = move
        alpha = max(alpha, best_score)

    return best_move