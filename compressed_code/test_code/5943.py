def solution():
    
    lions_after_1_year = 148
    birth_rate = 5
    death_rate = 1
    months_in_a_year = 12
    lions_at_first = lions_after_1_year - ((birth_rate - death_rate) * months_in_a_year)
    result = lions_at_first
    return result

print(solution())