def solution():
    """Michelangelo has 28 ceilings to paint. This week, he paints 12 of them. Next week, he will paint 1/4 the number of ceilings he did this week. How many ceilings will be left to paint after next week?"""
    # Define the total number of ceilings to paint
    TOTAL_CEILINGS = 28

    # Calculate the number of ceilings Michelangelo will paint next week
    next_week_ceiling_count = 12 * 0.25

    # Calculate the total number of ceilings left to paint
    total_ceiling_left = TOTAL_CEILINGS - 12 - next_week_ceiling_count

    # Display the total number of ceilings left to paint
    result = total_ceiling_left
    return result

print(solution())