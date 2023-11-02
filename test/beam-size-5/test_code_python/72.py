def solution():
    # Calculate the total cups of dog food used in the first year
    first_year_cups = (1 * 180) + (2 * 180)  # 1 cup every day for 180 days and 2 cups every day for the rest of its life

    # Calculate the number of bags of dog food needed
    bags_needed = first_year_cups / 110  # 1 bag contains 110 cups

    result = bags_needed
    return result

print(solution())