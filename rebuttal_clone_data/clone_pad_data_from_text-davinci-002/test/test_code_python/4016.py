def solution():
    percent_decrease_1 = 10
    percent_decrease_2 = 20
    initial_price = 1000
    decreased_price_1 = initial_price * (1 - (percent_decrease_1 / 100))
    decreased_price_2 = decreased_price_1 * (1 - (percent_decrease_2 / 100))
    result = decreased_price_2
    return result

print(solution())