#2 ≤ a ≤ 5 이고 2 ≤ b ≤ 5인 두 정수 a, b로 만들 수 있는 ab의 모든 조합을 구하면 다음과 같습니다.

#22=4,  23=8,  24=16,  25=32
#32=9,  33=27,  34=81,  35=243
#42=16,  43=64,  44=256,  45=1024
#52=25,  53=125,  54=625,  55=3125
#여기서 중복된 것을 빼고 크기 순으로 나열하면 아래와 같은 15개의 수가 됩니다.

#4,  8,  9,  16,  25,  27,  32,  64,  81,  125,  243,  256,  625,  1024,  3125

#그러면, 2 ≤ a ≤ 100 이고 2 ≤ b ≤ 100인 a, b를 가지고 만들 수 있는 ab는 중복을 제외하면 모두 몇 개입니까?
Result=[]

for a in range(2,101):
    for b in range(2,101):
        if a**b not in Result:
            Result.append(a**b)
        if b**a not in Result:
            Result.append(b**a)

Result.sort()
print(Result)
print(len(Result))

#another Solution
#ans = set([])
#for a in range(2,101):
#  for b in range(2,101):
#    ans.update({a**b})
#print(len(ans))
#set이 중복을 허용하지 않는것을 활용!

#another Solution 2
print(len({a ** b for a in range(2, 101) for b in range(2, 101)}))
#한줄로도 가능하네...
