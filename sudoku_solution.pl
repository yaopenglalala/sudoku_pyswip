:- use_module(library(clpfd)).

sudoku(Question, Solution, 4) :-
    Question = [R1C1,R1C2,R1C3,R1C4,
            R2C1,R2C2,R2C3,R2C4,
            R3C1,R3C2,R3C3,R3C4,
            R4C1,R4C2,R4C3,R4C4],
    Solution = Question,

    Solution ins 1..4,
    
    Row1 = [R1C1,R1C2,R1C3,R1C4],
    Row2 = [R2C1,R2C2,R2C3,R2C4],
    Row3 = [R3C1,R3C2,R3C3,R3C4],
    Row4 = [R4C1,R4C2,R4C3,R4C4],

    Col1 = [R1C1,R2C1,R3C1,R4C1],
    Col2 = [R1C2,R2C2,R3C2,R4C2],
    Col3 = [R1C3,R2C3,R3C3,R4C3],
    Col4 = [R1C4,R2C4,R3C4,R4C4],

    Block1 = [R1C1,R1C2,R2C1,R2C2],
    Block2 = [R1C3,R1C4,R2C3,R2C4],
    Block3 = [R3C1,R3C2,R4C1,R4C2],
    Block4 = [R3C3,R3C4,R4C3,R4C4],

    all_distinct(Row1), all_distinct(Row2), all_distinct(Row3), all_distinct(Row4),
    all_distinct(Col1), all_distinct(Col2), all_distinct(Col3), all_distinct(Col4),
    all_distinct(Block1), all_distinct(Block2), all_distinct(Block3), all_distinct(Block4),

    label(Solution).


sudoku(Question,Solution, 9) :-
    Question = [R1C1,R1C2,R1C3,R1C4,R1C5,R1C6,R1C7,R1C8,R1C9,
            R2C1,R2C2,R2C3,R2C4,R2C5,R2C6,R2C7,R2C8,R2C9,
            R3C1,R3C2,R3C3,R3C4,R3C5,R3C6,R3C7,R3C8,R3C9,
            R4C1,R4C2,R4C3,R4C4,R4C5,R4C6,R4C7,R4C8,R4C9,
            R5C1,R5C2,R5C3,R5C4,R5C5,R5C6,R5C7,R5C8,R5C9,
            R6C1,R6C2,R6C3,R6C4,R6C5,R6C6,R6C7,R6C8,R6C9,
            R7C1,R7C2,R7C3,R7C4,R7C5,R7C6,R7C7,R7C8,R7C9,
            R8C1,R8C2,R8C3,R8C4,R8C5,R8C6,R8C7,R8C8,R8C9,
            R9C1,R9C2,R9C3,R9C4,R9C5,R9C6,R9C7,R9C8,R9C9],
    Solution = Question,

    Solution ins 1..9,

    Row1 = [R1C1,R1C2,R1C3,R1C4,R1C5,R1C6,R1C7,R1C8,R1C9],
    Row2 = [R2C1,R2C2,R2C3,R2C4,R2C5,R2C6,R2C7,R2C8,R2C9],
    Row3 = [R3C1,R3C2,R3C3,R3C4,R3C5,R3C6,R3C7,R3C8,R3C9],
    Row4 = [R4C1,R4C2,R4C3,R4C4,R4C5,R4C6,R4C7,R4C8,R4C9],
    Row5 = [R5C1,R5C2,R5C3,R5C4,R5C5,R5C6,R5C7,R5C8,R5C9],
    Row6 = [R6C1,R6C2,R6C3,R6C4,R6C5,R6C6,R6C7,R6C8,R6C9],
    Row7 = [R7C1,R7C2,R7C3,R7C4,R7C5,R7C6,R7C7,R7C8,R7C9],
    Row8 = [R8C1,R8C2,R8C3,R8C4,R8C5,R8C6,R8C7,R8C8,R8C9],
    Row9 = [R9C1,R9C2,R9C3,R9C4,R9C5,R9C6,R9C7,R9C8,R9C9],
    
    Col1 = [R1C1,R2C1,R3C1,R4C1,R5C1,R6C1,R7C1,R8C1,R9C1],
    Col2 = [R1C2,R2C2,R3C2,R4C2,R5C2,R6C2,R7C2,R8C2,R9C2],
    Col3 = [R1C3,R2C3,R3C3,R4C3,R5C3,R6C3,R7C3,R8C3,R9C3],
    Col4 = [R1C4,R2C4,R3C4,R4C4,R5C4,R6C4,R7C4,R8C4,R9C4],
    Col5 = [R1C5,R2C5,R3C5,R4C5,R5C5,R6C5,R7C5,R8C5,R9C5],
    Col6 = [R1C6,R2C6,R3C6,R4C6,R5C6,R6C6,R7C6,R8C6,R9C6],
    Col7 = [R1C7,R2C7,R3C7,R4C7,R5C7,R6C7,R7C7,R8C7,R9C7],
    Col8 = [R1C8,R2C8,R3C8,R4C8,R5C8,R6C8,R7C8,R8C8,R9C8],
    Col9 = [R1C9,R2C9,R3C9,R4C9,R5C9,R6C9,R7C9,R8C9,R9C9],
    
    Block1 = [R1C1,R1C2,R1C3,R2C1,R2C2,R2C3,R3C1,R3C2,R3C3],
    Block2 = [R1C4,R1C5,R1C6,R2C4,R2C5,R2C6,R3C4,R3C5,R3C6],
    Block3 = [R1C7,R1C8,R1C9,R2C7,R2C8,R2C9,R3C7,R3C8,R3C9],
    Block4 = [R4C1,R4C2,R4C3,R5C1,R5C2,R5C3,R6C1,R6C2,R6C3],
    Block5 = [R4C4,R4C5,R4C6,R5C4,R5C5,R5C6,R6C4,R6C5,R6C6],
    Block6 = [R4C7,R4C8,R4C9,R5C7,R5C8,R5C9,R6C7,R6C8,R6C9],
    Block7 = [R7C1,R7C2,R7C3,R8C1,R8C2,R8C3,R9C1,R9C2,R9C3],
    Block8 = [R7C4,R7C5,R7C6,R8C4,R8C5,R8C6,R9C4,R9C5,R9C6],
    Block9 = [R7C7,R7C8,R7C9,R8C7,R8C8,R8C9,R9C7,R9C8,R9C9],

    all_distinct(Row1), all_distinct(Row2),  all_distinct(Row3), 
    all_distinct(Row4), all_distinct(Row5),  all_distinct(Row6), 
    all_distinct(Row7), all_distinct(Row8),  all_distinct(Row9), 

    all_distinct(Col1), all_distinct(Col2),  all_distinct(Col3), 
    all_distinct(Col4), all_distinct(Col5),  all_distinct(Col6), 
    all_distinct(Col7), all_distinct(Col8),  all_distinct(Col9), 

    all_distinct(Block1), all_distinct(Block2),  all_distinct(Block3), 
    all_distinct(Block4), all_distinct(Block5),  all_distinct(Block6), 
    all_distinct(Block7), all_distinct(Block8),  all_distinct(Block9),

    label(Solution). %保证返回确定的值而不返回variable(x)
    %Solution = []. %可能无解



