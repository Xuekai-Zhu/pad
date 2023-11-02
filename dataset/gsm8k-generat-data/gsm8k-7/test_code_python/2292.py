def solution():
    feeding_allowance = 4.0
    portion_given = feeding_allowance / 4.0
    candy_cost = 0.20

    # Calculate the amount of money given to Jake's friend
    friend_money = portion_given * feeding_allowance

    # Calculate the number of candies that can be purchased with this money
    num_candies = friend_money / candy_cost
    result = num_candies
    return result

print(solution())