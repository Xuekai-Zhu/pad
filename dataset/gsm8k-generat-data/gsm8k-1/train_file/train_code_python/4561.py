def solution():
    """Maynard's dog dug 8 holes in the lawn. Maynard filled in 75% of the hole with dirt. How many holes remain unfilled?"""
    total_holes = 8
    filled_percentage = 75
    filled_holes = total_holes * (filled_percentage / 100)
    unfilled_holes = total_holes - filled_holes
    result = unfilled_holes
    return result

print(solution())