def solution():
    matches_ played= 200
    matches_ won= 100
    percentage_won= 50
    total_won= matches_ played* (percentage_won/100)
    total_won= total_won+ matches_ won
    result= total_won
    return result

print(solution())