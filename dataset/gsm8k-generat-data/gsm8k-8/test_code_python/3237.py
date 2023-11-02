def solution():
    # Calculate the total number of pancakes needed for everyone to have a second pancake
    total_pancakes_needed = 2 * 8

    # Calculate the number of pancakes Luther has already made
    pancakes_already_made = 12

    # Calculate the number of pancakes Luther still needs to make
    pancakes_needed = total_pancakes_needed - pancakes_already_made
    result = pancakes_needed
    return result

print(solution())