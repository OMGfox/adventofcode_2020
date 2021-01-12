from copy import deepcopy


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
            return(guess)


def find_contiguous_range(input_file, incorrect_number):
    raw_frame = list()
    for line in input_file:
        number = int(line)
        if number == incorrect_number:
            break
        raw_frame.append(int(line))

    for i in range(len(raw_frame)):
        frame_window = list()
        for number in raw_frame[i:]:
            frame_window.append(number)
            if sum(frame_window) == incorrect_number:
                return frame_window
        frame_window.clear()
    return None


if __name__ == '__main__':
    print("\n# with real input:")
    with open("input") as input_file:
        result = processing(input_file)
        input_file.seek(0)
        result_range = find_contiguous_range(input_file, result)
        print(result_range)
        print("result = ", max(result_range) + min(result_range))
