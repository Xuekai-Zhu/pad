def solution():
    
    # Define the number of twenties and quarters
    twenties = 10
    quarters = 140

    # Calculate the total amount spent on quarters
    quarters_cost = quarters * 0.75

    # Calculate the total amount spent on twenties
    twenties_cost = twenties * 0.6

    # Calculate the total amount spent on all the quarters
    total_quarters_cost = quarters_cost

    # Calculate the total amount spent for the lunch
    total_cost = twenties_cost + total_quarters_cost

    # return the result
    result = total_cost
    return result

print(solution())