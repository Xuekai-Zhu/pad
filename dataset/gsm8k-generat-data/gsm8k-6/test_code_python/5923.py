def solution():
    # Calculate the total number of fireflies at the beginning
    initial_fireflies = 3

    # Calculate the number of fireflies that joined
    joined_fireflies = 4 + (12-4)  # four less than a dozen more fireflies

    # Calculate the number of fireflies remaining after two flew away
    remaining_fireflies = initial_fireflies + joined_fireflies - 2

    result = remaining_fireflies
    return result

print(solution())