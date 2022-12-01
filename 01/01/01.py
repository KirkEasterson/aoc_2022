def p1():
    f = open("input1", "r")
    c = f.read().split("\n")

    curr_max = 0
    local_max = 0
    for cal in c:
        if cal == "":
            if local_max > curr_max:
                curr_max = local_max
            local_max = 0
            continue
        local_max += int(cal)
    print(curr_max)


def p2():
    f = open("input2", "r")
    c = f.read().split("\n")

    local_cals_total = 0
    cals = []
    for cal in c:
        if cal == "":
            cals.append(local_cals_total)
            local_cals_total = 0
            continue
        local_cals_total += int(cal)
    cals.sort(reverse=True)
    print(sum(cals[0:3]))


def main():
    p2()


if __name__ == "__main__":
    main()
