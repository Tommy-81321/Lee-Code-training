# best solution
class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        result_array=[0]*len(nums)
        for i in range(len(nums)):
            if index[i]!=i:
                result_array[index[i]+1:]=result_array[index[i]:-1] #Move one position
            result_array[index[i]]=nums[i] #assign value
        return result_array


# # my solution
# class Solution(object):
#     def createTargetArray(self, nums, index):
#         """
#         :type nums: List[int]
#         :type index: List[int]
#         :rtype: List[int]
#         """
#         answer = list()
#         for value, order in zip(nums, index):
#             answer.insert(order, value)
#         return answer