# 소수 찾기 lv2
# 문제 설명
# 한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

# 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# 013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.
# 입출력 예
# numbers	return
# 17	    3
# 011	    2
# 입출력 예 설명
# 예제 #1
# [1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

# 예제 #2
# [0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

# 11과 011은 같은 숫자로 취급합니다.

# 풀이
from itertools import permutations

def otherSolution(numbers):
    # 소수를 담을 리스트생성
    num_list = [] 

    for i in range(1, len(numbers)+1): 
        # permutation: 순열, permutations('list', '조합할 원소 개수')
        # temp는 object를 리스트를 담게됨
        temp = permutations(numbers, i) 
        # temp는 1자리 숫자 리스트object, ..., len(numbers)자리 숫자리스트object를 한번씩 담게됨
        for j in temp:
            num_list.append(int(''.join(j))) 

    # int타입으로 바꿧기 때문에 011 == 11이된다.
    # set(list)를 함으로 중복되는 값들을 제거 ex) 011 == 11
    num_list = list(set(num_list))
    answer = len(num_list)

    # [에라토스테네스의 체]를 사용해 소수를 구할 수 있다.
    # pop보다 효율적이게 answer에 len(num_list)를 담고 소수가 아닌걸 걸러낸다.
    # 소수 : 2,3,5,7,11,13,17,19,23,29
    for i in num_list:
        # 0 or 1이 있으면 -1
        if i < 2:
            answer -= 1
        # 2의 배수, 
        # int(i**0.5) : float결과를 정수형으로 내림효과
        # 나누어 떨어지는 수가 있다면 -1하고 break;
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                answer -= 1
                break

    print(num_list)
    return answer

print("other : ", otherSolution("0123"))