def solution():
    feeding_allowance = 4  # Jake's feeding allowance is $4
    portion_given = feeding_allowance / 4  # Jake gave one-quarter of his feeding allowance

    # Calculate the amount of money Jake's friend received
    friend_money = feeding_allowance * portion_given

    # Calculate the number of candies his friend can purchase
    candies = friend_money / 0.20  # Each candy costs 20 cents

    result = candies
    return result

print(solution())