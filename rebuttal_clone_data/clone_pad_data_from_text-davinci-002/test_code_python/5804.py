def solution():
    total_requests = 30
    electropop_requests = total_requests / 2
    dance_requests = electropop_requests / 3
    rock_requests = 5
    oldies_requests = rock_requests - 3
    rap_requests = oldies_requests / 2
    result = rap_requests
    return result

print(solution())