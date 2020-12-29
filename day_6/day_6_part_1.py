if __name__ == '__main__':
    total = 0
    with open("input") as input_file:
        group = set()
        for line in input_file:
            line = line.strip()
            if line == "":
                total += len(group)
                group.clear()
            else:
                for char in line:
                    group.add(char)
        total += len(group)

    print(f"total sum: {total}")
