def solution():
    """A box of rainbow nerds contains 10 purple candies, 4 more yellow candies, and 2 fewer green candies than yellow candies. How many rainbow nerds are there in the box?"""
    # Define the number of purple candies
    purple_candies = 10

    # Calculate the number of yellow candies
    yellow_candies = purple_candies + 4

    # Calculate the number of green candies
    green_candies = yellow_candies - 2

    # Calculate the total number of candies
    total_candies = purple_candies + yellow_candies + green_candies

    # Display the total number of candies
    result = total_candies
    return result

print(solution())