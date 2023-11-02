def solution():
    giraffe_jade = 120
    giraffe_price = 150
    elephant_jade = giraffe_jade * 2
    elephant_price = 350
    jade_available = 1920
    giraffe_profit = (jade_available / giraffe_jade) * giraffe_price
    elephant_profit = (jade_available / elephant_jade) * elephant_price
    profit_difference = elephant_profit - giraffe_profit
    result = profit_difference
    return result

print(solution())