#클로저 기초(Closure)
#파이썬 변수 범위(Scope)
#Global 선언
#클로저 사용 이유
#Class -> Closure 구현

#일급함수(일급 객체)
#클로저 기초

#파이썬 변수 범위(scope)

#Ex 1
def func_v1(a):
    print(a)
    print(b)

b=20
#func_v1(10)
def func_v2(a):
    print(a)
    print(b)

func_v2(10)

# Ex 3

c=30

def func_v3(a):
    global c
    print(a)
    print(c)
    c=40

print(c)
func_v3(10)
print(c)

#Clousre(클로저) 사용 이유
#변수를 기억한다.
#서버 프로그래밍 -> 동시성(Concurrency) 제어 -> 메모리 공간에 여러 자원이 접근 -> 교착상태(DeadLock)
#메모리를 공유하지 않고 메시지 전달로 처리하기 위한 ->Erlang
#클로저는 공유하되 변경되지 않는(Immutable, Read Only) 적극적으로 사용 -> 함수형 프로그래밍
#클로저는 불변자료구조 및 atom, STM -> 멀티스레드(Coroutine) 프로그래밍에 강점

a = 100

print(a+100)
print(a+1000)

#결과 누적(함수 사용)
print(sum(range(1,51)))
print(sum(range(51,100)))



# 클래스 이용
class Averager():
    def __init__(self):
        self._series = []

    def __call__(self,v):
        self._series.append(v)
        print('inner >> {} / {}'.format(self._series,len(self._series)))
        return(sum(self._series)/len(self._series))

#인스턴스 생성
averager_cls = Averager()

#누적
print(averager_cls(10))
print(averager_cls(20))
print(averager_cls(30))