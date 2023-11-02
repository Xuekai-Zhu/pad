def solution():
    
    # Define the initial cost of the boat
    initial_cost = 9000

    # Calculate the value of the boat after the first year
    year1_value = initial_cost * 0.3

    # Calculate the value of the boat after the second year
    year2_value = year1_value * 0.3

    # Calculate the value of the boat after the third year
    year3_value = year2_value * 0.2

    # Calculate the total value of the boat after three years
    total_value = initial_cost + year1_value + year2_value + year3_value

    # return the result
    result = total_value
    return result

print(solution())