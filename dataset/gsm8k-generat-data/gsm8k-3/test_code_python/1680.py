def solution():
    """There were 349 pieces of candy in a bowl. Talitha took 108 pieces and Solomon took 153 pieces. How many pieces of candy remain in the bowl?"""
    # Define the initial number of candies
    initial_candies = 349

    # Define the number of candies taken by Talitha and Solomon
    talitha_candies = 108
    solomon_candies = 153

    # Calculate the remaining number of candies
    remaining_candies = initial_candies - talitha_candies - solomon_candies

    # Display the remaining number of candies
    result = remaining_candies
    return result

print(solution())