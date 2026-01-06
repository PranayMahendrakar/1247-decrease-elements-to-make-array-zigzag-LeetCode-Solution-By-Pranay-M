class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Case 1: Even indices are peaks (A[0] > A[1] < A[2] > A[3] ...)
        # Decrease odd-indexed elements
        moves1 = 0
        for i in range(1, n, 2):
            left = nums[i - 1] if i > 0 else float('inf')
            right = nums[i + 1] if i < n - 1 else float('inf')
            target = min(left, right) - 1
            if nums[i] >= target + 1:
                moves1 += nums[i] - target
        
        # Case 2: Odd indices are peaks (A[0] < A[1] > A[2] < A[3] ...)
        # Decrease even-indexed elements
        moves2 = 0
        for i in range(0, n, 2):
            left = nums[i - 1] if i > 0 else float('inf')
            right = nums[i + 1] if i < n - 1 else float('inf')
            target = min(left, right) - 1
            if nums[i] >= target + 1:
                moves2 += nums[i] - target
        
        return min(moves1, moves2)