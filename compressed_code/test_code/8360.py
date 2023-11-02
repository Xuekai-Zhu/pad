def solution():
    
    males_orchestra = 11
    females_orchestra = 12
    total_orchestra = males_orchestra + females_orchestra
    total_band = total_orchestra * 2
    males_choir = 12
    females_choir = 17
    total_choir = males_choir + females_choir
    result = total_orchestra + total_band + total_choir
    return result

print(solution())