def solution():
    
    # Define the initial cost of the boat
    initial_cost = 9000

    # Calculate the cost after the first year
    first_year_cost = initial_cost * 0.7

    # Calculate the cost after the second year
    second_year_cost = first_year_cost * 0.7

    # Calculate the cost after the third year
    third_year_cost = second_year_cost * 0.2

    # Calculate the total cost after three years
    total_cost = first_year_cost + second_year_cost + third_year_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())