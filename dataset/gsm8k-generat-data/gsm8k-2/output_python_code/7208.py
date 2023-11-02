def solution():
    """The price of candy bars is twice the cost of caramel, and the cost of cotton candy is half the price of 4 candy bars.
    If the price of 1 caramel is $3, how much do 6 candy bars, 3 caramel, and 1 cotton candy cost together?"""
    caramel_cost = 3
    candy_bar_price = 2 * caramel_cost
    cotton_candy_price = 0.5 * (4 * candy_bar_price)
    total_cost = (6 * candy_bar_price) + (3 * caramel_cost) + cotton_candy_price
    result = total_cost
    return result

print(solution())