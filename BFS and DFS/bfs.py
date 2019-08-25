
import collections
def  breadth_first_search(graph, root): 
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue: 
        vertex = queue.popleft()
        for child in graph[vertex]: 
            if child not in visited: 
                visited.add(child) 
                queue.append(child)
        print(visited)
if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1,2]} 
    breadth_first_search(graph, 0)
 
