def solution():
    
    initial_earnings = 28
    spent_on_milkshake = initial_earnings / 7
    remaining = initial_earnings - spent_on_milkshake
    saved = remaining / 2
    lost = remaining - saved - 1
    result = lost
    return result

print(solution())