class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        def helper(parity):
            # Make elements at parity indices smaller than neighbors
            moves = 0
            for i in range(parity, len(nums), 2):
                left = nums[i - 1] if i > 0 else float('inf')
                right = nums[i + 1] if i < len(nums) - 1 else float('inf')
                target = min(left, right) - 1
                if nums[i] > target:
                    moves += nums[i] - target
            return moves
        
        # Either make even indices smaller or odd indices smaller
        return min(helper(0), helper(1))