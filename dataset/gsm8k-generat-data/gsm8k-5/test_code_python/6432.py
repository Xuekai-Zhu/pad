def solution():
    marco_start = 24  # Marco starts with $24
    mary_start = 15  # Mary starts with $15

    # Marco gives Mary half of what he has
    marco_gives = marco_start / 2
    mary_new = mary_start + marco_gives

    # Mary spends $5
    mary_spends = 5
    mary_final = mary_new - mary_spends
    
    # Calculate how much more money Mary has than Marco
    difference = mary_final - marco_start
    result = difference
    return result

print(solution())