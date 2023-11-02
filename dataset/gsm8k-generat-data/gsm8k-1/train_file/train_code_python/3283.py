def solution():
    """Antonella has ten Canadian coins in her purse that are either loonies or toonies. A loonie equals $1 and a toonie equals $2. If she bought a $3 Frappuccino and still has $11, how many toonies did she initially have?"""
    total_coins = 10
    frappuccino_cost = 3
    remaining_cash = 11
    loonie_value = 1
    toonie_value = 2
    
    # Set up equation system to solve for number of loonies and toonies
    # l + t = total_coins
    # l * loonie_value + t * toonie_value = remaining_cash + frappuccino_cost
    
    # Solving for toonies
    # t = (remaining_cash + frappuccino_cost - l * loonie_value) / toonie_value
    for l in range(total_coins+1):
        t = (remaining_cash + frappuccino_cost - l * loonie_value) / toonie_value
        if t.is_integer() and t >= 0 and t <= total_coins:
            result = int(t)
            break
    
    return result

print(solution())