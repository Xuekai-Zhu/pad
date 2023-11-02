def solution():
    broccoli_price = 4
    num_broccoli_pounds = 3

    orange_price = 0.75
    num_oranges = 3

    cabbage_price = 3.75

    bacon_price = 3
    num_bacon_pounds = 1

    chicken_price = 3
    num_chicken_pounds = 2

    total_spent = (broccoli_price * num_broccoli_pounds) + (orange_price * num_oranges) + \
                  cabbage_price + (bacon_price * num_bacon_pounds) + (chicken_price * num_chicken_pounds)

    meat_spending = (bacon_price * num_bacon_pounds) + (chicken_price * num_chicken_pounds)

    percent_meat_spending = round((meat_spending / total_spent) * 100)

    result = percent_meat_spending
    return result

print(solution())