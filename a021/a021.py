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
    return str(eval(sz))

# 只考慮整數
# 直覺需要比大小
# 追加考慮正負數
class BigInt():
    def __init__(self, num: str):
        if num[0] == '-':
            self._positive = False
            num = num[1:]
        else:
            self._positive = True
        self._num = num
        self._digits = len(num)

    @property
    def sign(self):
        return self._positive

    @sign.setter
    def sign(self, isPlus):
        self._positive = isPlus

    @property
    def value(self) -> str:
        if self._positive:
            return self._num
        else:
            return '-' + self._num

    def __str__(self):
        if self._positive:
            return self._num
        else:
            return '-' + self._num

    def __gt__(self, other):
        # 比較正負號
        if self._positive and not other._positive:
            return True
        elif not self._positive and other._positive:
            return False

        # 正負相同，先比較位數
        if self._digits > other._digits:
            return self._positive
        elif self._digits < other._digits:
            return not self._positive
        else:
            # 比較數值大小
            for i in range(self._digits):
                if int(self._num[i]) > int(other._num[i]):
                    return self._positive
                elif int(self._num[i]) < int(other._num[i]):
                    return not self._positive

            # 數值相等
            return False

    def __lt__(self, other):
        return other > self

    def __eq__(self, other):
        # 比較正負號
        if self._positive != other._positive:
            return False

        if self._digits != other._digits:
            return False
        for i in range(self._digits):
            if self._num[i] != other._num[i]:
                return False

        return True

    def __ge__(self, other):
        return self > other or self == other

    def __le__(self, other):
        return other > self or other == self

    # 只考慮兩正數相加
    def bigAddSmall(self, big: str, small: str):
        bg = list(big[::-1])
        sm = list(small[::-1])
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

    # 只考慮兩正數相減
    def bigMinusSmall(self, big: str, small: str):
        bg = list(big[::-1])
        sm = list(small[::-1])
        ans = []
        borrow = 0
        for i, ch in enumerate(bg):
            if i < len(sm):
                temp = int(ch) - int(sm[i]) - borrow
                if temp < 0:
                    borrow = 1
                    temp += 10
                else:
                    borrow = 0
            else:
                temp = int(ch) - borrow
                borrow = 0

            # 最高為相減為0不紀錄
            # 相等位數相減會有問題
            # if i != len(bg) - 1 or temp != 0:
            #     ans.append(str(temp%10))
            # 無條件紀錄結果
            ans.append(str(temp%10))

        # 移除個位數以外帶頭為0的部分
        result = ''.join(ans).rstrip('0')
        if result == '':
            result = '0'

        return BigInt(result[::-1])

    # + (addition): __add__(self, other)
    # - (subtraction): __sub__(self, other)
    # * (multiplication): __mul__(self, other)
    # / (true division): __truediv__(self, other)
    # // (floor division): __floordiv__(self, other)
    # ** (power): __pow__(self, other)
    def __add__(self, other):
        # 只考慮位數比大小
        if self._digits > other._digits:
            big = self
            small = other
        elif self._digits < other._digits:
            big = other
            small = self
        else:
            big = self
            small = other
            for i in range(self._digits):
                if int(self._num[i]) > int(other._num[i]):
                    break
                elif int(other._num[i]) > int(self._num[i]):
                    big = other
                    small = self
                    break

        # 比較正負號
        if self._positive != other._positive:
            # 正負號不同
            ans = self.bigMinusSmall(big._num, small._num)
        else:
            # 正負號相同
            ans = self.bigAddSmall(big._num, small._num)
        ans.sign = big.sign
        return ans

    def __sub__(self, other):
        other.sign = not other.sign
        ans = self + other
        other.sign = not other.sign
        return ans

    def __mul__(self, other):
        n1 = list(self._num[::-1])
        n2 = list(other._num[::-1])
        answers = []
        for i, a in enumerate(n1):
            carry = 0
            ans = []
            for j in range(i):
                ans.append('0')
            for b in n2:
                temp = int(a) * int(b) + carry
                ans.append(str(temp%10))
                carry = temp // 10

            if carry:
                ans.append(str(carry))

            answers.append(ans)

        # print('level = ', len(answers))
        # print(answers)

        result = BigInt('0')
        for ans in answers:
            result = result + BigInt(''.join(ans[::-1]))

        result.sign = not (self.sign ^ other.sign)

        return result

    def __floordiv__(self, other):
        # remainder = self
        # count = self._digits - other._digits
        signs = [self.sign, other.sign]
        self.sign = True
        other.sign = True

        carry = ''
        ans = []
        for i in range(self._digits):
            sz = carry + self._num[i]
            num = BigInt(sz)
            q = 0
            while num >= other:
                num = num - other
                q += 1
            if q == 0:
                carry = carry + num._num[i]
            else:
                ans.append(str(q))
                carry = num._num
                print('q = ', q)
                print('remainder = ', carry)

        # recover signs
        self.sign = signs[0]
        other.sign = signs[1]
        result = BigInt(''.join(ans))
        result.sign = not (self.sign ^ other.sign)

        return result

