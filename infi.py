#!/usr/bin/python


data = open('data', 'r').read().strip()
off = data.rfind(']') + 1
groups = data.count('[')

instructions = zip(*(iter(eval('['  + data[off:].replace(')', '),').rstrip(',') + ']')),) * groups)

pdata = []

count = 0
pos =  map(lambda x: tuple(map(int, x.strip('[,]').split(','))), data[:off].split(']', groups - 1))
for rnd in instructions:
    pos = [(pos[idx][0] + rnd[idx][0], pos[idx][1] + rnd[idx][1]) for idx in range(groups)]
    if len(pos) != len(set(pos)):
        count += 1
        for i, b in enumerate(pos):
            if b[1] >= len(pdata):
                pdata += [''] * ((b[1] + 1) - len(pdata))
            if b[0] >= len(pdata[b[1]]):
                pdata[b[1]] += ' ' * ((b[0] + 1) - len(pdata[b[1]]))
            pdata[b[1]] = pdata[b[1]][:b[0]] + str(i + 1) + pdata[b[1]][b[0] + 1:]
print '\n'.join(pdata)
print count

