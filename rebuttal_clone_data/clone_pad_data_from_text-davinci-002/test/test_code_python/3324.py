def solution():
    total_apples = 200
    rotten_apples = total_apples * 0.4
    rotten_apples_that_smelled = rotten_apples * 0.7
    rotten_apples_that_didnt_smell = rotten_apples - rotten_apples_that_smelled
    result = rotten_apples_that_didnt_smell
    return result

print(solution())