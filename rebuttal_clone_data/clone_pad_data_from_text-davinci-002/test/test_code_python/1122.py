def solution():
    rate_georgia = 5
    rate_robert = rate_georgia * 2
    time = 20
    total_coughs_georgia = rate_georgia * time
    total_coughs_robert = rate_robert * time
    total_coughs = total_coughs_georgia + total_coughs_robert
    result = total_coughs
    
    return result

print(solution())