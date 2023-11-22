def solution():
    
    # Define the initial amount of money Adam has
    initial_money = 100

    # Define the cost of each rock and the selling price of each rock
    rock_cost = 5
    rock_price = 7

    # Calculate the total cost of buying the rocks
    total_cost = rock_cost * rock_count

    # Calculate the total revenue from selling the rocks
    total_revenue = rock_price * rock_count * 0.6

    # Calculate the profit from investment
    profit = total_revenue - total_cost

    # Calculate the loss
    loss = initial_money - profit

    # return the result
    result = loss
    return result

print(solution())