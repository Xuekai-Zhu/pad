def solution():
    # Let's assume the number of vampires as 'v' and the number of werewolves as 'w'
    # Total amount earned = amount earned from vampires + amount earned from werewolves
    # amount earned from vampires = 5 * (1/2) * v = 2.5v
    # amount earned from werewolves = 10 * (w - 8)
    # As per the problem statement, w = 4v
    # So, amount earned from werewolves = 10 * (4v - 8) = 40v - 80
    # Total amount earned = 2.5v + 40v - 80 = 42.5v - 80
    
    # We know that Van Helsing earned $105, so 42.5v - 80 = 105
    # Solving for 'v', we get v = 6
    
    # So, the number of werewolves is w = 4v = 24
    
    # Van Helsing removed 8 werewolves, so the percentage of werewolves he removed is:
    percentage_removed = (8/24) * 100
    result = percentage_removed
    return result

print(solution())