#모듈 내에 존재하는 변수, 함수, 클래스 등을 직접 임포트 하는 방법
from math import factorial, gcd
import statistics #통계 관련

print(factorial(10))
print(gcd(12, 18))

li = [34, 55, 45, 32, 23, 15]
print(f'평균:{statistics.mean[li]}')
print(f'분산:{statistics.variance[li]}')
print(f'표준편차:{statistics.stdev[li]}')
