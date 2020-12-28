def make_merged_input_data():
    with open("input") as input_file:
        raw_input_data = input_file.readlines()

    merged_input_data = []
    line = ""
    for index in range(len(raw_input_data)):
        data = raw_input_data[index].strip()
        if data == "":
            merged_input_data.append(line)
            line = ""
        else:
            line += " " + data
    merged_input_data.append(line)
    return merged_input_data


def is_all_fields_exists(line):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in fields:
        if field not in line:
            return False
    return True


if __name__ == '__main__':
    counter = 0
    for data_line in make_merged_input_data():
        if is_all_fields_exists(data_line):
            counter += 1
            print(data_line)

    print(f"number of valid passports: {counter}")



