class Console:
    def __init__(self, input_file):
        self._accumulator = 0
        self._loaded_input = None
        self._input_file = input_file
        self._current_position = 0
        self._is_finished = False

    def load_input_file(self, input_file):
        self._loaded_input = dict()
        for line_number, line in enumerate(input_file):
            command, value = line.split()
            value = int(value)
            self._loaded_input[line_number] = [command, {"value": value, "times_used": 0}]

    def execute(self):
        while not self._is_finished:
            self._is_finished = not self.next()
        print("accumulator: ", self.accumulator)

    def next(self):
        data = self._loaded_input[self._current_position]
        times_used = data[1]["times_used"]
        if times_used > 0:
            return False
        else:
            data[1]["times_used"] += 1

        command_name = data[0]
        value = data[1]["value"]
        if command_name == 'nop':
            self._nop(value)
        elif command_name == "acc":
            self._acc(value)
        elif command_name == "jmp":
            self._jmp(value)

        return True

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


if __name__ == '__main__':
    with open("input") as input_file:
        console = Console(input_file)
        console.load_input_file(input_file)
        console.execute()
