#가
number = [i for i in range(1, 11)]

#나
text="'{}% 진행중'"

#다
for i in number:
    print(i)
print()

#라
for i in number:
    print(text.format(i))
print()

#마
def isEvenOrOdd(A, B):
    if (A*B)%2==0:
        print('두 수의 곱은 짝수입니다.')
    else:
        print('두 수의 곱은 홀수입니다.')
isEvenOrOdd(1513, 351323)