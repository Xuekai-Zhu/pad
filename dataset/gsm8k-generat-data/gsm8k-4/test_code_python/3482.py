def solution():
    """Cersei bought 50 cotton candies. She gave her brother and sister 5 cotton candies each, then gave the remaining one-fourth of them to her cousin. If she ate 12 cotton candies, how many cotton candies are left?"""
    # Define the initial number of cotton candies
    initial_candies = 50
    
    # Calculate the number of cotton candies given to Cersei's brother and sister
    brother_sister_candies = 5 + 5
    
    # Calculate the number of cotton candies remaining
    remaining_candies = initial_candies - brother_sister_candies
    
    # Calculate the number of cotton candies given to Cersei's cousin
    cousin_candies = remaining_candies / 4
    
    # Calculate the number of cotton candies left after Cersei ate 12
    candies_left = initial_candies - (brother_sister_candies + cousin_candies + 12)
    
    # Return the result
    result = candies_left
    return result

print(solution())