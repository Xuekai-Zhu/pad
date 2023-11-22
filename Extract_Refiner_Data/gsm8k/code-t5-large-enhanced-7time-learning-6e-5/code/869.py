def solution():
    
    # Define the initial amount of money David has
    initial_money = 12.48

    # Define the number of bolts David wants to buy
    bolts_bought = 16

    # Define the cost of each bolt
    bolt_cost = 0.03

    # Calculate the total cost of the bolts
    total_cost = bolts_bought * bolt_cost

    # Calculate the amount of money David has left after paying for the bolts
    money_left = initial_money - total_cost

    # return the result
    result = money_left
    return result

print(solution())