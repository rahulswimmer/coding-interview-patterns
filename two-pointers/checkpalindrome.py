class Solution:
    def solve(self, A):
        p1 = 0
        p2 = len(A)-1

        for idx, x in enumerate(A/2):
            if A[p1] != A[p2]:
                return
            

sol = Solution()
word = "madam"
sol.solve(word)