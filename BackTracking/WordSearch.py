"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for row in range(len(board)):
            for col in range(len(board[0])):
                check = self.backtrack(board, word, row, col, 1)
                if check == True:
                    return True
                    
        return False
        
    def backtrack(self, board, word, i, j, nums):
        
        if nums == len(word):
            return True 
                
        if i < 0 or i >= len(board):
            return False
        
        if j < 0 or j >= len(board[0]):
            return False
        
        if board[i][j] != word[nums]:
            return False
        
        if nums == len(word):
            return True 
        
        tmp = word[nums]
        board[i][j] = "#"
        
        case1 = self.backtrack(board, word, i - 1, j, nums + 1)
        
        case2 = self.backtrack(board, word, i, j + 1, nums + 1)
        
        case3 = self.backtrack(board, word, i + 1, j, nums + 1)
        
        case4 = self.backtrack(board, word, i, j - 1, nums + 1)
        
        board[i][j] = tmp

        return (case1 or case2 or case3 or case4)


        """
        for rowAdd in range(-1, 2):
            for colAdd in range(-1, 2):
                if (rowAdd + colAdd) % 2 == 0:
                    continue
                row = i + rowAdd
                if row < 0 or row >= len(board):
                    continue 
                col = j + colAdd
                if col < 0 or col >= len(board[0]):
                    continue
                if board[row][col] == word[nums]:
                    print("hello " + board[row][col] + str(row) + str(col))
                    self.backtrack(board, word, row, col, nums + 1)
                    
        """
        
        