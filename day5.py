import numpy as np
from collections import Counter

with open('day5_input.txt','r') as f:
    a = f.readlines()
a = [b.replace('\n','') for b in a]
b = [b.split(' -> ') for b in a]
c = [[item.split(',') for item in sublist] for sublist in b]

horizontal_and_vertical = []
for line in c:
    x0, y0, x1, y1 = line[0][0] , line[0][1] , line[1][0] , line[1][1]
    if x0 == x1 or y0 == y1:
        horizontal_and_vertical.append(line)

def get_line_points(p0,p1):
    x_diff = int(p0[0]) - int(p1[0])
    y_diff = int(p0[1]) - int(p1[1])
    x_range = np.array( range( min(int(p0[0]),int(p1[0])) , max(int(p0[0]),int(p1[0]))+1 ))
    y_range = np.array( range( min(int(p0[1]),int(p1[1])) , max(int(p0[1]),int(p1[1]))+1 ))

    if x_diff == 0:
        points = [[str(x_range[0]),str(y)] for y in y_range]
    elif y_diff == 0:
        points = [[str(x),str(y_range[0])] for x in x_range]
    else:
        m = y_diff / x_diff
        c = int(p0[1]) - m*int(p0[0])
        y = m*np.array(x_range) + c
        y = [int(i) for i in y]
        points = [[str(x_range[i]),str(y[i])] for i,x in enumerate(x_range)]

    return points

def get_ans1():
    all_points = [get_line_points(x[0],x[1]) for x in horizontal_and_vertical]
    all_points = [','.join(x) for sublist in all_points for x in sublist]
    overlap_count = Counter(all_points)
    ans1 = len([x for x in overlap_count.items() if x[1]>1])
    print(ans1) # 5145

def get_ans2():
    all_points = [get_line_points(x[0],x[1]) for x in c]
    all_points = [','.join(x) for sublist in all_points for x in sublist]
    all_points
    overlap_count = Counter(all_points)
    ans2 = len([x for x in overlap_count.items() if x[1]>1])
    print(ans2) # 16518

if __name__ == '__main__':
    get_ans1()
    get_ans2()