def solution():
    total_money = 40 * 4  # Leila spent 1/4 of her money on a sweater, so she had 3/4 left
    sweater_cost = 40
    jewelry_cost = total_money - sweater_cost - 20  # Leila spent $20 on jewelry after buying the sweater
    difference = jewelry_cost - sweater_cost
    result = difference
    return result

print(solution())