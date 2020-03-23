class User:
    """
    User 클래스: SNS의 유저를 나타내는 클래스

    USER Class
    VAR Count == SNS유저를 나타내는 클래스
    """
    count = 0


    def __init__(self, name, email, pw):
        """
        __init__ 메소드: 이름, 이메일, 비밀번호를 인스턴스 변수로 갖고, 인스턴스가 생성될 때마다 클래스 변수 count를 1씩 증가시킨다
        :param name: Instance로 부터 받는 이름
        :param email: Instance로 부터 받는 E-mail Address
        :param pw: Instance로 부터 받는 Password

        전부 Instance 값을 INIT하는데 사용

        Instance INIT하는 동시 User Class VAR에 Count값을 1개 증가시킨다.

        """
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1

    def say_hello(self):
        """
        say_hello 메소드: 유저의 이름을 포함한 인사 메시지를 출력한다
        :return: Prints out User name from a particular instance.
        """
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def __str__(self):
        """
        __str__ 메소드: 유저 정보를 정의된 문자열 형태로 리턴한다
        :return: Prints out already defined string form.
        """
        return "사용자: {}, 이메일: {}, 비밀번호: ******".format(self.name, self.email)

    @classmethod
    def number_of_users(cls):
        """
        number_of_users 메소드: 총 유저 수를 출력하는 클래스 메소드
        :return: Prints out total of users from @classmethod.
        """
        print("총 유저 수는: {}입니다".format(cls.count))

help(User)
