#소수점 뒤에 양의 정수를 차례대로 붙여 나가면 아래와 같은 무리수를 만들 수 있습니다.

#0.123456789101112131415161718192021...

#이 무리수의 소수점 아래 12번째 자리에는 1이 옵니다 (위에서 붉게 표시된 숫자).

#소수점 아래 n번째 숫자를 dn이라고 했을 때, 아래 식의 값은 얼마입니까?

#d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

#d1=1

List=[i for i in range(1,1000000)]
New=[int(j)  for i in List for j in str(i)]
print(New[0]*New[9]*New[99]*New[999]*New[9999]*New[99999]*New[999999])