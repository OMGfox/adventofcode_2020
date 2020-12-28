def decode_row_number(code):
    left, right = 0, 127
    for index, char in enumerate(code):
        if char == "F":
            right = (left + right) // 2
        else:
            left = round((left + right) / 2)
        if index == len(code) - 1:
            return left if char == "F" else right


def decode_column_number(code):
    left, right = 0, 7
    for index, char in enumerate(code):
        if char == "L":
            right = (left + right) // 2
        else:
            left = round((left + right) / 2)
        if index == len(code) - 1:
            return left if char == "L" else right


if __name__ == '__main__':
    seats_id = []
    with open("input") as input_file:
        for line in input_file:
            line = line.strip()
            row_code, column_code = (line[:-3], line[-3:])
            row_number = decode_row_number(row_code)
            column_number = decode_column_number(column_code)
            seat_id = row_number * 8 + column_number
            seats_id.append(seat_id)
            print(line, seat_id)

    print(max(seats_id))
