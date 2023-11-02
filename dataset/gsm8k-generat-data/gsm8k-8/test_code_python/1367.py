def solution():
    # Define the number of backers at each level
    highest_backers = 2
    second_backers = 3
    lowest_backers = 10

    # Calculate the total amount raised
    total_raised = (highest_backers * 1000) + (second_backers * 100) + (lowest_backers * 10)

    # Determine the highest level of financial backing
    highest_level = total_raised / highest_backers

    result = highest_level
    return result

print(solution())