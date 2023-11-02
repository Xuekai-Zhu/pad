def solution():
    
    total_apples = 200
    rotten_percent = 0.4
    rotten_apples = total_apples * rotten_percent
    smelled_percent = 0.7
    smelled_apples = rotten_apples * smelled_percent
    not_smelled_apples = rotten_apples - smelled_apples
    result = not_smelled_apples
    return result

print(solution())