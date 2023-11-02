def solution():
    first_round_patrick = 70
    first_round_richard = first_round_patrick + 15
    second_round_patrick = first_round_richard * 2
    second_round_richard = second_round_patrick - 3
    difference_in_score = second_round_richard - first_round_patrick
    result = difference_in_score
    return result

print(solution())