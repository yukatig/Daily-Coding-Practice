'''
Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 0
 

Constraints:
0 <= n <= 5 * 106
'''

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = 0
        for i in range(2,n):
            checkPrime = self.isPrime(i)
            if checkPrime: 
                primes += 1
                
        return primes
    
    def isPrime(self, n):
        """
        :type n: int
        :rtype: bool
        """
        multiple = 2
        while (multiple ** 2 <= n):
            if (n % multiple == 0):
                return False
            multiple += 1
            
        return True