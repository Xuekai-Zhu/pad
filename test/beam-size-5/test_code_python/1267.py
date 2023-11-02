def solution():
    
    # Define the number of red candies
    red_candies = 54

    # Calculate the number of orange candies
    orange_candies = red_candies * 2

    # Calculate the number of yellow candies
    yellow_candies = red_candies / 2

    # Calculate the total number of candies
    total_candies = red_candies + orange_candies + yellow_candies

    # Calculate the number of pink candies
    pink_candies = 232 - total_candies

    # Display the number of pink candies
    result = pink_candies
    return result

print(solution())