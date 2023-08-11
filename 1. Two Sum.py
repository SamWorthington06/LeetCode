class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for num_one in range(len(nums)):
            for num_two in range(len(nums)):
                if nums[num_one] + nums[num_two] == target and num_one != num_two:
                    return [num_one,num_two]
    
if __name__ == '__main__':
    
    nums = [2,7,11,15]
    target = 9

    solution = Solution()
    print(solution.twoSum(nums, target))