class BusinessCard:
    def set_info(self, name, email, addr):
        self.name
        self.email
        self.addr
    
class Foo:
    def func1():
        print("function 1")
    def func2(self):
        print(id(self))
        print("function 2")

f=Foo()
#f.func2()   #func2가 작동 되는 이유는 첫번째 인자는 self지만 호출할때 아무것도 전달하지않는 이유
            #"첫번째 인자인 self에 대한값은 파이썬이 자동으로 넘겨준다"

#f.func1() //반대의 개념으로 인자 값을 넘겼는데 받아줄수가 없었기 때문

print('a')
f.func2()
