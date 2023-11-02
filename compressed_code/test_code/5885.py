def solution():
    
    cat1_frequency = 3
    cat2_frequency = cat1_frequency * 2
    cat3_frequency = cat2_frequency / 3
    total_meows = (cat1_frequency + cat2_frequency + cat3_frequency) * 5
    result = total_meows
    return result

print(solution())