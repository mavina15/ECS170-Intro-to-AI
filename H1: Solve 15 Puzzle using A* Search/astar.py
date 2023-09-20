# imports TilesNode which represents the 4 x 4 puzzle
from tiles import TilesNode

# imports from std lib, used to store and prioritize puzzle during A* search
from queue import PriorityQueue

# function calculates hueristic value for puzzle node using Manhattan distance
def heuristic(node: TilesNode) -> int:
    
    total_distance = 0
    for i in range(len(node.state)):
        for j in range(len(node.state[i])):
            tile = node.state[i][j]
            if tile != 0:
                goal_row = (tile - 1) // len(node.state)
                goal_col = (tile - 1) % len(node.state[i])
                
				# Manhattan distance = sums distance between each tile's current and goal position
                total_distance += abs(i - goal_row) + abs(j - goal_col)
    return total_distance

# A* star search function, 2 parameters -> root + huerisitic
def AStar(root, heuristic: callable) -> list[TilesNode] or None:
    
	# initlizes data structures
	# priority wueue stores puzzle states that will be explored, prioritized by f_score
    unexplored = PriorityQueue()
    counter = 0
    unexplored.put((heuristic(root), counter, root))
    
	# stores puzzle nodes already explored
    explored = set()
    
	# stores cost to reach puzzle to root node
    g_score = {root: 0}
    
	# stores estimated total cost (g_score + hueristic) to reach puzzle to root node
    f_score = {root: heuristic(root)}
    
	# loop that explores unexplored priority queue
    while not unexplored.empty():
        
		# each iteration gets puzzle node with lowest f_score (estimated total cost) from unexplored pq 
        current_node = unexplored.get()[2]
        
		# if current state is the goal state -> returns solution path
        if current_node.is_goal():
            return current_node.get_path()
		
		# else it marks the current node as explored 
        explored.add(current_node)
        
		# moves onto neighboring puzzle nodes (ie. children of current node)
        for neighbor in current_node.get_children():
            
			# need to calculate g_score 
            tentative_g_score = g_score[current_node] + 1
            
			# if neighbor node already explored and g_score is >= previous g_score
            if neighbor in explored and tentative_g_score >= g_score[neighbor]:
                
				# skips neighbor since there is not a better path
                continue

			# else (ie. tentative g_score < previous g_score)
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                
                # this becomes the better path, g_score, f_score updated, added to unexplored pq
                neighbor.parent = current_node
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor)
                
				# increment counter used to break ties when two nodes have the same f_score
                counter += 1 
                unexplored.put((f_score[neighbor], counter, neighbor))
                
	# if loop exits without solution -> returns None since no path to goal node found
    return None