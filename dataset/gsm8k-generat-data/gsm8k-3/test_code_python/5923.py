def solution():
    """On a moonless night, three fireflies danced in the evening breeze.  They were joined by four less than a dozen more fireflies, before two of the fireflies flew away.  How many fireflies remained?"""
    # Define the starting number of fireflies
    starting_fireflies = 3

    # Calculate the number of fireflies that joined
    joining_fireflies = 12 - 4
    total_fireflies = starting_fireflies + joining_fireflies

    # Calculate the number of fireflies that flew away
    flying_fireflies = 2
    remaining_fireflies = total_fireflies - flying_fireflies

    # Display the number of fireflies that remained
    result = remaining_fireflies
    return result

print(solution())