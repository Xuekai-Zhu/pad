def solution():
    # Calculate the total amount Julie will earn
    lawn_money = 20 * 20
    newspaper_money = 0.40 * 600
    dog_money = 15 * 24
    total_earnings = lawn_money + newspaper_money + dog_money

    # Calculate the total cost of the bike and how much Julie will have left
    bike_cost = 2345
    total_cost = bike_cost - (1500 + total_earnings)
    result = total_cost
    return result

print(solution())