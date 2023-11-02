def solution():
    
    # Define the initial number of vanilla and fruity scents
    vanilla_scents = 4
    fruity_scents = 8

    # Define the number of vanilla and fruity scents sold by the end of the day
    vanilla_sold = 5
    fruity_sold = 2

    # Calculate the number of vanilla and fruity scents sold
    vanilla_sold = vanilla_scents - vanilla_sold
    fruity_sold = fruity_scents - fruity_sold

    # Calculate the difference between the number of vanilla and fruity scents
    difference = vanilla_sold - fruity_sold

    # Display the difference
    result = difference
    return result

print(solution())