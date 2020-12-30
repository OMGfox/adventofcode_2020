from collections import defaultdict


def split_input_line(line):
    raw_bag_name, raw_bag_content = line.split("contain")
    bag_name = raw_bag_name.strip()
    if "bags" in bag_name:
        bag_name = bag_name[:-1]
    if "no other bags" in raw_bag_content:
        bag_content = None
    else:
        bag_content = defaultdict(dict)
        splitted_bag_content = raw_bag_content.split(",")
        for bags in splitted_bag_content:
            value = bags[:2].strip()
            key = bags[2:].replace(".", "").strip()
            if "bags" in key:
                key = key[:-1]
            bag_content[key] = value

    return bag_name, bag_content


def is_bag_contains(checked_bag, key, packed_input):
    if key == checked_bag or packed_input[key] is None:
        return False
    if checked_bag in packed_input[key]:
        return True
    for bag in packed_input[key]:
        result = is_bag_contains(checked_bag, bag, packed_input)
        if result:
            return True


def color_bag_counter(checked_bag, packed_input):
    counter = 0
    for bag_name in packed_input:
        if is_bag_contains(checked_bag, bag_name, packed_input):
            counter += 1

    return counter


if __name__ == '__main__':
    with open("input") as input_file:
        packed_input = dict()
        for line in input_file:
            key, value = split_input_line(line)
            packed_input[key] = value

        result = color_bag_counter("shiny gold bag", packed_input)
        print(f"result: {result}")
