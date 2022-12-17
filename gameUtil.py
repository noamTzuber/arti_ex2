PLAYER = 0
AI = 1
ROW_COUNT = 6
COLUMN_COUNT = 7
WINDOW_LENGTH = 4
EMPTY = 0
SQUARESIZE = 100
RADIUS = int(SQUARESIZE/2 -5)
BLUE = (0,0,255)
RED = (255,0,0)
YELLOW = (255,255,0)
BLACK = (0,0,0)

PLAYER_PIECE = 1
AI_PIECE = 2
# def minimax(state, depth, maximizingPlayer):
#     if depth == 0 or state.isWin() or state.isLose():
#         return state.getScore(), None
#
#     bestAction = None
#     if maximizingPlayer:
#         value = float("-inf")
#         for action in state.getLegalActions():
#             nextState = state.generateSuccessor(0, action)
#             nextScore, _ = minimax(nextState, depth - 1, False)
#             if nextScore > value:
#                 value = nextScore
#                 bestAction = action
#         return value, bestAction
#     else:
#         value = float("inf")
#         for action in state.getLegalActions():
#             nextState = state.generateSuccessor(0, action)
#             nextScore, _ = minimax(nextState, depth - 1, True)
#             if nextScore < value:
#                 value = nextScore
#                 bestAction = action
#         return value, bestAction