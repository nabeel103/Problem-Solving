# Number of Sub-arrays With Odd Sum
# Given an array of integers arr, return the number of subarrays with an odd sum.

# Since the answer can be very large, return it modulo 109 + 7.
#Example
# Input: arr = [1,3,5]
# Output: 4
# Explanation: All subarrays are [[1],[1,3],[1,3,5],[3],[3,5],[5]]
# All sub-arrays sum are [1,4,9,3,8,5].
# Odd sums are [1,9,3,5] so the answer is 4.


from ast import List


class Solution:
    def numOfSubarrays(self, arr = []) :
        
        even = 0
        odd = 0
        sum = 0
        ans = 0
        
        for n in arr:
            sum = sum + n
            if sum % 2 == 0:
                ans = ans + odd
                even = even +1
            else :
                ans = ans + 1 + even 
                odd = odd+1

        return (int)(ans % 1000000007)                

s = Solution()
print(s.numOfSubarrays([1,3,5]))

            
            