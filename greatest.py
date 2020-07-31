# fastest
class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        maximun = max(candies)
        for index in candies:
            result.append((index+extraCandies)>=maximun)
        return result
        
# # 
# class Solution(object):
#     def kidsWithCandies(self, candies, extraCandies):
#         """
#         :type candies: List[int]
#         :type extraCandies: int
#         :rtype: List[bool]
#         """
#         result = []
#         maximun = max(candies)
#         for index in candies:
#             if (index + extraCandies) >= maximun:
#                 result.append(True)
#             else:
#                 result.append(False)
#         return result