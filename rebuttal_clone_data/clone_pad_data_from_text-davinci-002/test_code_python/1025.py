def solution():
    parents = 800
    percent_agree = 20
    parents_agreeing = parents * (percent_agree/100)
    parents_disagreeing = parents - parents_agreeing
    result = parents_disagreeing 
    return result

print(solution())