from collections import defaultdict


def pack_input_to_dict(file_name):
    with open(file_name) as input_file:
        packed_input = dict()
        for line in input_file:
            key, value = split_input_line(line)
            packed_input[key] = value
        return packed_input


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
            bag_content[key] = int(value)

    return bag_name, bag_content


def count_bags_inside(bag_name, packed_input, factor=1):
    counter = 0
    if packed_input[bag_name] is None:
        return 0
    else:
        counter += sum((value * factor for key, value in packed_input[bag_name].items()))
    for key, value in packed_input[bag_name].items():
        counter += count_bags_inside(bag_name=key, packed_input=packed_input, factor=value*factor)

    return counter


if __name__ == '__main__':
    packed_input = pack_input_to_dict("input")
    print(packed_input)
    result = count_bags_inside(bag_name="shiny gold bag", packed_input=packed_input)
    print(f"result: {result}")
