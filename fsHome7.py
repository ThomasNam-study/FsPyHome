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


class Account(Wallet):

    def __init__(self, name, account_number):
        super().__init__(name)
        self.account_number = account_number

    def __str__(self):
        return "{}의 계좌입니다. 계좌번호 : {}".format(self.owner, self.account_number)

    def __add__(self, other):
        return self.money + other.money

    # 인스턴스를 직접 호출한다.
    def __call__(self, *args, **kwargs):
        print("호출되었습니다")

    def print_account_number(self):
        print("계좌 번호는 {} 입니다.".format(self.account_number))

    def send_money(self, money, to):
        if self.money > money:
            to.money += money
            self.money -= money
            print("{}원을 {}에게 보냈습니다.".format(money, to.owner))
            self.print_now_money()


