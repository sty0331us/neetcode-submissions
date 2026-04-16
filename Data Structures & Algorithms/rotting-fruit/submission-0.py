class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time = 0
        fresh = 0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])
        
        dir = [[0,-1], [0,1], [-1,0], [1,0]]

        while q and fresh>0:
            for _ in range(len(q)):
                pop = q.popleft()
                r,c = pop[0], pop[1]
                for dr, dc in dir:
                    nr, nc = r+dr, c+dc
                    if nr <0 or nc < 0 or nr == ROWS or nc == COLS or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    q.append([nr,nc])
                    fresh -= 1
            time += 1
            
        return time if fresh == 0 else -1

        