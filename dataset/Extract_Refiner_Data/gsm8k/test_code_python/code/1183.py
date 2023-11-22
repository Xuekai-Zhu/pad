def solution():
    
    snowballs_per_hour = 20
    melt_per_snowball = 2
    snowballs_available = 60
    snowballs_built_per_hour = snowballs_per_hour * melt_per_snowball / 15
    time_to_build = snowballs_available / snowballs_built_per_hour
    result = time_to_build
    return result

print(solution())