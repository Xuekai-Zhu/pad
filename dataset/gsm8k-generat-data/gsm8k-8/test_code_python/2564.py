def solution():
    # Calculate the cost of fixing the car with the discount
    cost = 20000 * 0.8

    # Calculate the winnings from the race, after keeping only 90%
    winnings = 70000 * 0.9

    # Calculate the profit from the car
    profit = winnings - cost
    result = profit
    return result

print(solution())