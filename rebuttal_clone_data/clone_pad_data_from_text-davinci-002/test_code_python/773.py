def solution():
    total_miles = 369
    miles_driven1 = 42
    hours_driven1 = 3
    miles_driven2 = 61
    hours_driven2 = 2
    miles_remaining = total_miles - (miles_driven1 * hours_driven1 + miles_driven2 * hours_driven2)
    result =  miles_remaining
    return result

print(solution())