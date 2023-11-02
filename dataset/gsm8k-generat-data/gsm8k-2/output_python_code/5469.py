def solution():
    """Henry went to the beach and picked up 17 perfect shells and 52 broken shells. Out of those 52 broken shells, half of them were spiral. Out of the 17 perfect shells, 12 of them were not spiral. How many more broken spiral shells were there than perfect spiral shells?"""
    perfect_shells = 17
    broken_shells = 52
    broken_spiral = broken_shells / 2
    perfect_not_spiral = 12
    perfect_spiral = perfect_shells - perfect_not_spiral
    broken_spiral_diff = broken_spiral - perfect_spiral
    result = broken_spiral_diff
    return result

print(solution())