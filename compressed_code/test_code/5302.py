def solution():
    
    first_round = 8
    second_round = first_round + 12
    third_round = 1.6 * second_round
    total_fish = first_round + second_round + third_round
    result = total_fish
    return result

print(solution())