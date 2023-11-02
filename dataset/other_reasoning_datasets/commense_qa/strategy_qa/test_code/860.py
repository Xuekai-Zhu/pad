def solution():
    popular_amendments = ["Fifth", "Fourteenth"]
    eighth_amendment = "Eighth"
    if eighth_amendment in popular_amendments:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())