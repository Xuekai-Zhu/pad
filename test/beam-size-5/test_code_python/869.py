def solution():
    
    # Define the initial amount of money David has
    initial_money = 12.48

    # Define the number of bolts David wants to buy
    bolts_needed = 16

    # Define the cost of each bolt
    bolt_cost = 0.03

    # Calculate the total cost of the bolts
    total_cost = bolts_needed * bolt_cost

    # Calculate the amount of money David has left
    money_left = initial_money - total_cost

    # Display the amount of money David has left
    result = money_left
    return result

print(solution())