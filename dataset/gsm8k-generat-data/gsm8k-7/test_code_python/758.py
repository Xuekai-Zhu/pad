def solution():
    flour_cost = 5
    stand_cost = 28
    cash_paid = 2 * 20 + 3
    total_cost = flour_cost + stand_cost

    # Calculate the total change that Faith will receive
    change = cash_paid - total_cost
    result = change
    return result

print(solution())