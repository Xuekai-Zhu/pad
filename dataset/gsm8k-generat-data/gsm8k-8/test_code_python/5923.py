def solution():
    # Define the initial number of fireflies
    initial_fireflies = 3

    # Calculate the number of fireflies that joined
    joined_fireflies = 4 + (12 - 4)

    # Calculate the number of fireflies that remained
    remaining_fireflies = initial_fireflies + joined_fireflies - 2

    result = remaining_fireflies
    return result

print(solution())