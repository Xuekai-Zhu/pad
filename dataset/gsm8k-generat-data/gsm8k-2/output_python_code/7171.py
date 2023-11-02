def solution():
    """Every time Carl earned $0.50 he would go to the corner market and buy a candy bar. Carl's neighbor said he would pay him $0.75 every week for taking out his trash. At the end of four weeks, how many candy bars will Carl be able to buy?"""
    candy_bar_cost = 0.5
    trash_payment = 0.75
    total_candy_bars = 0
    for i in range(4):
        total_candy_bars += int(trash_payment / candy_bar_cost)
        trash_payment = (trash_payment % candy_bar_cost) + 0.75

    result = total_candy_bars
    return result

print(solution())