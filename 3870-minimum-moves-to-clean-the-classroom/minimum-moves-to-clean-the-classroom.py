from collections import deque
class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        max_energy = energy
        litters = [(r,c) for r in range(m) for c in range(n) if classroom[r][c] == 'L']
        l_idx = {pos: i for i, pos in enumerate(litters)}
        target = (1 << len(litters)) - 1
        sr, sc = next((r,c) for r in range(m) for c in range(n) if classroom[r][c] == 'S')
        start_mask = 1 << l_idx[(sr,sc)] if (sr,sc) in l_idx else 0
        q = deque([(sr, sc, energy, start_mask, 0)])
        visited = {(sr, sc, start_mask): energy}
        while q:
            r,c,eng,mask,steps = q.popleft()
            if mask == target: 
                return steps
            if eng == 0 and classroom[r][c] != 'R': 
                continue
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dr, c + dc
                if not(0 <= nr < m and 0 <= nc < n):
                    continue  
                if classroom[nr][nc] == 'X':
                    continue
                
                if classroom[nr][nc] == 'R' :
                    ne = max_energy

                else:
                    ne = eng - 1
                if ne < 0:
                    continue
                nm = mask
                if (nr, nc) in l_idx:
                    nm |= 1 << l_idx[(nr,nc)]
                      
                
                if visited.get((nr, nc, nm), -1) >= ne:
                    continue
                visited[(nr,nc,nm)] = ne
                q.append((nr,nc,ne,nm, steps + 1))
        return -1