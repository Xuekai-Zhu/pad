def solution():
    hamburgers_cost = 4
    milkshakes_cost = 5
    total_cost = (hamburgers_cost * 8) + (milkshakes_cost * 6)
    money_left = 70
    money_at_first = total_cost + money_left
    result = money_at_first
    return result

print(solution())