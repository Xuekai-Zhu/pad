def solution():
    candy_bars = 2 * .75
    lollipops = 4 * .25
    spent = 1/6
    total = candy_bars + lollipops
    money_left = total - spent
    driveways_shoveled = money_left / 1.5
    
    return driveways_shoveled

print(solution())