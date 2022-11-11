

def optimalRoute(downhillScores, start, finish):
    """
    the function will outputs the route  for going from the starting point start to the
   finishing point finish while using only downhill segments and obtaining the maximum score. To achive this, I use
   topo sort and to have the newlist contain all the vertices in the topo order .Traverse through the new list,
   add and record all the largest path from the start's vertex to every vertex that the start's vertex is reachable.
    :Input:
    argv1:a list of tuple where each tuple contain (vertex,adjacent_vertex,weight) represent downhill Score
    argv2:start which is the start location
    argv3:finish which is the end location
    :Output, return or postcondition:he function will outputs the route  for going from the starting point start to the
   finishing point finish while using only downhill segments and obtaining the maximum score if there is one
    :Time complexity: O(D) because the highest complexity of all the function been called i this funciton which is
                    topo_sort_longest_path and it complexity was O(D)
                     where D for the number of edges
    :Aux space complexity:O(D+P) because the size of the adj_lst created by create_graph function
                     where D for the number of edges
                     and P is the number of hills
    """

    lst_size = lst_size_cal(downhillScores)
    adj_list = create_graph(downhillScores,lst_size)
    path = topo_sort_longest_path(start,finish,adj_list,lst_size)
    return path

def create_graph(downhillScores,lst_size):
    """
    create an adjacent list size N where N is the largest vertex in the directed graph, at each list[i]
    add a list of tuple (adjacent_vertex,weight), each tuple will store the vertex that adjacent to list[i] and the
    weight of that edges
    :Input: a list of tuple where each tuple contain (vertex,adjacent_vertex,weight) represent downhill Score
    argv1: list of tuple of downhill score
    argv2: the largest vertex inside the graph
    :Output, return or postcondition:   an adjacent list for directed graph represent the downhill scores
    :Time complexity: append all the tuple present in the origin array into new adj_lst will cost O(D)
                      where D is the number of tuple/segment in the array
    :Aux space complexity: the highest space complexity of the function will be O(D+P)
                            where D is the number of tuple/segment in the array
                            and P is the number of hill in the array
    """
    # create a list of D size where D is the largest vertex
    adjacency_list = [[] for i in range(lst_size)]
    for i in range(len(downhillScores)):
        adjacency_list[downhillScores[i][0]].append([downhillScores[i][1],downhillScores[i][2]])

    return adjacency_list

def lst_size_cal(downhillScores):
    """
    this function will find the largest vertex for the given list
    :Input: a list of tuple where each tuple contain (vertex,adjacent_vertex,weight) represent downhill Score
    argv1:  list of tuple of downhill score
    :Output, return or postcondition: the largest vertex inside the list
    :Time complexity: going through the entire list and append this all the vertex present in the tuple to the new list
                        -> which will cost O(D) where D is number of tuples in the list
    :Aux space complexity: create a list containing all the vertex in each segment -> O(D)
                                Where D is the nummber of segment
    """
    max_lst = []

    # find the largest vertex
    for i in downhillScores:
        max_lst.append(i[0])
        max_lst.append(i[1])
    lst_size = max(max_lst) + 1

    return lst_size

def printPath(path,pre,e):
    """
    The function will print out the path from a given predecessor_list with the start vertex by continuously trace
    the previous vertex until reach a None where a None will indicate the path has already ended
    :Input: a path_list with predecessor_list and the starting vertex, where index(predecessor_list) will be see as
    a vertex and the value store in predecessor_list(index) will be there predecessor.
    argv1: a list to store the path
    argv2: predecessor_list where index(predecessor_list) will be see as a vertex and the value store
    in predecessor_list(index) will be there predecessor.
    argve3: e will be the vertex to start with
    :Output, return or postcondition: return a path of all the predecessor of the given vertex
    :Time complexity: the complexity of the graph is O(P) in the worst case where the path need to find contain all the
    vertex in the graph so you have to trace through the entire list
    ->P is the number of vertex in the graph which predecessor_list belong to
    :Aux space complexity: space complexity for the will be the size of the path_lst, where in the worst case path will
    contain all possible vertex -> O(P) where P is the number of vertex in the graph which predecessor_list belong to
    """
    if pre[e] == None:
        return path
    else:
        path.append(pre[e])
        printPath(path,pre,pre[e])

