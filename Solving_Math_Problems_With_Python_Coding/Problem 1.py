#10보다 작은 자연수 중에서 3 또는 5의 배수는 3, 5, 6, 9 이고, 이것을 모두 더하면 23입니다.
#1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?

def Solution():
    L=[]
    tide=[]
    result=0
    a=0
    for i in range(1,1000):
        L.append(i)
    print(L)
    for i in L:
      if i%3==0:
        result+=i
        tide.append(i)
      elif i%5==0:
        result+=i
        tide.append(i)
      elif i%3==0 and i%5==0:
        reult+=i
        tide.append(i)

    print(tide)
    print(result)
Solution()
