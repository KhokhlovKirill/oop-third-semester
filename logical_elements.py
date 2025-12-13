class LogicalElement:
    def __init__(self):
        self.__inputs = [False, False]
        self._result = False
        self.__next_elem = None
        self.__next_input = 0

    def link(self, next_elem, next_input):
        self.__next_elem = next_elem
        self.__next_input = next_input

    @property
    def result(self):
        return self._result

    def __send_to_next_elem(self):
        if self.__next_input == 1:
            self.__next_elem.input1 = self.result
        elif self.__next_input == 2:
            self.__next_elem.input2 = self.result

    @property
    def input1(self):
        return self.__inputs[0]

    @input1.setter
    def input1(self, value: bool):
        self.__inputs[0] = value
        self.calc()
        self.__send_to_next_elem()

    @property
    def input2(self):
        return self.__inputs[1]

    @input2.setter
    def input2(self, value: bool):
        self.__inputs[1] = value
        self.calc()
        self.__send_to_next_elem()

    def calc(self):
        raise NotImplementedError('Use child classes for logical elements')

class Not(LogicalElement):
    def calc(self):
        self._result = (not self.input1)

class And(LogicalElement):
    def calc(self):
        self._result = (self.input1 and self.input2)

class Or(LogicalElement):
    def calc(self):
        self._result = (self.input1 or self.input2)

print('NAND:')
elem_not = Not()
elem_and = And()

print('A | B | not (A and B)')
for A in range(0, 2):
    for B in range(0, 2):
        elem_and.input1 = A
        elem_and.input2 = B
        elem_not.input1 = elem_and.result
        print(f'{A} | {B} | {int(elem_not.result)}')

print('XOR:')
print('A | B | A XOR B')
elem_and = And()
elem_or1 = Or()
elem_or2 = Or()
elem_not1 = Not()
elem_not2 = Not()
elem_not1.link(elem_or1, 1)
elem_not2.link(elem_or1, 2)
elem_or1.link(elem_and, 1)
elem_or2.link(elem_and, 2)
for A in range(0, 2):
    for B in range(0, 2):
        elem_or2.input1 = A
        elem_or2.input2 = B
        elem_not1.input1 = A
        elem_not2.input1 = B
        print(f'{A} | {B} | {int(elem_and.result)}')
