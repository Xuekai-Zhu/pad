def solution():
    num_requests = 30
    num_electropop = num_requests / 2
    num_dance = num_electropop / 3
    num_rock = 5
    num_oldies = num_rock - 3
    num_dj_choice = num_oldies / 2
    
    # Calculate the number of rap song requests by subtracting all other requests from the total
    num_rap = num_requests - num_electropop - num_dance - num_rock - num_oldies - num_dj_choice
    result = num_rap
    return result

print(solution())