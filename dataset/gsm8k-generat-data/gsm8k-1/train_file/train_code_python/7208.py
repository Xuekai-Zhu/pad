def solution():
    """The price of candy bars is twice the cost of caramel, and the cost of cotton candy is half the price of 4 candy bars. If the price of 1 caramel is $3, how much do 6 candy bars, 3 caramel, and 1 cotton candy cost together?"""
    cost_of_caramel = 3
    price_of_candy_bars = 2 * cost_of_caramel
    price_of_four_candy_bars = 4 * price_of_candy_bars
    price_of_cotton_candy = price_of_four_candy_bars / 2
    total_cost = (6 * price_of_candy_bars) + (3 * cost_of_caramel) + price_of_cotton_candy
    result = total_cost
    
    return result

print(solution())