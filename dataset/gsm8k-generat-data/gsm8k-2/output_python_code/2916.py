def solution():
    """If two piles of toys added together make 120 toys in total, and the larger of the two piles is twice as big as the smaller one, how many toys are in the larger pile?"""
    total_toys = 120
    smaller_pile = total_toys / 3  # Assuming the smaller pile is 1/3 of the total
    larger_pile = smaller_pile * 2
    result = larger_pile
    return result

print(solution())