def solution():
    
    # Define the value of a quarter and a dime in cents
    quarter_value = 25
    dime_value = 10

    # Calculate the total value of Kelly's pop
    total_pop_value = (5 * quarter_value) + (2 * dime_value)

    # Calculate the amount of pop left after buying a can of pop for 55 cents
    pop_left = total_pop_value - 55

    # Display the amount of pop left
    result = pop_left
    return result

print(solution())