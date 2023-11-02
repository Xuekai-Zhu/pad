def solution():
    winning_score = 11
    if winning_score == 2 or winning_score == 3 or winning_score == 5 or winning_score == 7 or winning_score == 11:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())