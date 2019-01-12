# sudoku_pyswip
使用pyswip与SWI-Prolog解数独

## 使用环境
> python 3.7.0   
> SWI-Prolog 7.6.4  
> pyswip 0.2.2

## 使用方法
### 运行sudoku_solutiont.py  

1. 控制台显示
    ```
    Solve a sudoku (i) or auto create sudoku? (a)
    ```
    i与a分别表示手动从控制台输入数独进行求解或者自动生成数独。

2. 键入i（或a）之后，控制台显示：
    ```
    Choose sudoku size : 4 or 9?
    ```
    选择数独的大小规模。
3. (1) 若之前选择i
    ```
    You should use _ to present a blank.
    ```
    将数独组织为```,```分隔的，以```_```表示空格的一维数组，在控制台输入  
    (2) 若之前选择a
    ```
    input the hole rate : (0, 1).
    ``` 
    选择孔洞概率
4. 打印数独的解