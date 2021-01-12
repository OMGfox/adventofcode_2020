def validation(frame, guess):
    for i in range(0, len(frame) - 1):
        for j in range(i + 1, len(frame)):
            if frame[i] + frame[j] == guess:
                # print(f"{frame[i]} + {frame[j]} = {guess}")
                return True
    return False


def processing(input_file, preamble=25):
    frame = list()
    for line in input_file:
        if len(frame) < preamble:
            frame.append(int(line))
        else:
            guess = int(line)
            if validation(frame, guess):
                frame.pop(0)
                frame.append(guess)
                continue
            print("result = ", guess)
            break


if __name__ == '__main__':
    test_preamble = 5
    print("# test input:")
    with open("test_input") as test_input_file:
        processing(test_input_file, test_preamble)

    preamble = 25
    print("\n# real input:")
    with open("input") as input_file:
        processing(input_file)
