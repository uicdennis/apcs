rome_map = {
    'I': 1, 
    'V': 5, 
    'X': 10, 
    'L': 50, 
    'C': 100, 
    'D': 500, 
    'M': 1000 }
''' 輸入說明:
每個輸入檔中會有一個或以上的測試資料。
每一行由兩個數字組成一筆測試資料，且所有數字將會小於4,000。
檔案最後會以符號 # 表示結束。
輸出說明:
每筆測試資料的答案必須輸出到檔案中，並且換行。如果答案為零，則須輸出字串 ZERO。
'''
# 直接使用table對照
units = {1:'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', \
         6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
tens = {1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', \
         6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
hundreds = {1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', \
         6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}
thousands = {1: 'M', 2: 'MM', 3: 'MMM'}

# 數值轉換羅馬數字
def num_2_rome(num: int) -> str:
    if num == 0:
        return 'ZERO'
    if num > 4000:
        return ''
    
    ans = ''
    if num > 1000:
        ans += thousands[num // 1000]
        num %= 1000
    if num > 100:
        ans += hundreds[num // 100]
        num %= 100
    if num > 10:
        ans += tens[num // 10]
        num %= 10
    if num > 0:
        ans += units[num]
    
    return ans

def rome_2_num(rome: str) -> int:
    if rome == 'ZERO':
        return 0

    # 需要比較與前一個羅馬數字的大小
    total = 0
    prev = 10000    # 預設為最大，第一次不用比較prev與curr
    # 順向檢查所有羅馬數字
    for ch in rome:
        curr = rome_map[ch]
        total += curr
        if prev < curr:
            # 順向已將羅馬數字加總
            # 發現前一字較小，需要倒扣，因此要扣兩倍
            total -= (prev * 2)
        prev = curr
        
    return total

def rome_2_num_2(rome: str) -> int:
    if rome == 'ZERO':
        return 0

    # 需要比較與前一個羅馬數字的大小
    total = 0
    prev = 0
    # 逆向檢查所有羅馬數字
    for ch in reversed(rome):
        curr = rome_map[ch]
        if curr < prev:
            total -= curr   # 發現前一字較大，需要倒扣
        else:
            total += curr   # 前一字沒有較大，直接加總
        prev = curr

    return total

def unit_test():
    # III, XXIV, DLXVII, MMXLVIII, ZERO, ''
    tests = [3, 24, 567, 2048, 0, 94, 444, 5432]

    for n in tests:
        print(num_2_rome(n))
    
    romes = ['III', 'XXIV', 'DLXVII', 'MMXLVIII', 'ZERO', 'XCIV', 'CDXLIV']
    for sz in romes:
        print(rome_2_num(sz), rome_2_num_2(sz))

if __name__ == "__main__":
    # unit_test()
    # sz = input()

    filename = input()
    fd = open(filename, 'rt', encoding="utf-8")
    romes = fd.readlines()
    for sz in romes:
        if sz == '#':
            break
        a, b = sz.split()
        result = rome_2_num(a) - rome_2_num(b)
        if result < 0:
            result *= -1
        print(num_2_rome(result))
