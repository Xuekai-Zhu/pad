def solution():
    
    # Define the cost of a blue tie and the ratio of red to blue ties
    BLUE_COST = 40
    RED_RATIO = 1.5

    # Calculate the cost of red ties
    red_cost = BLUE_COST * (1 + RED_RATIO)

    # Calculate the total cost of blue ties and red ties
    blue_total = 200
    red_total = red_cost * 2

    # Calculate the total cost of all the ties
    total_cost = blue_total + red_total

    # Display the total cost
    result = total_cost
    return result

print(solution())