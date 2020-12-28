
if __name__ == '__main__':
    counter = 0
    with open("input") as input_file:
        for line in input_file:
            condition, password = line.split(sep=":")
            the_range, letter = condition.split()
            min_of_range, max_of_range = the_range.split(sep="-")
            min_of_range = int(min_of_range)
            max_of_range = int(max_of_range)
            checker = 0
            for char in password:
                if char == letter:
                    checker += 1
            if min_of_range <= checker <= max_of_range:
                counter += 1
                print(f"{line.strip()} is valid!")
    print(f"count of valid passwords: {counter}")
