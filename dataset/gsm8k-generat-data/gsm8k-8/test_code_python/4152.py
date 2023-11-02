def solution():
    # Calculate the total cost of the first coat over 30 years
    coat1_total_cost = 300 + (300/15)*15*2

    # Calculate the total cost of the second coat over 30 years
    coat2_total_cost = 120*6

    # Calculate the amount saved by choosing the more expensive coat
    saved_amount = coat2_total_cost - coat1_total_cost

    result = saved_amount
    return result

print(solution())