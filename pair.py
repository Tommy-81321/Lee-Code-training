class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        map_nums = defaultdict(int)
        
        for idx,num in enumerate(nums):
            map_nums[num] = map_nums.get(num,0) +1
            
        print map_nums
         
        all_sum = 0
        for v in map_nums.values():
            all_sum += sum(range(v-1,0,-1))
            
        return all_sum



# 
# class Solution(object):
#     def numIdenticalPairs(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         total = 0
#         count = 0
#         for x in nums:
#             count += 1
#             for y in nums[count:]:
#                 if x == y:
#                     total+=1
#         return total