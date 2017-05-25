
class Graph:
    def __init__(self, v, e):
        self.v = v
        self.e = e
        # Note: The vertices are numbered starting from 1
        self.d = {k: [] for k in range(1, v+1)}

    def add_edge(self, u, v):
        l = self.d.get(u)
        l.append(v)
        self.d[u] = l

    # If there is directed edge from vertex a to vertex b --> a knows b
    def knows(self, a, b):
        l = self.d[a]
        if len(l) > 0 and b in l:
            return True
        return False

    # Find the celebrity from a group of people.
    # A celebrity is a person who everyone knows, but he does not know anyone.
    # From a graph perspective, a celebrity vertex is a vertex with n-1
    # incoming edges and 0 outgoing edges.
    # T(n)- O(n). The other methods include- (i) Traversing the adjacency
    # list/matrix to  check indegree and outdegree values of all vertices
    # (ii) Divide and conquer (iii) Use stack. Refer gfg for these methods
    def celeb(self):
        l = self.d.keys()
        i, j = 0, len(l)-1

        while i < j:
            if self.knows(l[i], l[j]) is True:
                c = l[j]
                i += 1
            else:
                c = l[i]
                j -= 1

        for i in l:
            if i == c:
                continue
            if self.knows(c, i) is False and self.knows(i, c) is True:
                continue
            return -1
        return c

    #
    # Utility function to print all paths from a given source to a destination
    #
    def print_paths_util(self, s, d, path, visited):
        visited[s] = True

        path.append(s)  # Append current node to path
        if s == d:
            print path  # print path when destination node is reached
        else:
            for i in self.d[s]:  # DFS on all adjacent nodes
                if not visited[i]:
                    self.print_paths_util(i, d, path, visited)

        # Remove current element from the path on completion of recursion
        # and reset its visited state
        path.pop()
        visited[s] = False

    #
    # Print all paths from a given source to a destination.
    # Approach: Apply DFS and keep storing path nodes in a list.
    #           Display the list on reaching the destination.
    #
    def print_paths(self, s, d):
        visited = [False]*(self.v+1)
        path = []
        self.print_paths_util(s, d, path, visited)


def main():
    v, e = map(int, raw_input().split())
    g = Graph(v, e)
    for i in range(e):
        a, b = map(int, raw_input().split())
        g.add_edge(a, b)
    s, d = map(int, raw_input().split())
    g.print_paths(s, d)


if __name__ == "__main__":
    main()
