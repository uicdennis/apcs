# 我們都知道電腦擅長於各種數字的計算，可是，
# 我們又知道各種程式語言的變數又都有上限，比如
# 整數只有232 或 264 個。如果要計算更大的數字時
# 又該如何計算呢? 就交給聰明的您來解決囉。
#
# 以 + 代表加法
# 以 - 代表減法
# 以 * 代表乘法
# 以 / 代表除法 (取商數)

# carry, borrow

# Python 支援大數運算，可於互動環境輸入範例試試。
# 2222222222222222222222222 + 1111111111111111111111111 = 3333333333333333333333333
# 2222222222222222222222222 - 1111111111111111111111111 = 1111111111111111111111111
# 2222222222222222222222222 * 1111111111111111111111111 = 2469135802469135802469135308641975308641975308642
# 2222222222222222222222222 / 1111111111111111111111111 = 2

def quick_solution(formula: str) -> str:
    sz = formula.replace('/', '//')
    return eval(sz)

# 只考慮整數
# 直覺需要比大小
class BigInt():
    def __init__(self, num: str):
        self._num = num
        self._digits = len(num)

    def __str__(self):
        return self._num
    
    def __gt__(self, other):
        if self._digits > other._digits:
            return True
        elif self._digits < other._digits:
            return False
        else:
            # 比較數值大小
            for i in range(self._digits):
                if int(self._num[i]) > int(other._num[i]):
                    return True
                elif int(self._num[i]) < int(other._num[i]):
                    return False
            
            return False
    
    def __lt__(self, other):
        return other > self

    def __eq__(self, other):
        if self._digits != other._digits:
            return False
        for i in range(self._digits):
            if self._num[i] != other._num[i]:
                return False
        
        return True

    def bigAddSmall(self, big: str, small: str):
        bg = list(big)
        sm = list(small)
        ans = []
        carry = 0
        for i, ch in enumerate(bg):
            if i < len(sm):
                temp = int(ch) + int(sm[i]) + carry
            else:
                temp = int(ch) + carry
            carry = temp // 10
            ans.append(str(temp%10))

        if carry > 0:
            ans.append('1')
        
        return BigInt(''.join(ans[::-1]))

    # + (addition): __add__(self, other)
    # - (subtraction): __sub__(self, other)
    # * (multiplication): __mul__(self, other)
    # / (true division): __truediv__(self, other)
    # ** (power): __pow__(self, other)
    def __add__(self, other):
        if self._digits > other._digits:
            big = self
            small = other
        elif self._digits < other._digits:
            big = other
            small = self
        return self.bigAddSmall(big._num[::-1], small._num[::-1])

class TestCompare():
    def test_different_digits(self):
        a = BigInt('333')
        b = BigInt('111111')
        assert b > a
    def test_big_number(self):
        a = BigInt('2222222222222222222222222')
        b = BigInt('3333333333333333333333333')
        assert b > a
    def test_equal_digits_1(self):
        a = BigInt('1234')
        b = BigInt('4321')
        assert b > a
    def test_equal_digits_2(self):
        a = BigInt('1234')
        b = BigInt('1432')
        assert b > a
    def test_equal_digits_3(self):
        a = BigInt('1234')
        b = BigInt('1243')
        assert b > a
    def test_equal_digits_4(self):
        a = BigInt('1234')
        b = BigInt('1235')
        assert b > a
    def test_equal_digits_5(self):
        a = BigInt('1234')
        b = BigInt('1234')
        assert not b > a

    def test_equal_num_1(self):
        a = BigInt('1234')
        b = BigInt('1234')
        assert b == a
    def test_equal_num_2(self):
        a = BigInt('0')
        b = BigInt('0')
        assert b == a
    def test_equal_num_3(self):
        a = BigInt('12345678987654321')
        b = BigInt('12345678987654321')
        assert b == a

    def test_add_1(self):
        a = BigInt('12')
        b = BigInt('9')
        assert (a+b) == BigInt('21')
    def test_add_2(self):
        a = BigInt('1234')
        b = BigInt('66')
        assert (a+b) == BigInt('1300')
    def test_add_3(self):
        a = BigInt('66')
        b = BigInt('234')
        assert (a+b) == BigInt('300')
    def test_add_4(self):
        a = BigInt('99876')
        b = BigInt('321')
        assert (a+b) == BigInt('100197')

def test_big():
    a = BigInt('2222222222222222222222222')
    b = BigInt('1111111111111111111111111')

    print('a > b => ', a>b)

if __name__ == "__main__":
    # eq1 = '2222222222222222222222222 + 1111111111111111111111111'
    # eq2 = '2222222222222222222222222 - 1111111111111111111111111'
    # eq3 = '2222222222222222222222222 * 1111111111111111111111111'
    # eq4 = '2222222222222222222222222 / 1111111111111111111111111'
    # eq5 = '1111111111111111111111111 - 2222222222222222222222222'
    # eqs = [eq1, eq2, eq3, eq4]
    # for eq in eqs:
    #     print(quick_solution(eq))

    # test_big()

    a = BigInt('99876')
    b = BigInt('321')
    c = a + b
    print(c)