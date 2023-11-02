def solution():
    # Find the total number of sweets initially
    initial_total = 30 + 40 + 50

    # Calculate the number of sweets Aaron eats
    aaron_total_eaten = 0.5 * initial_total

    # Calculate the number of cherry sweets left after Aaron gives 5 to his friend
    cherry_left = 0.5 * 30 - 5

    # Calculate the total number of sweets left
    total_left = cherry_left + 0.5 * 40 + 0.5 * 50

    result = total_left
    return result

print(solution())