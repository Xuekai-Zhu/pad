def solution():
    # Calculate the number of matches that Krishna won and the number of matches that Callum won
    krishna_won = (3/4) * 8
    callum_won = 8 - krishna_won

    # Calculate the total number of points earned by Callum
    callum_points = callum_won * 10
    result = callum_points
    return result

print(solution())