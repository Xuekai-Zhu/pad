def solution():
    # Calculate the cost of the racecar after the discount
    cost_after_discount = 20000 - (0.2 * 20000)

    # Calculate the money John keeps after winning the race
    money_kept = 0.9 * 70000

    # Calculate the profit John made from the car
    profit = money_kept - cost_after_discount
    result = profit
    return result

print(solution())