def solution():
    total_money = 90
    hat_percentage = 0.6
    scarf_price = 2

    # Calculate the amount spent on hats
    hat_spending = total_money * hat_percentage
    # Calculate the amount spent on scarves
    scarf_spending = total_money - hat_spending

    # Calculate the number of hats purchased
    num_hats = 2 * num_scarves

    # Calculate the cost of all hats purchased
    hat_cost = hat_spending

    # Calculate the cost of all scarves purchased
    scarf_cost = scarf_spending
    # Calculate the number of scarves that can be bought with the remaining money
    num_scarves = int(scarf_cost / scarf_price)

    result = num_scarves
    return result

print(solution())