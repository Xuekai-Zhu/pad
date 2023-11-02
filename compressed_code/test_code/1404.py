def solution():
    
    initial_doves = 20
    eggs_laid = initial_doves * 3
    hatch_rate = 0.75
    total_doves = initial_doves + (eggs_laid * hatch_rate)
    result = total_doves
    return result

print(solution())