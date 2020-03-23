class CreditCard:

    MAX_PAYMENT_LIMIT = 30000000

    def __init__(self, name, password, payment_limit):
        self.__name = name
        self.__password = password
        self.__payment_limit = payment_limit

    def get_name(self):
        return self.__name
    def get_password(self):
        return "비밀 번호는 볼 수 없습니다"
    def get_payment_limit(self):
        return self.__payment_limit

    def set_name(self, name):
        self.__name = name
    def set_password(self, password):
        self.__password = password
    def set_payment_limit(self, payment_limit):
        if payment_limit >= 0 and payment_limit <= CreditCard.MAX_PAYMENT_LIMIT:
            self.__payment_limit = payment_limit
        else:
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해주세요!")


user1 = CreditCard("Arisa Ichigaya", 1330, 10000000)
print(user1.get_password())
print(user1.get_name())
print(user1.get_payment_limit())

user1.set_name("Kasumi Toyama")
user1.set_password(7770)
user1.set_payment_limit(-50)
print(user1.get_password())
print(user1.get_name())
print(user1.get_payment_limit())