def solution():
    peter_miles_per_day = 3
    andrew_miles_per_day = 2
    days = 5
    peter_total_miles = peter_miles_per_day * days
    andrew_total_miles = andrew_miles_per_day * days
    total_miles = peter_total_miles + andrew_total_miles
    result = total_miles
    return result

print(solution())