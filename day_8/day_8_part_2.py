from copy import deepcopy

class Console:

    def __init__(self, input_file):
        self._accumulator = 0
        self._loaded_input = None
        self._loaded_input_copy = None
        self._input_file = input_file
        self._current_position = 0
        self._is_finished = False

    def load_input_file(self, input_file):
        self._loaded_input = dict()
        for line_number, line in enumerate(input_file):
            command, value = line.split()
            value = int(value)
            self._loaded_input[line_number] = [command, {"value": value, "times_used": 0}]

    def execute(self, invert_index_command=None):
        self._loaded_input_copy = deepcopy(self._loaded_input)
        if invert_index_command is not None:
            data = self._loaded_input_copy[invert_index_command]
            if data[0] == "nop":
                data[0] = 'jmp'
            elif data[0] == "jmp":
                data[0] = "nop"
        print(f"---------------state {invert_index_command} ---------------------")
        while not self._is_finished:
            print(self.accumulator)
            self._is_finished = not self.next()
        print("final_result", self.accumulator)
        self.reset()

    def next(self):
        data = self._loaded_input_copy[self._current_position]
        times_used = data[1]["times_used"]
        if times_used > 0:
            return False
        else:
            data[1]["times_used"] += 1

        previous_position = self._current_position
        command_name = data[0]
        value = data[1]["value"]
        if command_name == 'nop':
            self._nop(value)
        elif command_name == "acc":
            self._acc(value)
        elif command_name == "jmp":
            self._jmp(value)

        if previous_position == self._current_position:
            print("loop detected")
            return False

        return True

    def reset(self):
        self._accumulator = 0
        self._current_position = 0
        self._is_finished = False

    def _nop(self, value):
        self._current_position += 1

    def _acc(self, value):
        self._accumulator += value
        self._current_position += 1

    def _jmp(self, value):
        self._current_position += value

    @property
    def accumulator(self):
        return self._accumulator

    @property
    def loaded_input_len(self):
        return len(self._loaded_input)


if __name__ == '__main__':
    with open("input") as input_file:
        console = Console(input_file)
        console.load_input_file(input_file)
        for i in range(console.loaded_input_len):
            try:
                console.execute(invert_index_command=i)
            except:
                pass

### 672 is the last printed value and it's fit as a true answer
### but i'm not sure that it work ok
### please fix it if anybody can

