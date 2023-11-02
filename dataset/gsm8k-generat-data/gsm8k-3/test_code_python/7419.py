def solution():
    """Tapanga and Corey have 66 candies together. However, Tapanga has 8 more candies than Corey. How many candies does Corey have?"""
    # Define the total number of candies
    total_candies = 66

    # Calculate the number of candies Tapanga has
    tapanga_candies = (total_candies + 8) / 2

    # Calculate the number of candies Corey has
    corey_candies = total_candies - tapanga_candies

    # Display the number of candies Corey has
    result = corey_candies
    return result

print(solution())