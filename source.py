'''
=================
source
=================
'''

class Book:
    
    def setData(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author
        print("제목 : ",self.title)
        print('가격 : ',self.price)
        print('지은이 : ', self.author)


    def printData(self):
        print("제목 : ",self.title)
        print('가격 : ',self.price)
        print('지은이 : ', self.author)

    def __repr__(self):
        return print(self.title)
    
    def __init__(self):
        print('객체생성 완료')


book = Book()

book.setData('작은아씨들','7000','미상')

