with open('day8_input.txt') as f:
    input1 = f.readlines()
input2 = [i.replace('\n','').split('|') for i in input1]
input3 = [[item.strip().split(' ') for item in sublist] for sublist in input2]

def get_ans1():
    ans1 = 0
    unique_digit_lengths = '2347'
    for sample in input3:
        outputs = sample[1]
        for output in outputs:
            if str(len(output)) in unique_digit_lengths: ans1 += 1
            
    return ans1

length_digit_no = {2:'1',3:'7',4:'4',5:'235',6:'069',7:'8'}

def decipher_output(inputs, outputs):
    digit_wires = {length_digit_no[len(i)]:[] for i in inputs}
    for i in inputs: digit_wires[length_digit_no[len(i)]].append(i)

    # figure out 0,6 and 9
    temp = {k:(set(digit_wires['8'][0]) - set(k)).pop() for k in digit_wires['069']}
    for k,v in temp.items():
        if v in digit_wires['1'][0]:        # if missing value is a '1' value then 6
            digit_wires['6'] = [k]
        else:                               # else 0 or 9
            if v in digit_wires['4'][0]:    # if missing value is a '4' value then 0
                digit_wires['0'] = [k] 
            else:                           # else 9
                digit_wires['9'] = [k]   

    # figure out 2,3 and 5
    temp = {k:(set(digit_wires['8'][0]) - set(k)) for k in digit_wires['235']}
    for k,v in temp.items():
        if len( (set(digit_wires['1'][0]) - v) ) == 2:          # if the result set of the intersection of '1' value is 2 then 3
            digit_wires['3'] = [k]
        else:                                                   # 2 or 5
            if v.issubset(set(digit_wires['6'][0])):            # if missing value is a subset of '6' value then 2
                digit_wires['2'] = [k]
            else:                                               # else 5
                digit_wires['5'] = [k]

    del digit_wires['069'], digit_wires['235']

    output_string = ''
    for o in outputs:
        for k,v in digit_wires.items():
            if set(o) == set(v[0]):
                output_string += k

    return int(output_string)


if __name__ == '__main__':
    ans1 = get_ans1()
    ans2 = sum([decipher_output(sample[0],sample[1]) for sample in input3])
    print(f'Answer 1 is {ans1}. Answer 2 is {ans2}.')