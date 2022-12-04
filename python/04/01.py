import array


def p1():
    f = open("input", "r")
    c = f.read().split("\n")

    total = 0
    for pairs in c:
        if pairs == "":
            continue
        assignments = pairs.split(",")
        ass1 = list(map(int, assignments[0].split("-")))
        ass2 = list(map(int, assignments[1].split("-")))
        print(ass1)
        print(ass2)
        if (ass1[0] <= ass2[0] and ass1[1] >= ass2[1]) or (
            ass2[0] <= ass1[0] and ass2[1] >= ass1[1]
        ):
            total += 1

    print("total: ", total)


def p2():
    f = open("input", "r")
    c = f.read().split("\n")

    total = 0
    for pairs in c:
        if pairs == "":
            continue
        assignments = pairs.split(",")
        ass1 = list(map(int, assignments[0].split("-")))
        ass2 = list(map(int, assignments[1].split("-")))
        print("*"*8)
        print(ass1)
        print(ass2)
        if (ass1[0] <= ass2[1] and ass1[1] >= ass2[0]) or (
            ass2[0] <= ass1[1] and ass2[1] >= ass1[0]
        ):
            print("IS OVERLAP")
            total += 1

    print("total: ", total)


def main():
    p2()


if __name__ == "__main__":
    main()
