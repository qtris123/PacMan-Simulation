# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    seen = set([problem.getStartState()])
    def recurSearch(curLoc, actions):
        if problem.isGoalState(curLoc):
            return actions
        for successor in reversed(problem.getSuccessors(curLoc)): # list of triplet(s)
            next_loc = successor[0] 
            if next_loc not in seen:
                seen.add(next_loc)
                next_actions = actions.copy()
                next_actions.append(successor[1])
                ans =  recurSearch(next_loc, next_actions)
                
                if ans is not None:
                    return ans
        return None
    ans = recurSearch(problem.getStartState(), [])
    return ans
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    seen = set([problem.getStartState()])
    q_ = util.Queue()
    q_.push((problem.getStartState(), []))
    seen = set([problem.getStartState()])
    while not q_.isEmpty():
        cur, actions = q_.pop()
        if problem.isGoalState(cur):
            return actions
        for suc in problem.getSuccessors(cur):
            next_loc = suc[0]
            if next_loc not in seen:
                seen.add(next_loc)
                next_actions = actions.copy()
                next_actions.append(suc[1])
                q_.push((next_loc, next_actions))
    return []
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # seen = set()
    # q_ = util.PriorityQueue()
    # q_.push((problem.getStartState(), [], 0), 0)
    # while not q_.isEmpty():
    #     cur, actions, cost = q_.pop()
    #     if cur in seen:
    #         continue
    #     seen.add(cur)
    #     if problem.isGoalState(cur):
    #         return actions
    #     for suc in problem.getSuccessors(cur):
    #         next_loc = suc[0]
    #         seen.add(next_loc)
    #         next_actions = actions.copy()
    #         next_actions.append(suc[1])
    #         new_cost = cost + suc[2]
    #         q_.push((next_loc, next_actions, new_cost), new_cost)

    # return None
    "*** YOUR CODE HERE ***"
    q_ = util.PriorityQueue()
    q_.push((problem.getStartState(), [], 0), 0)
    seen = {}
    while not q_.isEmpty():
        cur, actions, cost = q_.pop()
        if cur in seen and seen[cur] <= cost:
            continue
        seen[cur] = cost
        if problem.isGoalState(cur):
            return actions
        for suc in problem.getSuccessors(cur):
            next_loc = suc[0]
            next_actions = actions.copy()
            next_actions.append(suc[1])
            new_cost = cost + suc[2]
            if next_loc not in seen or new_cost < seen[next_loc]:
                q_.push((next_loc, next_actions, new_cost), new_cost)

    return []
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    q_ = util.PriorityQueue()
    q_.push((problem.getStartState(), [], 0), 0 + heuristic(problem.getStartState(),problem))
    seen = {}
    while not q_.isEmpty():
        cur, actions, cost = q_.pop()
        if cur in seen and seen[cur] <= cost:
            continue
        seen[cur] = cost
        if problem.isGoalState(cur):
            return actions
        for suc in problem.getSuccessors(cur):
            next_loc = suc[0]
            next_actions = actions.copy()
            next_actions.append(suc[1])
            new_cost = cost + suc[2]
            if next_loc not in seen or new_cost < seen[next_loc]:
                q_.push((next_loc, next_actions, new_cost), new_cost + heuristic(next_loc, problem))

    return []
    util.raiseNotDefined()


# Abbreviations
# bfs = breadthFirstSearch
dfs = depthFirstSearch
# astar = aStarSearch
# ucs = uniformCostSearch
