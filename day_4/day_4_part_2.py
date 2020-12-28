import re


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


def parse_fields_to_dict(line):
    parsed_fields = {}
    for field in line.split():
        field_name, field_value = field.split(":")
        parsed_fields[field_name] = field_value
    return parsed_fields


def is_all_fields_exists(line):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for field in fields:
        if field not in line:
            return False
    return True


def is_byr_valid(byr):
    if type(byr) is str:
        byr = int(byr)

    return 1920 <= byr <= 2002


def is_iyr_valid(iyr):
    if type(iyr) is str:
        iyr = int(iyr)

    return 2010 <= iyr <= 2020


def is_eyr_valid(eyr):
    if type(eyr) is str:
        eyr = int(eyr)

    return 2020 <= eyr <= 2030


def is_hgt_valid(hgt):
    height = int(hgt[:-2])
    if "cm" in hgt:
        return 150 <= height <= 193
    elif "in" in hgt:
        return 59 <= height <= 76


def is_hcl_valid(hcl):
    color_regex = re.compile("#[0-9a-f]{6}")
    return bool(color_regex.match(hcl))


def is_ecl_valid(ecl):
    available_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return  ecl in available_colors


def is_pid_valid(pid):
    return len(pid) == 9 and pid.isdigit()


def is_all_fields_valid(line):
    validations = {
        "byr": is_byr_valid,
        "iyr": is_iyr_valid,
        "eyr": is_eyr_valid,
        "hgt": is_hgt_valid,
        "hcl": is_hcl_valid,
        "ecl": is_ecl_valid,
        "pid": is_pid_valid
    }
    parsed_fields = parse_fields_to_dict(line)
    for field_name, field_value in parsed_fields.items():
        if field_name == "cid":
            continue
        if not validations[field_name](field_value):
            return False
    return True


if __name__ == '__main__':
    counter = 0
    for data_line in make_merged_input_data():
        if is_all_fields_exists(data_line) and is_all_fields_valid(data_line):
            counter += 1
            print(data_line)

    print(f"number of valid passports: {counter}")
