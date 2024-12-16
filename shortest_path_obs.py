"""
Along with the minimum number of steps, we need to keep track of the number of obstacles as well.
the destination node will be visited multiple times for different values of k.
If a node is visited, then check the value of k as well. If the node can be visited with a higher number of obstacles,
then ignore that path but can be visited with lower value of k.
For example: for (2,1,0) and (2,1,1): 1 node is visited via 1 with 0 obstacles or 1 obstacle. it is possible that
the destination can be reached via (2,1,1) path because in the future there the other path might have higher obstacles.

# errors I made in brute_force:
# I was storing (0,0, k) in hset and checking grid[i][j] is in hset or not
# I udated the k value correctly in if (new_r, new_c, remaining_obs) not in visited and grid[new_r][new_c] == 1 by updating it locally but  if new_r >=0 and new_r < len(grid) and new_c >=0 and new_c < len(grid[0])
# for this case I used global k.
In the brute force approach, I made excessive look up to the hset.
That could be reduced by calculating the remaining_obs using value at grid index
"""
from collections import deque


class Solution_brute_force_TLE:
    def bfs(self, grid, k):
        q = deque()
        visited = set()
        q.append([0, 0, k])
        visited.add((0, 0, k))
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()  # curr[0] is row, curr[1] is col, curr[2] is k

                if curr[0] == len(grid) - 1 and curr[1] == len(grid[0]) - 1:
                    return self.ans

                for d in direction:
                    new_r = d[0] + curr[0]
                    new_c = d[1] + curr[1]
                    remaining_obs = curr[2]
                    if new_r >= 0 and new_r < len(grid) and new_c >= 0 and new_c < len(grid[0]):

                        if (new_r, new_c, remaining_obs) not in visited and grid[new_r][new_c] == 0:
                            if new_r == len(grid) - 1 and new_c == len(grid[0]) - 1:
                                self.ans += 1
                                return self.ans

                            visited.add((new_r, new_c, remaining_obs))
                            q.append([new_r, new_c, remaining_obs])

                        if (new_r, new_c, remaining_obs) not in visited and grid[new_r][new_c] == 1:
                            # can not add
                            if remaining_obs == 0:
                                continue

                            if remaining_obs > 0:
                                remaining_obs -= 1
                                visited.add((new_r, new_c, remaining_obs))
                                q.append([new_r, new_c, remaining_obs])
            self.ans += 1

        self.ans = -1
        return self.ans

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        self.ans = 0
        self.bfs(grid, k)
        return self.ans


class Solution:
    def bfs(self, grid, k):
        q = deque()
        visited = set()
        q.append([0, 0, k])
        visited.add((0, 0, k))
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()  # curr[0] is row, curr[1] is col, curr[2] is k
                # Check if target is reached
                if curr[0] == len(grid) - 1 and curr[1] == len(grid[0]) - 1:
                    return self.ans

                for d in direction:
                    new_r = d[0] + curr[0]
                    new_c = d[1] + curr[1]

                    if new_r >= 0 and new_r < len(grid) and new_c >= 0 and new_c < len(grid[0]):
                        remaining_obs = curr[2] - grid[new_r][new_c]
                        if remaining_obs >= 0 and (new_r, new_c, remaining_obs) not in visited:
                            visited.add((new_r, new_c, remaining_obs))
                            q.append([new_r, new_c, remaining_obs])

            self.ans += 1

        self.ans = -1
        return self.ans

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        self.ans = 0
        self.bfs(grid, k)
        return self.ans


