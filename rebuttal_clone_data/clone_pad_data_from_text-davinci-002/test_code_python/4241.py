def solution():
    wolfgang_marbles = 16
    ludo_marbles = wolfgang_marbles * 1.25
    michael_marbles = (wolfgang_marbles + ludo_marbles) * (2/3)
    total_marbles = wolfgang_marbles + ludo_marbles + michael_marbles
    marbles_per_person = total_marbles / 3
    result = marbles_per_person
    return result

print(solution())