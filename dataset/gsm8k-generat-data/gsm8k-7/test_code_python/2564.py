def solution():
    cost = 20000
    discount_percent = 0.2
    discount_amount = cost * discount_percent
    discounted_cost = cost - discount_amount
    prize_money = 70000
    kept_percent = 0.9

    # Calculate the total cost of fixing the car after the discount
    total_cost = discounted_cost

    # Calculate the amount of money John kept from winning the race
    kept_money = prize_money * kept_percent

    # Calculate John's profit from the car
    profit = kept_money - total_cost
    result = profit
    return result

print(solution())