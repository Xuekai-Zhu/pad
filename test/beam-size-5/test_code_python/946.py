def solution():
    
    total_points = 45
    azibo_points = (total_points - 20) / 3
    bahati_points = azibo_points + 20
    dinar_points = dinar_points + 10
    azibo_points = azibo_points - bahati_points
    result = azibo_points
    return result

print(solution())