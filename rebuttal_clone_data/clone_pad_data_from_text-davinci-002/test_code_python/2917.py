def solution():
    total_toys = 120
    larger_pile = 2 * smaller_pile
    smaller_pile = total_toys - larger_pile
    return larger_pile

print(solution())