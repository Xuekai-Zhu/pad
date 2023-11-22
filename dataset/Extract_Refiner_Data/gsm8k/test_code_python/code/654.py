def solution():
    
    rice_time = 30
    pork_time = rice_time + 20
    beans_time = (rice_time + pork_time) / 2
    total_time = rice_time + pork_time + beans_time
    result = total_time
    return result

print(solution())