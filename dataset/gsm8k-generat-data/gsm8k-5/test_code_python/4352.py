def solution():
    # Calculate the cost of renting tablecloths for all 20 tables
    tablecloth_cost = 20 * 25

    # Calculate the cost of renting place settings for all 20 tables
    place_setting_cost = 20 * 4 * 10

    # Calculate the cost of roses for all centerpieces
    rose_cost = 20 * 10 * 5

    # Calculate the cost of lilies for all centerpieces
    lily_cost = 20 * 15 * 4

    # Calculate the total cost of all decorations
    total_cost = tablecloth_cost + place_setting_cost + rose_cost + lily_cost
    result = total_cost
    return result

print(solution())