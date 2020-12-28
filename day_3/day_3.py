def trees_counter(step, print_map=False):
    counter = 0
    input_data = []
    with open("input") as input_file:
        input_data = input_file.readlines()

    index = 0
    for num in range(0, len(input_data), step[1]):
        line = input_data[num].strip()
        if index == 0:
            index += step[0]
            continue
        while index >= len(line):
            line += line
        if line[index] == "#":
            counter += 1
            line = "".join((line[:index], 'X', line[index + 1:]))
        else:
            line = "".join((line[:index], 'O', line[index + 1:]))
        index += step[0]
        if print_map:
            print(line)
    return counter


if __name__ == '__main__':
    result_1_1 = trees_counter(step=[1, 1])
    result_3_1 = trees_counter(step=[3, 1])
    result_5_1 = trees_counter(step=[5, 1])
    result_7_1 = trees_counter(step=[7, 1])
    result_1_2 = trees_counter(step=[1, 2])
    print(f"With step [1, 1] number of trees: {result_1_1}")
    print(f"With step [3, 1] number of trees: {result_3_1}")
    print(f"With step [5, 1] number of trees: {result_5_1}")
    print(f"With step [7, 1] number of trees: {result_7_1}")
    print(f"With step [1, 2] number of trees: {result_1_2}")
    print(f"multiplying = {result_1_1 * result_3_1 * result_5_1 * result_7_1 * result_1_2}")
