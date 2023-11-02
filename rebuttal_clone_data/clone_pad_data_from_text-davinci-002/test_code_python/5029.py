def solution():
    sweater_price = 30
    scarf_price = 20
    number_of_sweaters = 6
    number_of_scarves = 6
    total_cost = (sweater_price * number_of_sweaters) + (scarf_price * number_of_scarves)
    initial_savings = 500
    final_savings = initial_savings - total_cost
    result = final_savings
    return result

print(solution())