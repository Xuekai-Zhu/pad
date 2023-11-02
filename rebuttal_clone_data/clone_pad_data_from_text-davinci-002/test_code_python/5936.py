def solution():
    flour_needed = 100
    harris_flour = 400
    total_flour = harris_flour + traci_flour
    traci_flour = total_flour - harris_flour
    result = traci_flour
    return result

print(solution())