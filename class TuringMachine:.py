class TuringMachine:
    def __init__(self, tape_string):
        self.tape = list(tape_string)
        self.head_position = 0
        self.count = 0  # Keep count of 'x'

    def step(self):
        if self.tape[self.head_position] == 'x':
            self.count += 1
            if self.count % 3 != 0:  # Only keep every third 'x'
                self.tape[self.head_position] = '$'
        self.head_position += 1

    def run(self):
        while self.head_position < len(self.tape):
            self.step()
        # Only keep 'x' in the tape
        return ''.join([x for x in self.tape if x == 'x'])


tm = TuringMachine('xxxxxxxxx')
print(tm.run())  # Output: xxx

tm = TuringMachine('xxxxxxxx')
print(tm.run())  # Output: xx

tm = TuringMachine('xxx')
print(tm.run())  # Output: x

