"""
Introduction to Artificial Intelligence, 89570, Bar Ilan University, ISRAEL

Student name:
Student ID:

"""

# multiAgents.py
# --------------
# Attribution Information: part of the code were created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# http://ai.berkeley.edu.
# We thank them for that! :)


import random, util, math

from connect4 import Agent


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxAgent, AlphaBetaAgent & ExpectimaxAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 1  # agent is always index 1
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class BestRandom(MultiAgentSearchAgent):

    def getAction(self, gameState):
        return gameState.pick_best_move()


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 1)
    """

    def min_max(self, current_state, current_dep, is_max):
        actions = current_state.getLegalActions(self.index)
        if current_dep == self.depth or actions is None:
            return self.evaluationFunction(current_state), None
        if is_max:
            max_val = float("-inf")
            best_act = ""
            for i in actions:
                val, state = self.min_max(current_state.generateSuccessor(0, i), current_dep + 1, False)
                if val >= max_val:
                    max_val = val
                    best_act=i
            return max_val, best_act
        else:
            min_val = float("inf")
            best_act=""
            for i in actions:
                val, state = self.min_max(current_state.generateSuccessor(0, i), current_dep + 1, True)
                if val <= min_val:
                    min_val = val
                    best_act = i
            return min_val, best_act

    def minMax(self, currentGameState, current_dep, max_or_min):
        actions = currentGameState.getLegalActions(self.index)
        if current_dep == self.depth or not actions:
            return self.evaluationFunction(currentGameState), None
        if max_or_min:
            return max(
                [(self.minMax(currentGameState.generateSuccessor(0, i), current_dep + 1, False)[0], i) for i
                 in actions])
        else:
            return min(
                [(self.minMax(currentGameState.generateSuccessor(0, i), current_dep + 1, True)[0], i) for i
                 in actions])

    def getAction(self, gameState):
        val, act = self.min_max(gameState, 0, True)
        # val, act = self.minMax(gameState,0, True)
        return act


class AlphaBetaAgent(MultiAgentSearchAgent):
    def alpha_beta_min_max(self, current_state, current_dep, is_max):
        actions = current_state.getLegalActions(self.index)
        if current_dep == self.depth or actions is None:
            return self.evaluationFunction(current_state), None
        if is_max:
            max_val = float("-inf")
            best_act = ""
            for i in actions:
                val, state = self.min_max(current_state.generateSuccessor(0, i), current_dep + 1, False)
                if val >= max_val:
                    max_val = val
                    best_act=i
            return max_val, best_act
        else:
            min_val = float("inf")
            best_act=""
            for i in actions:
                val, state = self.min_max(current_state.generateSuccessor(0, i), current_dep + 1, True)
                if val <= min_val:
                    min_val = val
                    best_act = i
            return min_val, best_act

    def getAction(self, gameState):
        val, act = self.min_max(gameState, 0, True)



class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()
