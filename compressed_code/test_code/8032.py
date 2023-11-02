def solution():
    
    adam_magnets = 18
    adam_gave_away = adam_magnets // 3
    peter_magnets = (adam_magnets - adam_gave_away) * 2
    result = peter_magnets
    return result

print(solution())