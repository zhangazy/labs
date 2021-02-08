gain = []
n = input()
gain = [int(val) for val in n.split(',')]
max = -10000
cnt = 0
list = [0]
for x in range(len(gain)):
    cnt += gain[x]
    list.append(cnt)
    print(cnt)
for i in list:
    if i > max:
        max = i

print(max)