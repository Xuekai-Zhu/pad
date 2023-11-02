def solution():
    
    total_rhinestones = 45
    bought_rhinestones = total_rhinestones / 3
    found_rhinestones = total_rhinestones / 5
    still_need = total_rhinestones - bought_rhinestones - found_rhinestones
    result = still_need
    return result

print(solution())