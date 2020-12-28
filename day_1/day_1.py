
if __name__ == '__main__':
    input_data = []
    with open("input") as input_file:
        for line in input_file:
            input_data.append(int(line))

    for i in range(len(input_data)):
        for j in range(i + 1, len(input_data)):
            num1 = input_data[i]
            num2 = input_data[j]
            result = num1 + num2
            if result == 2020:
                multiplying = num1 * num2
                print(f"{input_data[i]} + {input_data[j]} = {result} (multiplying is {multiplying})")
