def solution():
    
    initial_passengers = 124
    passengers_off_in_Texas = 58
    passengers_on_in_Texas = 24
    passengers_off_in_NC = 47
    passengers_on_in_NC = 14
    crew_members = 10
    total_passengers = initial_passengers - passengers_off_in_Texas + passengers_on_in_Texas - passengers_off_in_NC + passengers_on_in_NC + crew_members
    result = total_passengers
    return result

print(solution())