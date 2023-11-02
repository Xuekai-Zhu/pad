def solution():
    # Define the number of red candies
    red_candies = 40
    
    # Calculate the number of yellow candies
    yellow_candies = 3 * red_candies - 20
    
    # Calculate the number of blue candies
    blue_candies = yellow_candies / 2
    
    # Calculate the total number of candies
    total_candies = red_candies + yellow_candies + blue_candies
    
    # Subtract the number of yellow candies (which Carlos ate) from the total
    remaining_candies = total_candies - yellow_candies
    
    result = remaining_candies
    return result

print(solution())