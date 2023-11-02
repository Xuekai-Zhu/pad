def solution():
    
    total_deer = 920
    eight_antlers_percent = 10
    eight_antlers_deer = total_deer * (eight_antlers_percent / 100)
    albino_percent = 25
    albino_eight_antlers = eight_antlers_deer * (albino_percent / 100)
    result = albino_eight_antlers
    return result

print(solution())