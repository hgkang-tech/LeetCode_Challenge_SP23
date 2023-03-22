class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        
        left[0] = 1
        right[n - 1] = 1
        answer = []
        for i in range(1, n):
            left[i] = nums[i - 1] * left[i - 1]
 
        for j in range(n-2, -1, -1):
            right[j] = nums[j + 1] * right[j + 1]

        for i in range(n):
            answer.append(left[i] * right[i])
        return answer
        