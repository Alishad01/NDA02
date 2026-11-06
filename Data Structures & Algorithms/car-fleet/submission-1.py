class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []
        for i in range(len(position)):
            ans = ( target - position[i] ) // speed[i]
            if ans not in res:
                res.append(ans)
        return len(res)