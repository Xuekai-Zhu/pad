def solution():
    # Calculate the total amount of money Selina earned from selling her clothes
    total_money_earned = 3 * 5 + 5 * 3 + 4 * shirts_sold

    # Calculate the total cost of the two shirts Selina purchased
    total_shirt_cost = 2 * 10

    # Calculate Selina's profit from selling her clothes and buying the shirts
    profit = 30 - (total_money_earned - total_shirt_cost)

    # Calculate the number of shirts Selina sold to the store
    shirts_sold = profit / 4

    result = shirts_sold
    return result

print(solution())