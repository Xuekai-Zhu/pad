def solution():
    number_of_goats = 4  # Alma is feeding four goats
    total_carrots = 47  # Alma has 47 baby carrots

    # Calculate how many carrots each goat gets
    carrots_per_goat = total_carrots // number_of_goats

    # Calculate how many carrots are left over
    left_over_carrots = total_carrots % number_of_goats
    result = left_over_carrots
    return result

print(solution())