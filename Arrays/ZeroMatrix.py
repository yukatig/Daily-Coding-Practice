"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
"""


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        """
        result = []
        for row in range(len(matrix)):
            temp = []
            result.append(temp)
            for col in range(len(matrix[0])):
                temp.append(matrix[row][col])
                
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if result[row][col] == 0:
                    for i in range(len(matrix)):
                        matrix[i][col] = 0
                    for j in range(len(matrix[0])):
                        matrix[row][j] = 0
        """
        m = len(matrix)
        n = len(matrix[0])

        firstRowZero = False
        firstColZero = False

        # check if zeroes in first column
        for i in range(m):
            if matrix[i][0] == 0:
                firstColZero = True

        # check if zeroes in first row
        for j in range(n):
            if matrix[0][j] == 0:
                firstRowZero = True

        # look through rest of matrix
        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        for a in range(1, m):
            if matrix[a][0] == 0:
                for b in range(n):
                    matrix[a][b] = 0

        for c in range(1, n):
            if matrix[0][c] == 0:
                for d in range(m):
                    matrix[d][c] = 0

        if firstRowZero:
            for e in range(n):
                matrix[0][e] = 0

        if firstColZero:
            for f in range(m):
                matrix[f][0] = 0
