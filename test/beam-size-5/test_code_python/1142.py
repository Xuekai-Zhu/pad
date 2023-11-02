def solution():
    
    # Define the initial amount of money Adam has
    initial_money = 100

    # Define the cost and selling price of rocks
    rock_cost = 5
    rock_price = 7

    # Calculate the total cost of buying rocks
    total_rock_cost = rock_cost * rock_price

    # Calculate the total revenue from selling rocks
    rock_revenue = rock_cost * rock_price

    # Calculate the amount of money Adam sells
    rock_sell = rock_revenue * 0.6

    # Calculate the amount of money Adam loses
    lost_money = initial_money - rock_sell - rock_sell

    # Display the amount of money Adam loses
    result = lost_money
    return result

print(solution())