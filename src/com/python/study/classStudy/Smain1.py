from src.com.python.study.classStudy.SingtonRepository import SingltonRepository

if __name__ == '__main__':
    userRepository = SingltonRepository.getInstance()
    userRepository.userlist.append("user1")
    print(userRepository.userlist)

    from src.com.python.study.classStudy.Smain2 import test
    test()
    print("git test")

