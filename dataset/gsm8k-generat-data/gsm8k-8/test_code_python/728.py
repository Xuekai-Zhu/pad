def solution():
    # Define the cost of each item and the amount of each item purchased
    poster_cost = 5
    notebook_cost = 4
    bookmark_cost = 2
    poster_amount = 2
    notebook_amount = 3
    bookmark_amount = 2

    # Calculate the total cost of the purchase
    total_cost = poster_cost * poster_amount + notebook_cost * notebook_amount + bookmark_cost * bookmark_amount

    # Calculate the amount of money Whitney will have left over
    leftover_money = 2 * 20 - total_cost
    result = leftover_money
    return result

print(solution())