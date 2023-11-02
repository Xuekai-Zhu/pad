def solution():
    # Define the years of the baby boom and the Cuban Revolution
    baby_boom_years = range(1946, 1964)
    cuban_revolution_years = range(1953, 1959)
    # Check if there is any overlap between the two time periods
    overlap = set(baby_boom_years).intersection(cuban_revolution_years)
    if overlap:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())