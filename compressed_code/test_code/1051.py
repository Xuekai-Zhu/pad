def solution():
    
    joanna_gumballs = 40
    jacques_gumballs = 60
    total_gumballs = joanna_gumballs + jacques_gumballs
    new_gumballs = 4 * total_gumballs
    total_gumballs_with_new = total_gumballs + new_gumballs
    each_gets = total_gumballs_with_new // 2
    result = each_gets
    return result

print(solution())