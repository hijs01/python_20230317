from src.com.python.study.classStudy.Car import Car

if __name__ == '__main__':
    carlist = list()
    c1 = Car('현대지동차', '펠리세이드', '화이트')
    c2 = Car('현대', '쏘나타', '블랙')

    carlist.append(c1)
    carlist.append(c2)
    for carObj in carlist:
        # print(carObj)
        print(f'회사명: {carObj.model}')



