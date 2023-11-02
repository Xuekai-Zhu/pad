def solution():
    """Lily has 5 lottery tickets to sell.  She sells the first ticket for $1.  She then sells each successive ticket for a dollar more than the previous ticket. She plans to keep a $4 profit and give the remaining money as the prize. How much money will the winner of the lottery receive?"""
    # Define the starting price and profit
    starting_price = 1
    profit = 4

    # Calculate the total cost of all the tickets
    total_cost = starting_price + (starting_price + 1) + (starting_price + 2) + (starting_price + 3) + (starting_price + 4)
    
    # Calculate the total revenue from selling the tickets
    total_revenue = total_cost + profit

    # Calculate the prize money
    prize_money = total_revenue - starting_price

    # Display the prize money
    result = prize_money
    return result

print(solution())