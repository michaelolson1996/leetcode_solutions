class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        columns = {}
        for i in range(len(board)):
            new_row = {}
            if i % 3 == 0:
                new_box = {
                    1: {},
                    2: {},
                    3: {},
                }
            for j, col in enumerate(board[i]):
                if col != ".":
                    col = int(col)
                    if j not in columns:
                        columns[j] = {}

                    if col in columns[j]:
                        return False
                    else:
                        columns[j][col] = True

                    if col in new_row:
                        return False
                    else:
                        new_row[col] = True

                    if j < 3:
                        if col in new_box[1]:
                            return False
                        new_box[1][col] = True
                    elif j < 6:
                        if col in new_box[2]:
                            return False
                        new_box[2][col] = True
                    else:
                        if col in new_box[3]:
                            return False
                        new_box[3][col] = True
        return True
