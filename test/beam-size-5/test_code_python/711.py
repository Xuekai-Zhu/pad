def solution():
    
    # Define the initial price of each computer and the percentage increase
    initial_price = 700
    percentage_increase = 10

    # Calculate the new price of each computer
    new_price = initial_price * (1 + percentage_increase/100)

    # Calculate the total cost of buying 500 computers at the new prices
    total_cost = 500 * new_price

    # Display the total cost
    result = total_cost
    return result

print(solution())