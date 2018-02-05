import time

n = 3000

# initialize cubes list
cubes = [i**3 for i in range(0, n)]

# init a matrix where sums of pair of cubes are stored
a = [[0 for _ in range(0, n)] for _ in range(0, n)]

# init hash-dict
hd = {}
s = set()

time_start = time.time()
# fulfill matrix
for i in range(0, n-1):
    for j in range(i+1, n):
        val = cubes[i] + cubes[j]
        a[i][j] = val
        # print(val)
        if val in s:
            hd[val].append((i, j))
        else:
            s.add(val)
            hd[val] = []
            hd[val].append((i, j))

filename = 'result.txt'
file = open(filename, 'w')
h1 = 'a^3 + b^3 = '
h2 = 'pairs of numbers'
file.write(h1 + ' '*(60-len(h1)-len(h2)) + h2 + '\n\n')
info = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
for k in hd.keys():
    if len(hd[k]) > 1:
        file.write(str(k) + ' '*(60-len(str(k))-len(str(hd[k]))) + str(hd[
                                                                           k]) +
                   '\n')
        info[len(hd[k])] += 1
    else:
        info[1] += 1

time_end = time.time()
time_diff = time_end - time_start
print('estimated time = ', time_diff)
file.write('\n\tSTATISTICS: \n\n')
file.write('Estimated time: ' + str(time_diff) + ' sec\n')
file.write('Found unique sums: \n')
for k, v in info.items():
    if v != 0:
        file.write("\t" + str(v) + " values where " + str(k)
                   + " pairs have the same value!\n")
file.close()
