shape_points = {
    "A": 1,
    "B": 2,
    "C": 3,
    "X": 1,
    "Y": 2,
    "Z": 3,
}

def calc_outcome_points(opp, me):
    if shape_points[opp] == shape_points[me]:
        return 3  # draw
    match opp:
        case "A":
            if me == 'Y':
                return 6
        case "B":
            if me == 'Z':
                return 6
        case "C":
            if me == 'X':
                return 6

    return 0



def calculate_hand(opp, me):
    outcome_points = calc_outcome_points(opp,me)
    return shape_points[me] + outcome_points

def get_appropriate_hand(opp, res):
    match res:
        case "X":  # lose
            if opp == 'A':
                return 'Z'
            elif opp == 'B':
                return 'X'
            else:
                return 'Y'
        case "Y":  # draw
            if opp == 'A':
                return 'X'
            elif opp == 'B':
                return 'Y'
            else:
                return 'Z'
        case "Z":  # win
            if opp == 'A':
                return 'Y'
            elif opp == 'B':
                return 'Z'
            else:
                return 'X'


def p1():
    f = open("input", "r")
    c = f.read().split("\n")

    total_points = 0
    for round in c:
        if round == '':
            continue
        moves = round.split(" ")
        round_points = calculate_hand(moves[0], moves[1])
        print('round points: ', round_points)
        total_points += round_points

    print(total_points)



def p2():
    f = open("input", "r")
    c = f.read().split("\n")

    total_points = 0
    for round in c:
        if round == '':
            continue
        moves = round.split(" ")
        me = get_appropriate_hand(moves[1])
        round_points = calculate_hand(moves[0], me)
        print('round points: ', round_points)
        total_points += round_points

    print(total_points)


def main():
    p2()


if __name__ == "__main__":
    main()
