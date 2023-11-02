def solution():
    """When doing her exercises, Mairead runs for 40 miles, walks for 3/5 times as many miles as she ran, and walks for five times the number of miles she jogged. Calculate the total distance Mairead has covered while doing her exercises."""
    
    miles_ran = 40
    miles_walked = (3/5) * miles_ran
    miles_jogged = miles_walked/5
    
    total_distance = miles_ran + miles_walked + miles_jogged
    result = total_distance
    return result

print(solution())