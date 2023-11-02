def solution():
    
    total_parents = 800
    agree_percent = 20
    disagree_percent = 100 - agree_percent
    disagree_num = (disagree_percent / 100) * total_parents
    result = disagree_num
    return result

print(solution())