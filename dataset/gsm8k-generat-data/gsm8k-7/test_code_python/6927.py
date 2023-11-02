def solution():
    kiddie_scoop_price = 3
    regular_scoop_price = 4
    double_scoop_price = 6

    num_regular_scoops = 2
    num_kiddie_scoops = 2
    num_double_scoops = 3

    # Calculate the cost of all kiddie scoops
    kiddie_scoop_cost = num_kiddie_scoops * kiddie_scoop_price

    # Calculate the cost of all regular scoops
    regular_scoop_cost = num_regular_scoops * regular_scoop_price

    # Calculate the cost of all double scoops
    double_scoop_cost = num_double_scoops * double_scoop_price

    # Calculate the total cost
    total_cost = kiddie_scoop_cost + regular_scoop_cost + double_scoop_cost
    result = total_cost
    return result

print(solution())