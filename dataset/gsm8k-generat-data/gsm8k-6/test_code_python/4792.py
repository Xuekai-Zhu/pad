def solution():
    monday_pots = 12  
    tuesday_pots = monday_pots * 2  # twice as many as Monday
    wednesday_pots = 50 - monday_pots - tuesday_pots  # remaining pots after Monday and Tuesday
    result = wednesday_pots
    return result

print(solution())