def solution():
    initial_money = 30
    ride_spending = initial_money / 2
    dessert_spending = 5

    # Calculate the total amount of money spent
    total_spending = ride_spending + dessert_spending

    # Calculate the amount of money left
    money_left = initial_money - total_spending
    result = money_left
    return result

print(solution())