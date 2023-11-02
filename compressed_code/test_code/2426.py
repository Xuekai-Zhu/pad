def solution():
    
    initial_passengers = 124
    texas_off = 58
    texas_on = 24
    nc_off = 47
    nc_on = 14
    crew_members = 10
    total_passengers = initial_passengers - texas_off + texas_on - nc_off + nc_on + crew_members
    result = total_passengers
    return result

print(solution())