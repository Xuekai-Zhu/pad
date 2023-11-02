def solution():
    Javier_meat = 5 * 1.5
    Javier_pumpkin = 2 * 1.25
    Javier_cheese = 4
    Javier_total = Javier_meat + Javier_pumpkin + Javier_cheese
    
    brother_pumpkin = 12
    brother_total = brother_pumpkin
    
    winner = max(Javier_total, brother_total)
    result = winner
    
    return result

print(solution())