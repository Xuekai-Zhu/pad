def solution():
    
    budget = 300
    cost_per_rose = 2
    total_roses = budget // cost_per_rose
    jenna_roses = total_roses // 3
    imma_roses = total_roses // 2
    hanna_gives = jenna_roses + imma_roses
    result = hanna_gives
    return result

print(solution())