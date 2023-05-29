# PyTuring IT2023 HW2
`TuringMachine` is a class that simulates a Turing machine itself.

The `__init__` method is the initializer for the class.
When a new instance of `TuringMachine` is created, this method sets up the initial state of the machine.
It takes an input string (which we call `tape_string`) and converts it to a list of characters (`self.tape`).
This list represents the tape of the Turing machine.
The `self.head_position` variable is the position of the 'read-write head' of the Turing machine -
this is the part of the machine that can read and write symbols on the tape.
Finally, `self.count` is a variable that keeps track of how many 'x' characters have been encountered.

The `step` method makes the Turing machine perform one 'step' of its operation.
This involves reading the symbol at the current head position and applying the rules of the machine.
In our case, the rules are: if the current symbol is 'x', increment the count;
if the count is a multiple of 3, leave the symbol as 'x'; otherwise, replace it with '$'.
After applying the rule, the head position is incremented to move to the next symbol.

The `run` method makes the Turing machine perform its operation until it has processed all symbols on the tape.
It does this by repeatedly calling the `step` method until the head position reaches the end of the tape.

The expression `''.join([x for x in self.tape if x == 'x'])` creates a new string,
that consists of all the 'x' symbols that are left on the tape after the machine has finished running.

After the TuringMachine class is defined, we create two instances of it, each with a different input string.
We then call the `run` method on each instance and print the result.
The result is the string of 'x' symbols that are left on the tape
after the machine has processed the input string according to its rules.
