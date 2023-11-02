def solution():
    # Find the number of midfielders in the soccer team
    midfielders = 2 * 10  # twice as many midfielders as defenders

    # Find the total number of players who are goalies, defenders and midfielders
    total = 3 + 10 + midfielders

    # Find the number of strikers in the team
    strikers = 40 - total

    result = strikers
    return result

print(solution())