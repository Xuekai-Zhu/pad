def solution():
    """Every morning, Jason eats an omelet made using three eggs. How many eggs will Jason consume in two weeks?"""
    # Define the number of eggs per omelet and the number of days in two weeks
    EGGS_PER_OMELET = 3
    DAYS_IN_TWO_WEEKS = 14

    # Calculate the total number of eggs consumed in two weeks
    total_eggs = EGGS_PER_OMELET * DAYS_IN_TWO_WEEKS

    # return the result
    result = total_eggs
    return result

print(solution())