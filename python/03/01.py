def p1():
    f = open("input", "r")
    c = f.read().split("\n")

    total = 0
    for rucksack in c:
        if rucksack == "":
            continue
        comp_size = int(len(rucksack) / 2)

        sack1 = rucksack[:comp_size].strip()
        sack2 = rucksack[comp_size:].strip()

        sack1_chars = set(sack1)
        sack2_chars = set(sack2)

        wrong_item = "".join(sack1_chars.intersection(sack2_chars))
        priority = 0
        if wrong_item.isupper():
            priority = ord(wrong_item) - 39 + 1
        else:
            priority = ord(wrong_item) - 97 + 1
        print("priority of ", wrong_item, " is ", priority)
        total += priority

    print("total: ", total)


def p2():
    f = open("input", "r")
    c = f.read().split("\n")

    total = 0
    for batch_start in range(0, len(c) - 1, 3):
        if batch_start == "":
            continue

        batch = c[batch_start : batch_start + 3]
        line_sets = []
        for rucksack in batch:
            print('rucksack: ', rucksack)
            line_sets.append(set(rucksack))

        badge = "".join(line_sets[0] & line_sets[1] & line_sets[2])
        priority = 0
        if badge.isupper():
            priority = ord(badge) - 39 + 1
        else:
            priority = ord(badge) - 97 + 1
        print("priority of ", badge, " is ", priority)
        total += priority

    print("total: ", total)


def main():
    p2()


if __name__ == "__main__":
    main()
