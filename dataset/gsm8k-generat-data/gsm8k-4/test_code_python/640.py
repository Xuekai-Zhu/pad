def solution():
    """Michelangelo has 28 ceilings to paint. This week, he paints 12 of them. Next week, he will paint 1/4 the number of ceilings he did this week. How many ceilings will be left to paint after next week?"""
    # Define the total number of ceilings to paint
    total_ceilings = 28

    # Define the number of ceilings painted this week
    ceilings_painted_this_week = 12

    # Define the number of ceilings painted next week
    ceilings_painted_next_week = ceilings_painted_this_week / 4

    # Calculate the total number of ceilings left to paint
    ceilings_left_to_paint = total_ceilings - ceilings_painted_this_week - ceilings_painted_next_week

    result = ceilings_left_to_paint
    return result

print(solution())