def solution():
    # Calculate the amount of money Carrie can make by selling tomatoes
    money_from_tomatoes = 200 * 1  # Carrie can sell a tomato for $1

    # Calculate the amount of money Carrie can make by selling carrots
    money_from_carrots = 350 * 1.5  # Carrie can sell a carrot for $1.50

    # Calculate the total amount of money Carrie can make by selling all of her tomatoes and carrots
    total_money = money_from_tomatoes + money_from_carrots
    result = total_money
    return result

print(solution())