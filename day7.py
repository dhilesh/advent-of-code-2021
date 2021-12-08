
import numpy as np

with open('day7_input.txt','r') as f:
    a = f.readline()
b = a.split(',')
crab_start_pos = np.array([int(k) for k in b])

range(len(crab_start_pos))

def arrange_crabs_distance(crab_start_pos):
    y_test = crab_start_pos
    residual_dist = []
    for x in range(min(y_test),max(y_test)+1):
        residuals = y_test - np.array([x]*len(y_test))
        residual_dist.append(sum(abs(residuals)))
    return min(residual_dist)

def arrange_crabs_fuel(crab_start_pos):
    y_test = crab_start_pos
    costs_array = np.cumsum(range(0,2001))
    costs = []
    for x in range(min(y_test),max(y_test)+1):
        residuals = y_test - np.array([x]*len(y_test))
        cost = np.array([costs_array[abs(x)] for x in residuals])
        costs.append(sum(abs(cost)))
    return min(costs)

if __name__ == '__main__':
    ans1 = arrange_crabs_distance(crab_start_pos)
    ans2 = arrange_crabs_fuel(crab_start_pos)
    print(f'Part 1 answer is: {ans1}. Part 2 answer is: {ans2}.')