def dfs(v,visited,stack,adj_lst):
    """
    This function is an application of DFS, we will travel through the graph until reach dead end vertex, then we
    append that vertex into and mark all vertex already travel through as "True" by this we won't travel through that
    trace back the previous vertex, and if that vertex also don't have any other way to go then we append it again to the
    stack and repeat this over again until we find a vertex where the adj_vertex of it didn't travel, then we travel through
    that branch and repeat the cycle until we traverse through the entire graph. After finish traverse we will have
    topological list order of the graph.
    :Input: adj_lst represent of the graph, a stack to store the order, a visited array, and the len of the adj_lst
    argv1: v is the len of the adj_lst
    argv2: visited an array to keep track of what vertex already visit
    argv3: stack, to store the new logical order
    argv4: adj_lst, which is an adjacent list represent the graph.
    :Output, return or postcondition: a list containing the topoligical order of the graph
    :Time complexity: cost of traverse through the list with the help of the adjacent list will bring the cost to
                        O(D+P) where D is number of edges and P is number vertex-> O(P)
    :Aux space complexity: space complexity of this function O(D+P) because of input adj_lst
    """
    visited[v] = True

    for i in adj_lst[v]:
        if (not visited[i[0]]):
            dfs(i[0],visited,stack,adj_lst)

    # Push current vertex to stack which stores topological
    # sort
    stack.append(v)

def topo_sort_longest_path(s,e,adj_lst,lst_size):
    """
    This function is using the application of DFS, and modification to print out all the vertex by the topological order
    which is what the brief ask by saying that the skier can only go down which mean that he are going in 1 direction and
    by assume this we make the list sort by topological order
    Firstly it will take the adj_list and do new modified dfs() for the entire list by calling Function dfs,take the output.
    Then traverse through the new list, add and record all the largest path from the start's vertex to every vertex
    that the start's vertex is reachable.
    During the process of finding the longest path, we use a pred_list to record the path back
    Secondly after we have the list of longest distance from the start's vertex to every reachable vertex, we use the
    print_path() to trace pack the path from start's vertex to end's vertex that we want.
    :Input: a start and end vertex for the path, an adj_list of the graph, and the size of the list.
    argv1:s which is the start location
    argv2:e which is the end location
    argv3: adj_lst which is the adj_lst represent the graph
    argv4: lst_size which is the size of the list
    :Output, return or postcondition:
    :Time complexity:   the time complexity of calling dfs() for the entire graph is O(D+P) and calling print_path()
                        is O(P)
                        which D for the number of edges and P the number of vertex.
                        and base on the brief we can assume that D>P
                        so the overall complexity will be O(D)

    :Aux space complexity: dist,pre,visited,stack,path will all have the space of O(P) where P is the number of vertex
                            But the highest space complexity come from the input which is the adj_lst which have the
                            space complexity of O(P+D)
    """
    path = [e]
    visited = [False for i in range(lst_size)]
    dist = [float('-inf') for i in range(lst_size)]
    pre = [None for i in range(lst_size)]
    stack = []

    for i in range(lst_size):
        if (visited[i] == False):
            dfs(i, visited, stack,adj_lst)


    dist[s] = 0

    while (len(stack) > 0):
        a = stack.pop()
        if (dist[a] != float('-inf')):
            for i in adj_lst[a]:
                if (dist[i[0]] < dist[a] + i[1]):
                    dist[i[0]] = dist[a] + i[1]
                    #updating parent for each vetex that create the largest path.
                    pre[i[0]] = a


    printPath(path, pre, e)
    if len(path) == 1 and e != s:
        path = None
    elif s == e:
        return path
    else:
        path = path[::-1]
    return path


if __name__ == '__main__':
    downhillScores = [(0, 6, -500), (1, 4, 100), (1, 2, 300),
                      (6, 3, -100), (6, 1, 200), (3, 4, 400), (3, 1, 400),
                      (5, 6, 700), (5, 1, 1000), (4, 2, 100)]

    print(optimalRoute(downhillScores, 5, 2))