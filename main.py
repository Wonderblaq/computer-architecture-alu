from logic_gates import NAND_gate
from logic_gates import NOT_gate
from logic_gates import AND_gate
from logic_gates import OR_gate
from logic_gates import XOR_gate

# CREATING AND ADDER CIRCUIT
def half_adder(a, b):
    s = XOR_gate(a, b)
    c = AND_gate(a, b)
    return (s, c)


def full_adder(a, b, c):
    s = XOR_gate(XOR_gate(a, b), c)
    c1 = AND_gate(a, b)
    c2 = AND_gate(XOR_gate(a, b), c)
    c_out = OR_gate(c1, c2)
    return (s, c_out)


def ALU(a, b, c, opcode):
    if opcode == 0:
        s, c = half_adder(a, b)
        return (s, c)

    elif opcode == 1:
        s, c = full_adder(a, b, c)
        return (s, c)

    # Increment
    elif opcode == 2:
        s, c = full_adder(a, 0, 1)
        return (s, c)

    # Optional Decrement
    elif opcode == 3:
        s = NOT_gate(a)
        c = NOT_gate(a)
        return (s, c)


print(ALU(1, 1, 1, 3))



