class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        for x in set(arr):
            if arr.count(x)>(len(arr)/4):
                return
