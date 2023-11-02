def solution():
    money_received = 100  # John received $100 from his uncle
    money_given_away = money_received / 4  # John gave away 1/4 of the money to his sister
    money_spent = 40  # John spent $40 on groceries

    # Calculate the money remaining with John
    money_remaining = money_received - money_given_away - money_spent
    result = money_remaining
    return result

print(solution())