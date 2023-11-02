def solution():
    """Nancy carves statues out of jade. A giraffe statue takes 120 grams of jade and sells for $150. An elephant statue takes twice as much jade and sells for $350. If Nancy has 1920 grams of jade, how much more money will she make turning it all into elephants instead of giraffes?"""
    giraffe_jade = 120
    elephant_jade = 2 * giraffe_jade
    giraffe_profit = 150
    elephant_profit = 350
    total_jade = 1920

    # Find the maximum number of giraffes Nancy can make with her jade
    max_giraffes = total_jade // giraffe_jade

    # Find the maximum number of elephants Nancy can make with her jade
    max_elephants = total_jade // elephant_jade

    # Calculate the profits for each scenario
    giraffe_profits = max_giraffes * giraffe_profit
    elephant_profits = max_elephants * elephant_profit

    # Calculate the difference in profits
    profit_difference = elephant_profits - giraffe_profits

    result = profit_difference
    return result

print(solution())