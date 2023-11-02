def solution():
    apple_price = 2
    emmy_money = 200
    gerry_money = 100

    # Calculate the number of apples Emmy can buy
    num_emmy_apples = emmy_money // apple_price

    # Calculate the number of apples Gerry can buy
    num_gerry_apples = gerry_money // apple_price

    # Calculate the total number of apples they can buy together
    total_apples = num_emmy_apples + num_gerry_apples
    result = total_apples
    return result

print(solution())