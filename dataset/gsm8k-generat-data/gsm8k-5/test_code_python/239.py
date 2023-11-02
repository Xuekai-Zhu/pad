def solution():
    # Calculate the total amount of money Frank has
    total_money = (7 * 1) + (4 * 5) + (2 * 10) + (1 * 20)

    # Calculate the amount of money Frank spent on peanuts
    spent_money = total_money - 4  # Frank had $4 in change, so he spent the rest on peanuts

    # Calculate the amount of peanuts Frank bought
    peanuts_bought = spent_money / 3  # Peanuts cost $3 per pound

    # Calculate the average amount of peanuts Frank eats per day
    days_per_week = 7
    average_peanuts_per_day = peanuts_bought / days_per_week

    result = average_peanuts_per_day
    return result

print(solution())