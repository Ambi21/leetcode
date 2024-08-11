strs = ["flower","flowe","fligh"]
str1 = strs[0]
n = 0
for i in range(len(strs) - 1):
    strs[i] = str1
    str1 = ''
    if len(strs[i]) > len(strs[i+1]):
        n = len(strs[i+1])
    else:
        n = len(strs[i])
    for j in range(n):
        if strs[i][j] == strs[i+1][j]:
            str1 += strs[i][j]
    
print(str1)