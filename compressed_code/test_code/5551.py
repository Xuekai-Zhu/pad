def solution():
    
    candy_bar_cost = 0.5
    trash_payment = 0.75
    total_candy_bars = 0
    for i in range(4):
        total_candy_bars += int(trash_payment / candy_bar_cost)
        trash_payment = (trash_payment % candy_bar_cost) + 0.75

    result = total_candy_bars
    return result

print(solution())