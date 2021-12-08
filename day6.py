
import numpy as np
# from collections import Counter

with open('day6_input.txt','r') as f:
    a = f.readline()
b = a.split(',')
fish_pool = [k for k in b]

def calc_fish_population(days):
    fish_interval_values = {str(i):0 for i in range(9)}
    for num in fish_pool:
        fish_interval_values[num] += 1
    fish_interval_values

    for _ in range(days):
        # print('before',fish_interval_values)
        new_dict = {str(i):0 for i in range(9)}
        for interval,value in fish_interval_values.copy().items():
            if interval == '0':
                new_fish = value
                # new_dict[interval] = 0
            if int(interval) > 0:
                new_dict[str(int(interval)-1)] = value
        new_dict['6'] += new_fish
        new_dict['8'] += new_fish
        fish_interval_values = new_dict
    return sum(fish_interval_values.values())

if __name__ == '__main__':
    ans1 = calc_fish_population(80)
    ans2 = calc_fish_population(256)
    print(f'The answer to part 1 is {ans1}')
    print(f'The answer to part 2 is {ans2}')