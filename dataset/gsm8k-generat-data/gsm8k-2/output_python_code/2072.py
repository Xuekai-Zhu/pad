def solution():
    """Alex had 36 ounces of jelly beans. He ate 6 ounces. Then he divided the rest equally into 3 piles. How much does each pile weigh?"""
    initial_weight = 36
    eaten_weight = 6
    remaining_weight = initial_weight - eaten_weight
    pile_weight = remaining_weight / 3
    result = pile_weight
    return result

print(solution())