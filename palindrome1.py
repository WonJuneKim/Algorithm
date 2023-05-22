import collections
# collections 모듈은 Counter 클래스를 사용하기 위해 필요
import sys

word = sys.stdin.readline().rstrip() #입력받은 단어를 가져온다, rstrip()은 문자열 끝의 개행 문자를 제거
check_word = collections.Counter(word) #word의 각 문자의 개수를 세는 Counter 객체인 check_word를 생성
cnt = 0 #변수 cnt 초기화(홀수 개수의 문자를 세는 변수이다)
result = '' #펠린드롬의 앞과 뒤 부분을 저장하는 변수(빈 문자열로 선언)
mid = '' #펠린드롬 가운데에 들어갈 문자를 저장하는 변수(빈 문자열로 선언)
for k, v in list(check_word.items()): #check_word의 각 요소를 순회하며 홀수 개수인 문자를 찾는다.
    if v % 2 == 1: #홀수라면
        mid = k #중간에 들어갈 값으로 저장
        cnt += 1
        if cnt >= 2: #홀수가 2개이상이면 팰린드롬이 될 수 없다!!
            print("I'm Sorry Hansoo")
            exit()

for k, v in sorted(check_word.items()): #check_word의 각 요소를 정렬하여 사전순으로 순회, sorted 함수를 사용하여 정렬
    result += (k * (v // 2)) #정렬된 요소를 순회하면서 result에 각 문자의 절반 개수 만큼 문자를 추가, v//2는 현재  문자 개수를 2로 나눈 몫
print(result + mid + result[::-1]) # result + mid + result[::-1]를 통해 앞 부분, 가운데 문자, 뒷 부분을 이어 붙여 팰린드롬 문자열 완성