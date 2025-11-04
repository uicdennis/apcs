def find_factor(num: int, n: int) -> tuple[str, int]:
    power = 0
    while (num % n) == 0:
        power += 1
        num //= n

    sz = ''
    if power > 0:
        sz = str(n)
        if power > 1:
            sz = sz + '^'
            sz = sz + str(power)
    
    return sz, num

if __name__ == "__main__":
    num = int(input())
    ans = []
    max_check_factor = int(num ** 0.5) + 1

    # 先計算2的因數以加速效率
    sz, num = find_factor(num, 2)

    if sz:
        ans.append(sz)

    # 從3開始檢查質因數
    for n in range(3, max_check_factor, 2):
        sz = ''
        sz, num = find_factor(num, n)
        if sz:
            ans.append(sz)

    # num不被除盡，表示有更大的質因數
    if num != 1:
        ans.append(str(num))

    if len(ans) > 1:
        print(' * '.join(ans))
    else:
        print(ans[0])