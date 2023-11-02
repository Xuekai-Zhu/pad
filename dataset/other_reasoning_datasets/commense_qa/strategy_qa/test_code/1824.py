def solution():
    moulin_rouge_capacity = 850
    spanish_war_injured = 750 #assuming an average of 700-800
    if spanish_war_injured <= moulin_rouge_capacity:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())