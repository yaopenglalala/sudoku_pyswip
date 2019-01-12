import random
from pyswip import Prolog

AVAILABLE_SIZE = (4, 9)

class Sudoku(object):
    def __init__(self, size = 9, hole_rate = 0.5):
        # 确定数独大小 ：4或9
        self.size = size
        # 确定空洞率
        self.hole_rate = hole_rate
        # 行剩余可选数字
        self.rows_available = [[i for i in range(self.size)] for j in range(self.size)]
        # 列剩余可选数字
        self.columns_available = [[i for i in range(self.size)] for j in range(self.size)]
        # 每个小九宫格剩余可选数字
        self.blocks_available =  [[i for i in range(self.size)] for j in range(self.size)]
        # 每个数字的可能选集（用于下一个位置可用为空时的回退）
        self.cells_avaiable = [[i for i in range(self.size)] for j in range(self.size * self.size)]

        # print(rows_available)
        self.block_size = int(self.size ** 0.5)
        self.sudoku = [[] for i in range(self.size)]
        self.fill_next(0, 0)
        self.standard_answer = self.remain_answer()
        # self.sudoku_print()
        self.hole_create()
        # self.sudoku_print()

    def fill_next(self, row, column):
        # sudoku_print(sudoku)
        block_row = row // self.block_size
        block_column = column // self.block_size
        block_area = block_row * self.block_size + block_column

        available_row = self.rows_available[row]
        available_column = self.columns_available[column]
        available_block = self.blocks_available[block_area]
        available_cell = self.cells_avaiable[row * self.size + column]

        while len(available_cell) != 0 :
            available_value = get_available_value(available_row, available_column, available_block, available_cell)
            # 无可选值，说明上一个方格填法不可满足
            if available_value == -1:
                return -1

            # 填入
            self.sudoku[row].append(available_value)

            # 把这种填法所用值从行、列、小数独块可用值中移除
            remove_filled(available_row, available_column, available_block, available_value)

            # 填下一个
            if (row + 1) == self.size and (column + 1) == self.size:
                return 1
            else :
                # 判断下一个是不是新的一行
                next_column = column + 1
                next_row = row + (next_column // self.size)
                next_column = next_column % self.size

                res = self.fill_next(next_row, next_column)
                
                if res == 1: # 成功填入
                    return 1
                elif res == -1: # 后一个方格无法继续填，移除该方案
                    self.sudoku[row].pop()
                    available_cell.remove(available_value)
                    reset(available_row, available_column, available_block, available_value)
                    self.cells_avaiable[next_row * self.size + next_column] = [i for i in range(self.size)]
        
        # 试过所有可行解，都不能填充，说明上一个位置填充有误
        return -1

    # 将数独的标准答案保留
    def remain_answer(self) :
        answer = [[] for i in range(self.size)]
        for row in range(self.size) :
            for column in range(self.size) :
                answer[row].append(self.sudoku[row][column])
        return answer

    # 在数独中制造孔洞
    def hole_create(self) :
        for row in range(self.size) :
            for column in range(self.size) :
                random_float = random.random()
                if random_float < self.hole_rate :
                    self.sudoku[row][column] = -1

    def sudoku_print(self) :
        _print_like_sudoku(self.sudoku, self.size)

    def show_answer(self) :
        _print_like_sudoku(self.standard_answer, self.size)

    def list_return(self) :
        result = []
        for row in self.sudoku :
            for number in row :
                result.append(number)
        return result

# 将行可行解、列可行解、区块可行解与自身可行解取交集，随机返回一个
def get_available_value(available_row, available_column, available_little, cell_avaiable):
        # print(available_row)
        # print(available_column)
        # print(available_little)
        available_set = list(set(available_row).intersection(set(available_column)))
        available_set = list(set(available_set).intersection(set(available_little)))
        available_set = list(set(available_set).intersection(set(cell_avaiable)))

        ava_set_len = len(available_set)
        
        if ava_set_len == 0 :
            return -1

        loc = random.randint(0, ava_set_len - 1)
        res = available_set[loc]
        # print(res)
        return res

# 将该方格已填过的内容从各个可行解中移除
def remove_filled(available_row, available_column, available_little, filled):
        available_row.remove(filled)
        available_column.remove(filled)
        available_little.remove(filled)

# 证明该方格该填法不可满足后，将之填过的放回可行解集合中
def reset(available_row, available_column, available_little, not_suit):
        available_row.append(not_suit)
        available_column.append(not_suit)
        available_little.append(not_suit)

def list_print_like_sudoku(list, size):
    block_size = int (size ** 0.5)
    for row in range(size) :
        line = "["
        for column in range(size) :
            line += str(list[row * size + column]) + ", "
            if column % block_size == block_size - 1 :
                line = line.rstrip(' ')
                line = line.rstrip(',')
                line += "|"
        line = line.rstrip('|')
        print(line + "]")
        if row % block_size == block_size - 1 :
            if (size == 9) :
                print("-------------------------")
            elif (size == 4) :
                print("-----------")

def _print_like_sudoku(rows, size) :
    block_size = int (size ** 0.5)
    for row in range(size) :
        line = "["
        for column in range(size) :
            if rows[row][column] == -1 :
                line += "_, "
            else :
                line += str(rows[row][column] + 1) + ", "
            if column % block_size == (block_size - 1) :
                line = line.rstrip(' ')
                line = line.rstrip(',')
                line += "|"
        line = line.rstrip('|')
        print(line + "]")
        if row % block_size == (block_size - 1):
            if (size == 9) :
                print("-------------------------")
            elif (size == 4) :
                print("-----------")


                
                    