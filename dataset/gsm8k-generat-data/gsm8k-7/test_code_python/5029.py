def solution():
    num_sweaters = 6
    sweater_price = 30

    num_scarves = 6
    scarf_price = 20

    total_cost = (num_sweaters * sweater_price) + (num_scarves * scarf_price)

    remaining_savings = 500 - total_cost

    result = remaining_savings
    return result

print(solution())