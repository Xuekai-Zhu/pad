def solution():
    deposit = 0.10  # 10% deposit
    last_year_cost = 250  # cost of last year's costume
    increase_percent = 40  # 40% increase in cost from last year
    total_cost = last_year_cost * (1 + increase_percent/100)  # total cost of the costume
    remaining_payment = total_cost - (deposit * total_cost)  # amount paid on pick up
    result = remaining_payment
    return result

print(solution())