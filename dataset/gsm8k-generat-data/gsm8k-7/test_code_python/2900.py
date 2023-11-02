def solution():
    money_left = 55  # dollars
    hot_dog_cost = 2

    # Calculate the money James spent on giving back to the charity and the hot dog
    money_spent = hot_dog_cost + (money_left / 2)

    # Calculate the total money James won
    total_money = money_spent * 2
    result = total_money
    return result

print(solution())