#! /usr/bin/env python
import sys
import copy

class FootStep(object):
        x=0
        y=0
        v=0

def flatten(ls):
        def iter(a, b):
                if (a==[]):
                        return b
                elif(type(a)==list):
                        return iter(a[0], iter(a[1:], b))
                else:
                        return list(a) + b
        if(ls==[]):
                return ''
        else:
                return ''.join(iter(ls[0], iter(ls[1:], [])))


d = {'up':1<<0,'down':1<<1,'left':1<<2,'right':1<<3}
maxl = {'height':30,'width':30}
map = []
linenum = 0
#f = open('map_sample','r')
for line in sys.stdin:
#for line in f.readlines():
        map.append(list(line.replace('\n','')))
        if 'S' in line:
                sx = line.find('S')
                sy = linenum
        if 'G' in line:
                gx = line.find('G')
                gy = linenum
        linenum+=1

distance = 0
fs = FootStep()
fs.x = sx
fs.y = sy
flog = [fs]

best = maxl['height']*maxl['width']

while 1:
        if flog[-1].x in range(gx-1,gx+1) and flog[-1].y in range(gy-1,gy+1):
                if best > distance:
                        best = distance
                        bmap = copy.deepcopy(map)
        if flog[0].v == ( d['up'] | d['down'] | d['left'] | d['right'] ):
                break
        if distance < best or ((best - distance) >= (gx-flog[-1].x + gy-flog[-1].y)):
                if (flog[-1].v & d['up'])==0 and map[flog[-1].y-1][flog[-1].x]==' ':
                        flog[-1].v |= d['up']
                        tmp = copy.copy(flog[-1])
                        tmp.y -= 1
                        tmp.v = 0
                        flog.append(tmp)
                        map[flog[-1].y][flog[-1].x] = '$'
                        distance+=1
                        continue
                if (flog[-1].v & d['down'])==0 and map[flog[-1].y+1][flog[-1].x]==' ':
                        flog[-1].v |= d['down']
                        tmp = copy.copy(flog[-1])
                        tmp.y += 1
                        tmp.v = 0
                        flog.append(tmp)
                        map[flog[-1].y][flog[-1].x] = '$'
                        distance+=1
                        continue
                if (flog[-1].v & d['left'])==0 and map[flog[-1].y][flog[-1].x-1]==' ':
                        flog[-1].v |= d['left']
                        tmp = copy.copy(flog[-1])
                        tmp.x -= 1
                        tmp.v = 0
                        flog.append(tmp)
                        map[flog[-1].y][flog[-1].x] = '$'
                        distance+=1
                        continue
                if (flog[-1].v & d['right'])==0 and map[flog[-1].y][flog[-1].x+1]==' ':
                        flog[-1].v |= d['right']
                        tmp = copy.copy(flog[-1])
                        tmp.x += 1
                        tmp.v = 0
                        flog.append(tmp)
                        map[flog[-1].y][flog[-1].x] = '$'
                        distance+=1
                        continue
        map[flog[-1].y][flog[-1].x] = ' '
        del flog[-1]
        distance-=1
        if distance ==1:
                break
for line in map:
        print flatten(line)
