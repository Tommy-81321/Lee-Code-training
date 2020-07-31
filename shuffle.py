# fastest one
class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        output = [None] * len(s)
        for char,i in zip(s,indices):
            output[i] = char
        return "".join(output)



# # my solution
# class Solution(object):
#     def restoreString(self, s, indices):
#         """
#         :type s: str
#         :type indices: List[int]
#         :rtype: str
#         """
#         string_to_list = list(s)
#         backup_list = [0 for i in range(len(string_to_list))]
#         for order, index in enumerate(indices):
#             backup_list[index] = string_to_list[order]
#         return "".join(backup_list)