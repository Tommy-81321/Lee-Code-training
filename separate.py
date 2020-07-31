# fastest: only use one input
class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        length = len(nums)//2
        total = list()
        list_1 = nums[:length]
        list_2 = nums[length:]
        for index in range(length):
            total.append(list_1[index])
            total.append(list_2[index])
        return total

# # faster
# class Solution(object):
#     def shuffle(self, nums, n):
#         """
#         :type nums: List[int]
#         :type n: int
#         :rtype: List[int]
#         """
#         total = list()
#         list_1 = nums[:n]
#         list_2 = nums[n:]
#         for index in range(n):
#             total.append(list_1[index])
#             total.append(list_2[index])
#         return total

## slower
# class Solution(object):
#     def shuffle(self, nums, n):
#         """
#         :type nums: List[int]
#         :type n: int
#         :rtype: List[int]
#         """
#         total = list()
#         list_1 = nums[:n]
#         list_2 = nums[n:]
#         for index in range(n):
#             total.append(list_1[index])
#             total.append(list_2[index])
#         return total