def solution():
    
    total_eggs = 6 * 30
    eggs_given_away = 2 * 30
    eggs_bought = 5 * 30
    net_eggs = total_eggs - eggs_given_away + eggs_bought
    result = net_eggs
    return result

print(solution())