def solution():
    diamond_earrings_cost = 6000
    num_diamond_earrings = 2

    iphone_cost = 2000

    scarf_price = 1500

    total_value = 20000

    # Calculate the total cost of the diamond earrings
    total_earrings_cost = diamond_earrings_cost * num_diamond_earrings

    # Calculate the total cost of all other items except the scarves
    total_cost_without_scarves = total_value - total_earrings_cost - iphone_cost

    # Calculate the number of scarves
    num_scarves = total_cost_without_scarves // scarf_price
    result = num_scarves
    return result

print(solution())