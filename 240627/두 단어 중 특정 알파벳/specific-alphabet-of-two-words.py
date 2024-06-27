def get_set_word(idx, arrays, temp, result):
    if(len(arrays) == idx):
        result.append(temp)
        temp = []
        return
    else:
        for w in arrays[idx]:            
            get_set_word(idx+1, arrays, temp+[w], result)
    return result

length = ord('z')-ord('a')+1
result = [0 for i in range(length)]

N = int(input())
words = []

# word 입력받기
for i in range(N):
    a, b = input().split()
    a = list(a)
    b = list(b)
    c = a+b
    c = set(c)

    for k in c:
        idx = ord(k)-ord('a')
        result[idx] += 1

for val in result:
    print(val)