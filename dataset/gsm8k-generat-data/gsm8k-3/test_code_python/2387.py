def solution():
    """Dirk sells amulets at a Ren Faire. He sells for 2 days and each day he sells 25 amulets.
    Each amulet sells for 40 dollars and they cost him 30 dollars to make.
    If he has to give 10% of his revenue to the faire, how much profit did he make?"""
    # Define the variables and constants
    num_days = 2
    num_amulets_per_day = 25
    sale_price = 40
    cost_per_amulet = 30
    faire_cut = 0.1

    # Calculate the total revenue
    total_amulets_sold = num_days * num_amulets_per_day
    total_revenue = total_amulets_sold * sale_price

    # Calculate the total cost
    total_cost = total_amulets_sold * cost_per_amulet

    # Calculate the faire's cut
    faire_profit = total_revenue * faire_cut

    # Calculate the final profit
    final_profit = total_revenue - total_cost - faire_profit

    # Display the final profit
    result = final_profit
    return result

print(solution())