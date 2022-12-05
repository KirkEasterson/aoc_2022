import array
import numpy as np


def p2():
    f = open("input", "r")
    c = f.read().split("\n")

    # GET THE STACK
    stacks = []
    i = 0
    while i < len(c):
        line = c[i]
        if line == "":
            break

        items = []  # items for the line
        for j in range(0, len(line), 4):
            if line[j] == " ":  # is empty spot
                items.append(None)
                continue

            items.append(line[j + 1])  # the ID of the box
        stacks.append(items)
        i += 1

    stacks = stacks[: len(stacks) - 1]

    # get longest row
    max_len = 0
    for row in stacks:
        if len(row) > max_len:
            max_len = len(row)
    # print("max row: ", max_len)

    # fill out remaining bits
    for row in stacks:
        for j in range(len(row), max_len):
            row.append(None)
    # print("filled out stack:")
    # print(stacks)

    # invert the stack
    transposed_stack = np.transpose(stacks)

    # reverse each stack
    transposed_stack = np.flip(transposed_stack, 1)
    # print(transposed_stack)

    # stop the np nonsense
    formatted_stack = np.ndarray.tolist(transposed_stack)
    for k in range(len(formatted_stack)):
        formatted_stack[k] = [j for j in formatted_stack[k] if j is not None]
    # print(formatted_stack)

    # GET THE INSTRUCTIONS
    i += 1
    instrs = []
    while i < len(c):
        line = c[i]
        if line == "":
            break
        i += 1
        split_line = line.split(" ")
        instrs.append([int(split_line[1]), int(split_line[3]), int(split_line[5])])

    # follow the instructions
    for instr in instrs:
        # print('instr: ', instr)
        # print(formatted_stack)
        move_x = instr[0]
        from_x = instr[1] - 1
        to_x = instr[2] - 1
        boxes = formatted_stack[from_x][-move_x:]
        formatted_stack[from_x] = formatted_stack[from_x][:-move_x]
        formatted_stack[to_x].extend(boxes)

    # print the result
    res = ""
    for stack in formatted_stack:
        res += str(stack[-1])
    print("result: ", res)


def p1():
    f = open("input", "r")
    c = f.read().split("\n")

    # GET THE STACK
    stacks = []
    i = 0
    while i < len(c):
        line = c[i]
        if line == "":
            break

        items = []  # items for the line
        for j in range(0, len(line), 4):
            if line[j] == " ":  # is empty spot
                items.append(None)
                continue

            items.append(line[j + 1])  # the ID of the box
        stacks.append(items)
        i += 1

    stacks = stacks[: len(stacks) - 1]

    # get longest row
    max_len = 0
    for row in stacks:
        if len(row) > max_len:
            max_len = len(row)
    # print("max row: ", max_len)

    # fill out remaining bits
    for row in stacks:
        for j in range(len(row), max_len):
            row.append(None)
    # print("filled out stack:")
    # print(stacks)

    # invert the stack
    transposed_stack = np.transpose(stacks)

    # reverse each stack
    transposed_stack = np.flip(transposed_stack, 1)
    # print(transposed_stack)

    # stop the np nonsense
    formatted_stack = np.ndarray.tolist(transposed_stack)
    for k in range(len(formatted_stack)):
        formatted_stack[k] = [j for j in formatted_stack[k] if j is not None]
    # print(formatted_stack)

    # GET THE INSTRUCTIONS
    i += 1
    instrs = []
    while i < len(c):
        line = c[i]
        if line == "":
            break
        i += 1
        split_line = line.split(" ")
        instrs.append([int(split_line[1]), int(split_line[3]), int(split_line[5])])

    # follow the instructions
    for instr in instrs:
        # print('instr: ', instr)
        # print(formatted_stack)
        move_x = instr[0]
        from_x = instr[1] - 1
        to_x = instr[2] - 1
        for j in range(move_x):
            box = formatted_stack[from_x].pop()
            formatted_stack[to_x].append(box)

    # print the result
    res = ""
    for stack in formatted_stack:
        res += str(stack[-1])
    print("result: ", res)


def main():
    p2()


if __name__ == "__main__":
    main()
