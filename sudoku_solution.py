import sudoku
from pyswip import Prolog

if __name__ == "__main__":
    test_way = input("Solve a sudoku (i) or auto create sudoku? (a) \n")

    if (test_way == "i") :
        sudoku_size = int(input("Choose sudoku size : 4 or 9? \n"))
        prolog_question = input("You should use _ to present a blank. \n")
    elif (test_way == "a") :
        sudoku_size = int(input("Choose sudoku size : 4 or 9? \n"))

        while(sudoku_size not in sudoku.AVAILABLE_SIZE) :
            sudoku_size = int (input("Unavailable size, you should input 4 or 9. \n"))

        hole_rate = float(input("input the hole rate : (0, 1). \n"))
        while(hole_rate < 0 or hole_rate > 1) :
            hole_rate = float(input("Unavailable hole rate. \n"))

        # 生成数独并打印
        question = sudoku.Sudoku(sudoku_size, hole_rate)
        print("Question : ")
        question.sudoku_print()
        print("Standard answer : ")
        question.show_answer()

        list_question = question.list_return()

        # 转换成prolog语言可处理的输入
        prolog_question = ""
        for item in list_question :
            if item == -1 :
                prolog_question += "_"
            else :
                prolog_question += str(item + 1)
            prolog_question += ","
        prolog_question = prolog_question.rstrip(",")

    # 运行pl文件，求出结果
    # print(prolog_question)
    solution_pl = Prolog()
    solution_pl.consult("sudoku_solution.pl")
    # print(prolog_question)
    result = solution_pl.query("sudoku([" + prolog_question + "], X, " + str(sudoku_size) + ").")
    # result = solution_pl.query("findall(Solution, sudoku([" + prolog_question + "],Solution), X).")
    # result = solution_pl.query("problem(1, Rows), sudoku(Rows), maplist(portray_clause, Rows).")
    
    # 打印结果
    count = 1
    for res in result :
        print("Possible answer " + str(count) + " :")
        # print(res)
        solution = res["X"]
        if len(solution) != 0 :
            sudoku.list_print_like_sudoku(solution, sudoku_size)
            count += 1
        else :
            print("no")
    if (count == 1) :
        print("This sudoku has no solution!")