# amazed formula: bset case
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        # nums = sorted(nums, reverse=True)
        dct = {}
        for i, n in enumerate(sorted(nums)):
            if n not in dct:
                dct[n] = i
        return [dct[n] for n in nums]

# #my solution
# class Solution(object):
#     def smallerNumbersThanCurrent(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         answer = list()
#         for x in nums:
#             total = 0
#             for y in nums:
#                 if x > y:
#                     total+=1
#             answer.append(total)
#         return answer

def main():
    print(Solution().smallerNumbersThanCurrent([8,2,1,1]))

if __name__ == "__main__":
    main()
    