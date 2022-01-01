in_list = [544, 7, 15, 447, 12344, 475]
res_list = [number for i, number in enumerate(in_list) if i > 0 and in_list[i] > in_list[i - 1]]
res_list = [num1 for num1, num2 in zip(in_list[1:], in_list[:-1]) if num1 > num2]
print(res_list)