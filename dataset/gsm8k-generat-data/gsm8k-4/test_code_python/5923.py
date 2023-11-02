def solution():
    """On a moonless night, three fireflies danced in the evening breeze.  They were joined by four less than a dozen more fireflies, before two of the fireflies flew away.  How many fireflies remained?"""
    # Define the initial number of fireflies
    initial_fireflies = 3

    # Calculate the number of fireflies that joined later
    joined_fireflies = 12 - 4

    # Calculate the total number of fireflies
    total_fireflies = initial_fireflies + joined_fireflies

    # Calculate the number of fireflies that flew away
    flew_away_fireflies = 2

    # Calculate the number of fireflies that remained
    remaining_fireflies = total_fireflies - flew_away_fireflies

    # return the result
    result = remaining_fireflies
    return result

print(solution())