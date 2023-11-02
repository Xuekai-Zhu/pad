def solution():
    # Calculate the number of cups of flour required for each egg
    cups_per_egg = 0.5

    # Calculate the total number of cups of flour required
    total_cups_of_flour = cups_per_egg * 60

    # Calculate the total number of eggs and cups of flour required
    total = 60 + total_cups_of_flour
    result = total
    return result

print(solution())