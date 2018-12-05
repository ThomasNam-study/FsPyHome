import random

# 1. __call__ : 인스턴스 자체를 호출가능하게 할 수 있다.
# 2. __len__ : 클래스 안에 컬랙션형 데이터가 존재할 때 len 함수로 수를 구하게 할 수 있다.
# 3. __contains__ : in 절을 이용하여 데이터를 존재하는지 확인 가능하다.
# 4. __getitem__ : 객체에 [] 연산자로 데이터를 리턴하게 할 수 있다.
# 5. __setitem__ : 객체에 [] 연산자로 데이터를 설정할 수 수 있다.
# 6. __delitem__ : 객체에 [] 연산자로 데이터를 삭제할 수 있다.
# 7. __add__ : + 연산자를 구현할 수 있다.
# 8. __sub__ : - 연산자를 구현할 수 있다.
# 9. __mul__ : * 연산자를 구현할 수 있다.

# 1. __truediv__ : / 연산자를 구현할 수 있다.
# 2. __eq__ : == 연산자를 구현할 수 있다.
# 3. __ne__ : != 연산자를 구현할 수 있다.
# 4. __lt__ : < 연산자를 구현할 수 있다.
# 5. __le__ : <= 연산자를 구현할 수 있다.
# 6. __gt__ : > 연산자를 구현할 수 있다.
# 7. __ge__ : >= 연산자를 구현할 수 있다.

class Wallet:
    money = 0

    # 생성자
    def __init__(self, name):
        self.owner = name

    def __str__(self):
        return "{}의 지갑입니다.".format(self.owner)

    def __repr__(self):
        return "{}의 지갑입니다.".format(self.owner)

    def print_owner_name(self):
        print('owner name is ', self.owner)

    def print_now_money(self):
        print("현재 잔액 : ", self.money)

    def spend(self, m):
        if self.money < m:
            print("돈이 부족합니다.")
        else:
            self.money -= m
            print("{}를 지출했습니다.".format(m))

        self.print_now_money()

    def income(self, m):
        self.money += m
        self.print_now_money()

# 은행 클래스
class Bank:
    name = ""
    phone = ""      # 은행 대표번호
    pattern = ""    # 계좌 번호 생성 패턴

    def __init__(self, name, phone, pattern):
        self.name = name
        self.phone = phone
        self.pattern = pattern

    def __eq__(self, other):
        return self.name == other.name

    # 계좌 번호 랜덤 생성
    def make_account_number(self):
        accountNum = ""
        for p in self.pattern:
            if p == "x":
                accountNum += str(random.randint(0, 9))
            else:
                accountNum += p

        return accountNum

class Account(Wallet):
    bank = None
    account_number = ""
    passwd = ""

    def __init__(self, name, bank, passwd):
        super().__init__(name)
        self.account_number = bank.make_account_number()
        self.bank = bank
        self.passwd = passwd

    def __str__(self):
        return "{}의 계좌입니다. {} 계좌번호 : {}".format(self.owner, self.bank.name, self.account_number)

    # 소유자가 같은 경우면 + 시킨다.
    def __add__(self, other):
        if self.owner == other.owner:
            return self.money + other.money
        else:
            return self.money

    # 인스턴스를 직접 호출한다.
    def __call__(self, *args, **kwargs):
        print("호출되었습니다")

    def __eq__(self, other):
        return self.owner == other.owner

    def __ne__(self, other):
        return self.owner != other.owner

    def print_account_number(self):
        print("계좌 번호는 {} 입니다.".format(self.account_number))

    def send_money(self, money, to, passwd):

        if self.passwd != passwd:
            print("패스워드가 다릅니다. - 고객문의 센터 - " + self.bank.phone)
            return

        sameBank = self.bank == to.bank

        # 송금 수수료
        fee = 0

        if not sameBank:
            fee = 500

        if self.money > money + fee:
            to.money += money
            self.money -= money + fee
            print("{}원을 {}에게 보냈습니다. - 수수료 : {}원".format(money, to.owner, fee))
            self.print_now_money()
        else:
            print("잔액이 부족합니다 - 고객문의 센터 - " + self.bank.phone)


kb = Bank("국민은행", "02-1234-1234", 'xxx-xxxx-xx-xx')
shinhan = Bank("신한은행", "02-4242-1234", 'xxx-xx-xxxx-xxxx')


namAccount = Account("NAM2", kb, "1234")
namAccount1 = Account("NAM2", kb, "1234")
namAccount2 = Account("NAM2", shinhan, "1234")

suzyAccount1 = Account("SUZY", kb, "1234")
suzyAccount2 = Account("SUZY", shinhan, "1234")

print(namAccount)
print(namAccount2)

namAccount.income(50000)
namAccount1.income(150000)
namAccount.send_money(10000, suzyAccount1, "1212")
namAccount.send_money(10000, suzyAccount1, "1234")
namAccount.send_money(10000, suzyAccount2, "1234")


print("합산1 : {}".format(namAccount + suzyAccount1))
print("합산2 : {}".format(namAccount + namAccount1))

