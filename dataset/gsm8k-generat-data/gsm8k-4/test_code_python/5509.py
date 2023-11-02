def solution():
    """A box of rainbow nerds contains 10 purple candies, 4 more yellow candies, and 2 fewer green candies than yellow candies. How many rainbow nerds are there in the box?"""
    # Define the number of yellow candies
    yellow_candies = None

    # Calculate the number of green candies
    green_candies = yellow_candies - 2

    # Calculate the total number of candies
    total_candies = yellow_candies + purple_candies + green_candies

    # Define the equation for the number of yellow candies
    # yellow_candies = purple_candies + 4

    # Substitute the above equation into the equation for the number of green candies
    # green_candies = purple_candies + 2

    # Substitute the above equations into the equation for the total number of candies
    total_candies = purple_candies + (purple_candies + 4) + (purple_candies + 2)

    # Simplify the equation and solve for purple_candies
    purple_candies = (total_candies - 6) / 3

    # Calculate the number of yellow candies using the first equation
    yellow_candies = purple_candies + 4

    # Calculate the number of green candies using the second equation
    green_candies = yellow_candies - 2

    # Calculate the total number of candies
    total_candies = purple_candies + yellow_candies + green_candies

    # return result
    result = total_candies
    return result

print(solution())