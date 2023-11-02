def solution():
    # Define the price and the amount of money each person has
    apple_price = 2
    emmy_money = 200
    gerry_money = 100

    # Calculate the number of apples each person can buy
    emmy_apples = emmy_money // apple_price
    gerry_apples = gerry_money // apple_price

    # Calculate the total number of apples they can buy together
    total_apples = emmy_apples + gerry_apples
    result = total_apples
    return result

print(solution())