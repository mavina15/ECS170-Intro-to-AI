from copy import deepcopy

# need TilesNode.is_goal
# need TilesNode.generate_children


class TilesNode:

    def __init__(self, state, parent=None,):
        self.state = state
        self.parent = parent

    def is_goal(self) -> bool:

        return self.state == [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]

    def find_empty_space(self) -> tuple[int, int]:

        for i, row in enumerate(self.state):
            for j, col in enumerate(row):
                if col == 0:
                    return i, j

    def swap_tiles(self, row1, col1, row2, col2):

        new_state = deepcopy(self.state)
        new_state[row1][col1], new_state[row2][col2] = (
            new_state[row2][col2],
            new_state[row1][col1],
        )
        return new_state

    def generate_children(self) -> list["TilesNode"]:

        children = []

        empty_row, empty_col = self.find_empty_space()

        # left move
        if empty_col > 0:
            new_state = self.swap_tiles(
                empty_row, empty_col, empty_row, empty_col - 1)
            children.append(TilesNode(state=new_state, parent=self))

        # right move
        if empty_col < 3:
            new_state = self.swap_tiles(
                empty_row, empty_col, empty_row, empty_col + 1)
            children.append(TilesNode(state=new_state, parent=self))

        # move up
        if empty_row > 0:
            new_state = self.swap_tiles(
                empty_row, empty_col, empty_row - 1, empty_col)
            children.append(TilesNode(state=new_state, parent=self))

        # move down
        if empty_row < 3:
            new_state = self.swap_tiles(
                empty_row, empty_col, empty_row + 1, empty_col)
            children.append(TilesNode(state=new_state, parent=self))

        return children

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.state)

    def __repr__(self) -> str:
        return self.__str__()

    def get_path(self) -> list["TilesNode"]:

        path = []
        current_node = self
        while current_node:
            path.append(current_node)
            current_node = current_node.parent
        return path[::-1]

    def __eq__(self, other):
        if isinstance(other, TilesNode):
            return self.state == other.state
        return False

    def __hash__(self):
        return hash(tuple(map(tuple, self.state)))

    def is_solvable(self):

        flat_state = [tile for row in self.state for tile in row if tile != 0]

        inversions = 0
        for i in range(len(flat_state)):
            for j in range(i + 1, len(flat_state)):
                if flat_state[i] > flat_state[j]:
                    inversions += 1

        return inversions % 2 == 0


# START HERE


class TilesNode:
    """A class to represent a node in the Fifteen-Tile Puzzle.

    Parameters
    ----------
    state: list[list[int]]
        An array (list of list) of ints representing the initial state of the puzzle.
        This array should contain integers from 0 to 15 separated by spaces.
        The integer 0 represents the empty space in the puzzle.

    parent : Node, optional
        The parent node of the current node. The default is None.
    """

    # init method: class constructor method and initilizes TilesNode object
    def __init__(
        self,

        # parameters
        # 2D list rep current puzzle config
        state,

        # optional specification of parent node of current node
        parent=None,
    ):
        self.state = state
        self.parent = parent

        # checks if current puzzle node is goal node, 4x4 grid
    def is_goal(self) -> bool:
        goal_state = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0]
        ]

        # check if every index in self matches to the goal state
        return all(self.state[i][j] == goal_state[i][j] for i in range(len(self.state)) for j in range(len(self.state[i])))

        # finds rows and column indices of 0 of current puzzle node
    def find_empty_space(self) -> tuple[int, int]:
        """Helper function to find the empty space in the current state.

        You don't need to use this function, but it may be helpful.

        Returns
        -------
        empty_row : int
            The row index of the empty space.

        empty_col : int
            The column index of the empty space.
        """
        for i, row in enumerate(self.state):
            for j, col in enumerate(row):
                if col == 0:
                    return i, j

        # creates new puzzle node by swapping two tile positions
    def swap_tiles(self, row1, col1, row2, col2):
        """
        Helper function to swap two tiles in the current state.

        You don't need to use this function, but it may be helpful.

        """
        new_state = deepcopy(self.state)
        new_state[row1][col1], new_state[row2][col2] = (
            new_state[row2][col2],
            new_state[row1][col1],
        )
        return new_state

        # genrates and returns list of child nodes (new puzzle nodes) reachable from current node by moving tiles
    def get_children(self) -> list["TilesNode"]:
        children = []
        empty_row, empty_col = self.find_empty_space()

        # valid movies (left, right, up, down)
        possible_moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]

        for move_row, move_col in possible_moves:
            new_row, new_col = empty_row + move_row, empty_col + move_col

            # Check if the new position is within bounds
            if 0 <= new_row < len(self.state) and 0 <= new_col < len(self.state[0]):
                # Create a new state by swapping the empty space with the adjacent tile
                new_state = self.swap_tiles(
                    empty_row, empty_col, new_row, new_col)
                new_child = TilesNode(new_state, parent=self)
                children.append(new_child)

        return children

        # string rep of puzzle node, easily reps node

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.state)

    def __repr__(self) -> str:
        return self.__str__()

        # backtracks from goal to initial node, returns list of TilesNode objects rep path of puzzle nodes leading to goal
    def get_path(self) -> list["TilesNode"]:
        """
        Once a goal node is found, this function can be used to backtrack.

        Be sure to set .parent correctly when creating child nodes for this to work.

        You don't need to use this function, but it may be helpful.
        """
        path = []
        current_node = self
        while current_node:
            path.append(current_node)
            current_node = current_node.parent
        return path[::-1]

        # compares 2 TilesNode objects for equality
    def __eq__(self, other):
        if isinstance(other, TilesNode):
            return self.state == other.state
        return False

        # generates hash value for TilesNode based on node
    def __hash__(self):
        return hash(tuple(map(tuple, self.state)))

        # checks if current puzzle node can be solved, based on number of inversions in puzzle
    def is_solvable(self):
        """
        Check if the current state is solvable.
        In a solvable state, the number of inversions must be even.

        You don't need to use this function, but it may be helpful.
        """
        flat_state = [tile for row in self.state for tile in row if tile != 0]

        inversions = 0
        for i in range(len(flat_state)):
            for j in range(i + 1, len(flat_state)):
                if flat_state[i] > flat_state[j]:
                    inversions += 1

                # if number of inversions is even -> puzzle is solvable
        return inversions % 2 == 0
