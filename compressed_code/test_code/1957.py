def solution():
    
    total_playtime = 100
    grinding_time = total_playtime * 0.8
    expansion_time = 30
    enjoyable_time = total_playtime - grinding_time + expansion_time
    result = enjoyable_time
    return result

print(solution())