def solution():
    
    # Define the initial number of lego sets and the price per lego set
    initial_sets = 13
    initial_price = 15

    # Define the number of games bought and the remaining budget
    games_bought = 8
    remaining_budget = 5

    # Calculate the total cost of the games
    total_cost = games_bought * 20

    # Calculate the total revenue from selling the lego sets
    total_revenue = initial_sets * initial_price

    # Calculate the number of lego sets remaining
    remaining_sets = initial_sets - total_revenue

    # Calculate the total cost of buying the remaining games
    remaining_cost = remaining_sets * remaining_budget

    # Calculate the total number of lego sets
    total_sets_remaining = remaining_sets + total_cost

    # return the result
    result = total_sets_remaining
    return result

print(solution())