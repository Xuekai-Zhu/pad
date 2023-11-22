def solution():
    
    # Define the number of white carnations ordered
    white_carnations = 200 / 5

    # Calculate the number of red roses ordered
    red_roses = 4 * white_carnations

    # Calculate the number of red roses delivered by 5 pm
    delivered_red_roses = red_roses - 5

    # Display the number of red roses delivered by 5 pm
    result = delivered_red_roses
    return result

print(solution())