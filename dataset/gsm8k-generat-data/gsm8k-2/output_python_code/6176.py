def solution():
    """Lorraine made a pan of brownies and cut them into 16 pieces. Her children ate 25% of the brownies when they got home from school. After dinner, the entire family ate 50% of the remaining brownies. After everyone went to bed, Lorraine ate 1 more brownie. How many brownies are left over?"""
    total_brownies = 16
    children_brownies = total_brownies * 0.25
    remaining_brownies = total_brownies - children_brownies
    family_brownies = remaining_brownies * 0.5
    remaining_brownies -= family_brownies
    lorraine_brownies = remaining_brownies - 1
    result = lorraine_brownies
    return result

print(solution())