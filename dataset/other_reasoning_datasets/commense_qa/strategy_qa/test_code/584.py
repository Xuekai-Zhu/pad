def solution():
    supreme_court_seats = 9
    uk_prime_ministers_since_1952 = 15
    if supreme_court_seats >= uk_prime_ministers_since_1952:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())