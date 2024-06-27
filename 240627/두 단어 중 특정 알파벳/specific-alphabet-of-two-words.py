length = ord('z')-ord('a')+1
result = [0 for i in range(length)]

N = int(input())
words = []

# word 입력받기
for i in range(N):
    a, b = input().split()
    a = list(a)
    b = list(b)
    
    temp1 = [0] * length
    temp2 = [0] * length
    for char in a:
        idx = ord(char)-ord('a')
        temp1[idx] +=1
    for char in b:
        idx = ord(char)-ord('a')
        temp2[idx] +=1
    
    for idx in range(length):
        result[idx]+= max(temp1[idx], temp2[idx])

for val in result:
    print(val)