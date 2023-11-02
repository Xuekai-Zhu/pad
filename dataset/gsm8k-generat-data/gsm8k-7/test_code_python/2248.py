def solution():
    first_comp_wins = 40
    second_comp_wins = (5/8) * first_comp_wins
    third_comp_wins = first_comp_wins + second_comp_wins

    total_wins = first_comp_wins + second_comp_wins + third_comp_wins
    result = total_wins
    return result

print(solution())