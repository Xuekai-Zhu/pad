def solution():
    
    total_requests = 30
    electropop_requests = total_requests / 2
    dance_requests = electropop_requests / 3
    rock_requests = 5
    oldies_requests = rock_requests - 3
    dj_choice_requests = oldies_requests / 2
    rap_requests = total_requests - (electropop_requests + dance_requests + rock_requests + oldies_requests + dj_choice_requests)
    result = rap_requests
    return result

print(solution())