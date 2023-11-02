def solution():
    
    giraffe_jade = 120
    elephant_jade = 2 * giraffe_jade
    giraffe_profit = 150
    elephant_profit = 350
    total_jade = 1920

    
    max_giraffes = total_jade // giraffe_jade

    
    max_elephants = total_jade // elephant_jade

    
    giraffe_profits = max_giraffes * giraffe_profit
    elephant_profits = max_elephants * elephant_profit

    
    profit_difference = elephant_profits - giraffe_profits

    result = profit_difference
    return result

print(solution())