# You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

# Return the average salary of employees excluding the minimum and
#  maximum salary. Answers within 10-5 of the actual answer will be accepted.
#Example 1
# Input: salary = [1000,2000,3000]
# Output: 2000.00000
# Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
# Average salary excluding minimum and maximum salary is (2000) / 1 = 2000


# Constraints:

# 3 <= salary.length <= 100
# 1000 <= salary[i] <= 106
# All the integers of salary are unique.

from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        # print(salary)
        sum = 0
        salary = list( dict.fromkeys(salary) )
        if 3<=len(salary) and len(salary)<=100:

            for i in range (1, len(salary)-1):
                if salary[i]>=1000 and salary[i]<= 1000000:

                    sum = sum + salary[i]
                   
        
        return sum/(len(salary)-2)


        

    