def solution():
    """Every time Carl earned $0.50 he would go to the corner market and buy a candy bar. Carl's neighbor said he would pay him $0.75 every week for taking out his trash. At the end of four weeks, how many candy bars will Carl be able to buy?"""
    candy_cost = 0.5
    trash_payment = 0.75
    weeks = 4
    earnings = candy_cost * weeks * 7 + trash_payment * weeks
    candy_bars = earnings / candy_cost
    result = candy_bars
    
    return result

print(solution())