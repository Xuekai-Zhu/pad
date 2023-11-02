def solution():
    total_apples = 40 / 0.5
    percent_sweet = 75
    sweet_apples = total_apples * (percent_sweet/100)
    sour_apples = total_apples - sweet_apples
    result = sweet_apples + sour_apples
    
    return result

print(solution())