def solution():
    senator_term = 10
    supreme_court_term = 16
    if supreme_court_term > senator_term:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())