def solution():
    """Michael bought 6 crates of egg on Tuesday. He gave out 2 crates to Susan, who he admires and bought another 5 crates on Thursday. If one crate holds 30 eggs, how many eggs does he have now?"""
    total_eggs = 6 * 30
    eggs_given_away = 2 * 30
    eggs_bought = 5 * 30
    net_eggs = total_eggs - eggs_given_away + eggs_bought
    result = net_eggs
    return result

print(solution())