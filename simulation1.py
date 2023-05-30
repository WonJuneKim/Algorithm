import sys

input = sys.stdin.readline

# 숫자
n = int(input())
n, m = map(int, input().split())

# 문자
a = input().strip()

# 문자 띄어쓰기로 배열로 받을 때
b = input().split()


# 두 줄 배열
a = [input().split() for _ in range(2)]


