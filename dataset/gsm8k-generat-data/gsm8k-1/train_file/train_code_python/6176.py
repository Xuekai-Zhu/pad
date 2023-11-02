def solution():
    """Lorraine made a pan of brownies and cut them into 16 pieces. Her children ate 25% of the brownies when they got home from school. After dinner, the entire family ate 50% of the remaining brownies. After everyone went to bed, Lorraine ate 1 more brownie. How many brownies are left over?"""
    total_brownies = 16
    brownies_eaten_first_round = total_brownies * 0.25
    brownies_left_after_first_round = total_brownies - brownies_eaten_first_round
    brownies_eaten_second_round = brownies_left_after_first_round * 0.5
    brownies_left_after_second_round = brownies_left_after_first_round - brownies_eaten_second_round - 1
    result = brownies_left_after_second_round
    return result

print(solution())