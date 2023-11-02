def solution():
    curtain_price = 30.00
    num_curtains = 2
    wall_print_price = 15.00
    num_wall_prints = 9
    installation_cost = 50.00

    # Calculate the total cost of the curtains
    total_curtain_cost = curtain_price * num_curtains

    # Calculate the total cost of the wall prints
    total_wall_print_cost = wall_print_price * num_wall_prints

    # Calculate the total cost of the order without installation
    total_order_cost = total_curtain_cost + total_wall_print_cost

    # Add the installation cost to the total order cost
    total_order_cost += installation_cost

    result = total_order_cost
    return result

print(solution())