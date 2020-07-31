# fastest
class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        total = []
        # or total = list()
        sum_total = 0
        for index in range(length):
            sum_total += nums[index]
            total.append(sum_total)
        return total



# # faster
# class Solution(object):
#     def runningSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         total = []
#         sum_total = 0
#         for index in range(len(nums)):
#             sum_total += nums[index]
#             total.append(sum_total)
#         return total

# # lower
# class Solution(object):
#     def runningSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         total = []
#         for index in range(len(nums)):
#             total.append(sum(nums[:index+1]))
#         return total