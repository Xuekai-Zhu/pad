def solution():
    
    # Define the number of candies in each bag
    red_candies = 54
    orange_candies = red_candies * 2
    yellow_candies = red_candies / 2

    # Calculate the total number of candies
    total_candies = red_candies + orange_candies + yellow_candies

    # Calculate the number of candies that are pink
    pink_candies = 232 - total_candies

    # Display the number of candies that are pink
    result = pink_candies
    return result

print(solution())