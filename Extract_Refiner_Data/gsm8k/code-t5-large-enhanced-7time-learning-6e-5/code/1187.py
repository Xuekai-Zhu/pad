def solution():
    
    # Define the cost of color and cut
    COLOR_COST = 40
    CUT_COST = 30

    # Define the starting and ending height of the hair
    START_HEIGHT = 10
    END_HEIGHT = 8

    # Calculate the total cost of haircut
    cut_cost = (END_HEIGHT - START_HEIGHT) * CUT_COST

    # Calculate the total cost of cut and color
    total_cost = cut_cost + COLOR_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())