#################################
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
        a = '12'
        b = '9'
        assert (BigInt(a)+BigInt(b)).value == quick_solution(a + ' + ' + b)
    def test_add_2(self):
        a = '1234'
        b = '66'
        assert (BigInt(a)+BigInt(b)).value == quick_solution(a + ' + ' + b)
    def test_add_3(self):
        a = '66'
        b = '234'
        assert (BigInt(a)+BigInt(b)).value == quick_solution(a + ' + ' + b)
    def test_add_4(self):
        a = '99876'
        b = '321'
        assert (BigInt(a)+BigInt(b)).value == quick_solution(a + ' + ' + b)

    def test_minus_1(self):
        a = '12'
        b = '9'
        assert (BigInt(a)-BigInt(b)).value == quick_solution(a + ' - ' + b)
    def test_minus_2(self):
        a = '1234'
        b = '66'
        assert (BigInt(a)-BigInt(b)).value == quick_solution(a + ' - ' + b)
    def test_minus_3(self):
        a = '66'
        b = '234'
        assert (BigInt(a)-BigInt(b)).value == quick_solution(a + ' - ' + b)
    def test_minus_4(self):
        a = '99876'
        b = '321'
        assert (BigInt(a)-BigInt(b)).value == quick_solution(a + ' - ' + b)

    def test_multipe_1(self):
        a = '99876'
        b = '8888'
        assert (BigInt(a)*BigInt(b)).value == quick_solution(a + ' * ' + b)
    def test_multipe_2(self):
        a = '-567'
        b = '93218'
        assert (BigInt(a)*BigInt(b)).value == quick_solution(a + ' * ' + b)

    def test_divde_1(self):
        a = '99876'
        b = '609'
        assert (BigInt(a)//BigInt(b)).value == quick_solution(a + ' / ' + b)
    def test_divde_2(self):
        a = '-567'
        b = '3'
        assert (BigInt(a)//BigInt(b)).value == quick_solution(a + ' / ' + b)

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

    # a = BigInt('99876')
    # b = BigInt('321')
    # c = a * b
    # print(c)
    # a = '-567'
    # b = '93218'
    # # assert (BigInt(a)*BigInt(b)) == quick_solution(a + ' * ' + b)
    # sz = a + ' * ' + b
    # print(sz)
    # ans = quick_solution(sz)
    # print(ans)
    # # print(type(ans))
    # d = BigInt(a) * BigInt(b)
    # print(d)

    # a = '234'
    # b = '234'
    # c = BigInt(a) - BigInt(b)
    # a = '4'
    # b = '4'
    # d = BigInt(a) - BigInt(b)

    a = '99876'
    b = '609'
    # a = '-567'
    # b = '3'
    e = BigInt(a) // BigInt(b)
    f = quick_solution(a + ' / ' + b)
    print('e = ', e)
    print('f = ', f)
