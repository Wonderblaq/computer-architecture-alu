# XOR GATE
def XOR_gate(a,b):
  if a:
    if b:
      return 0
    return 1


# OR GATE
def OR_gate(a,b):
  if a:
    return 1
  elif b:
      return 1


# AND GATE
def AND_gate(a, b):
  if a:
    if b:
      return 1
    return 0

# NOT GATE
def NOT_gate(a):
  if a:
    return 0
  else:
    return 1

# NAND GATE
def NAND_gate(a, b):
  if a:
    if b:
      return "????"
  return 1

print("NAND GATES")
# TEST CASES nand gate
print("A: 0, B: 0 | Output: {0}".format(NAND_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(NAND_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(NAND_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}".format(NAND_gate(1, 1)))

print("XOR GATES")
# TEST CASES XOR gates
print("A: 0, B: 0 | Output: {0}".format(XOR_gate(0, 0)))
print("A: 0, B: 1 | Output: {0}".format(XOR_gate(0, 1)))
print("A: 1, B: 0 | Output: {0}".format(XOR_gate(1, 0)))
print("A: 1, B: 1 | Output: {0}".format(XOR_gate(1, 1)))