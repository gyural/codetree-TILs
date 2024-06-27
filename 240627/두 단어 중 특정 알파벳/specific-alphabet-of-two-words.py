from itertools import combinations

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
    words.append([a,b])
set_word = get_set_word(0, words, [], [])

for combi in set_word:
    d=""
    for word in combi:
        d += word

    obj = {}
    for char in d:
        if(char in obj.keys()):
            obj[char] += 1
        else:
            obj[char] = 1

    for key, val in obj.items():
        idx = ord(key)-ord('a')
        result[idx] = max(result[idx], val)
    del obj
for val in result:
    print(val)