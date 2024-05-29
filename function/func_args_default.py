
'''
#인수의 기본값

-파이썬에서는 인수의 기본값을 설정하여,
자주 바뀌지 않는 매개값은 기본값으로 처리할 수 있게 함
'''

def calc_stepsum(begin, end, step=1): #기본값 설정
    sum = 0
    for n in range(begin, end+1, step):
        sum += n
    return sum

print(calc_stepsum(1,10))
print(calc_stepsum(1,10,2)) #step 2로 변경
      
      
#기본값이 지정된 매개변수를 오른쪽으로 몰아야 함
def calc_sum(end, begin=0, step=1): #end 1번으로 설정
    sum = 0
    for n in range(begin, end+1, step):
        sum += n
    return sum

print(calc_sum(100))
