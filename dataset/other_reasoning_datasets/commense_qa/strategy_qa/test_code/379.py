def solution():
    texas_avg_temp = (68 + 89)/2
    frost_temp = 32
    if texas_avg_temp > frost_temp:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())