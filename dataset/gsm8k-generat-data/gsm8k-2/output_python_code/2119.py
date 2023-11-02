def solution():
    """In the first round of bowling, Patrick knocked down a total of 70 pins and Richard knocked down 15 more pins than Patrick. In the second round, Patrick knocked down twice as many pins as Richard in the first round and Richard knocked down 3 less than Patrick. How many more pins in total did Richard knock down than Patrick?"""
    patrick_first_round_score = 70
    richard_first_round_score = patrick_first_round_score + 15
    richard_second_round_score = patrick_first_round_score / 2 - 3
    patrick_second_round_score = richard_first_round_score * 2
    patrick_total_score = patrick_first_round_score + patrick_second_round_score
    richard_total_score = richard_first_round_score + richard_second_round_score
    difference = richard_total_score - patrick_total_score
    result = difference
    return result

print(solution())