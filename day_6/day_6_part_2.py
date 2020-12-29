from collections import defaultdict


def answer_counter(input_text):
    group_number = 0
    groups = defaultdict(list)
    for line in input_text:
        line = line.strip()
        if line == "":
            group_number += 1
        else:
            groups[group_number].append([char for char in line])

    total = 0
    for values in groups.values():
        buffer = None
        for answers in values:
            if buffer is None:
                buffer = set([answer for answer in answers])
            else:
                buffer = buffer & set([answer for answer in answers])
        total += len(buffer)
    return total


if __name__ == '__main__':
    with open("input") as input_file:
        total = answer_counter(input_file)

    print(f"total sum: {total}")
