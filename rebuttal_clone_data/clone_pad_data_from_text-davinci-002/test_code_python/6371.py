def solution():
    cost_of_register = 1040
    loaves_of_bread = 40
    price_of_bread = 2
    cakes = 6
    price_of_cakes = 12
    rent = 20
    electricity = 2
    daily_profit = ((loaves_of_bread * price_of_bread) + (cakes * price_of_cakes)) - (rent + electricity)
    number_of_days = cost_of_register / daily_profit
    result = number_of_days
    return result

print(solution())