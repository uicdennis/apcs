# Input                   Output
# 2 + 3 * 4               14
# 2 * ( 3 + 4 ) * 5       70
# 去括號，前序，中序，後序問題
# 中序式(Infix)、前序式(Prefix)、後序式(Postfix)

# 3. 加入優先權
# 3.1 設定優先權table
# 3.2 運算員直接輸出
# 3.3 遇到堆疊裡的運算子優先權若較低，則將堆疊裡所有運算子輸出??
# 3.4 若字串已無需要處理，則輸出所有堆疊裡的東西
# 3.5 若考慮括號，則左括號進堆疊，右括號則pop堆疊至左括號，括號不輸出。

    
prioity = {'+':1, 
      '-':1,
      '*':2,
      '/':2,
      '%':2,
      '(':3,
      ')':3}

sz = '24*(31+49)*15'
sz1 = '2+3*4'               # [3, '*', 4, '+', 2] <= [3, 4, 2], ['*', '+']
sz2 = '2*(3+4)*5'           # ['(', 3, '+', 4, ')', '*', 2, '*', 5]
sz3 = '(6/2)+(8%5)-2*1'
sz4 = '((4+(5*(8+9)))+(6/3))'   # ['8+9', ]
sz5 = '2*3+4'
sz6 = '4+3-2'

# 假如運算式沒有空格分開，那就需此函式進行分離
def to_infix(formula: str, infix: list) -> int:
    idx = 0
    idx1 = 0
    # count = 0
    total = len(formula)
    while idx < total:
        ch = formula[idx]
        if ch == '+' or ch == '-' \
           or ch == '*' or ch == '/':
            infix.append(formula[idx1:idx])
            infix.append(ch)
            idx1 = idx + 1
        elif ch == '(':
            idx += 1
            infix.append(ch)
            idx += to_infix(formula[idx:], infix)
            # idx += count
            idx1 = idx
        elif ch == ')':
            infix.append(formula[idx1:idx])
            return idx

        idx +=1

    infix.append(formula[idx1:])

# 中序運算式不適合程式運算，需要改成後序或前序
def in_to_post(formula: list[str]) -> list:
    stackOP = []
    postfix = []

    for op in formula:
        if op.isnumeric():
            postfix.append(op)
        elif op == '(':
            stackOP.append(op)
        elif op == ')':
            # 在stackOP裡，成對括號中間，必定有運算子，必須將他們加入postfix裡
            while stackOP and stackOP[-1] != '(':
                postfix.append(stackOP.pop())
            stackOP.pop()   # 移除 '('
            print(stackOP)
            pass
        else:   # 運算子
            # 目前的運算子必須跟stackOP裡的運算子比較priority
            # 若priority較高才直接輸出，否則存入stack，等候op2
            while stackOP and prioity[stackOP[-1]] > prioity[op]:
                postfix.append(stackOP.pop())
            stackOP.append(op)

    while stackOP:
        postfix.append(stackOP.pop())

    print(postfix)
    return postfix

def calc_postfix(formula: list[str]) -> int:
    ans = []

    for op in formula:
        if op.isnumeric():
            ans.append(op)
        else:
            b = int(ans.pop())
            a = int(ans.pop())
            if op == '+':
                ans.append(a + b)
            elif op == '-':
                ans.append(a - b)
            elif op == '*':
                ans.append(a * b)
            elif op == '/':
                ans.append(a // b)
            elif op == '%':
                ans.append(a % b)
    
    print(ans)
    return int(ans[0])

# 利用eval()
# 可比較exec()
def quick_solution(formula: str):
    print(eval(formula.replace('/', '//')))

if __name__ == "__main__":
    infix = []
    quick_solution(sz2)
    to_infix(sz1, infix)
    print(infix)
    if ''.join(infix) == sz1:
        print('True')
        postfix = in_to_post(infix)
        calc_postfix(postfix)

    infix = []
    to_infix(sz5, infix)
    # print(infix)
    if ''.join(infix) == sz5:
        # print('True')
        postfix = in_to_post(infix)
        calc_postfix(postfix)

    infix = []
    to_infix(sz6, infix)
    # print(infix)
    if ''.join(infix) == sz6:
        # print('True')
        postfix = in_to_post(infix)
        calc_postfix(postfix)

    infix = []
    to_infix(sz4, infix)
    print(infix)
    if ''.join(infix) == sz4:
        print('True')
