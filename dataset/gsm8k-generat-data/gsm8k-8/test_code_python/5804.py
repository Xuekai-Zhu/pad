def solution():
    # Calculate the number of electropop requests
    electropop_requests = 0.5 * 30

    # Calculate the number of dance music requests
    dance_requests = (1/3) * electropop_requests

    # Calculate the number of rock music requests
    rock_requests = 5

    # Calculate the number of oldies requests
    oldies_requests = rock_requests - 3

    # Calculate the number of times Ziggy plays an oldie
    oldies_plays = 0.5 * oldies_requests

    # Calculate the number of rap song requests
    rap_requests = 30 - electropop_requests - dance_requests - rock_requests - oldies_requests

    result = rap_requests
    return result

print(solution())