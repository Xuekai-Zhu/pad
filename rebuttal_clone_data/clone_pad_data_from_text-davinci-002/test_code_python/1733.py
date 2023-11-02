def solution():
    
    pairs_of_pants = 4
    jumpers = 4
    sets_of_pajamas = 4
    t_shirts = 20
    friends = 3
    
    total_clothing = pairs_of_pants + jumpers + sets_of_pajamas + t_shirts
    total_donated = total_clothing + (total_clothing * friends)
    total_after_keep = total_donated / 2
    result = total_after_keep
    
    return result

print(solution())