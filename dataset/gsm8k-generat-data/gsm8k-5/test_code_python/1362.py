def solution():
    initial_gumballs = [40, 60]  # Joanna had 40 gumballs and Jacques had 60 gumballs
    purchased_gumballs = [4 * x for x in initial_gumballs]  # They purchased 4 times the number of gumballs they initially had
    total_gumballs = sum(initial_gumballs) + sum(purchased_gumballs)  # They added the purchased gumballs to their dishes and have a total of gumballs now
    
    # They decided to put together their gumballs and share them equally
    each_gets = total_gumballs // 2  # Divide the total number of gumballs by 2 since they are sharing equally
    
    result = each_gets
    return result

print(solution())