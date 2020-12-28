if __name__ == '__main__':
    counter = 0
    with open("input") as input_file:
        for line in input_file:
            condition, password = line.split(sep=":")
            password = password.strip()
            positions, letter = condition.split()
            first_pos, second_pos = positions.split(sep="-")
            first_pos = int(first_pos) - 1
            second_pos = int(second_pos) - 1
            checker = 0
            first_pos_letter = password[first_pos]
            second_pos_letter = password[second_pos]
            if (first_pos_letter == letter and second_pos_letter != letter or
                    second_pos_letter == letter and first_pos_letter != letter):
                counter += 1
                print(f"{line.strip()} is valid!")
    print(f"number of valid passwords: {counter}")
