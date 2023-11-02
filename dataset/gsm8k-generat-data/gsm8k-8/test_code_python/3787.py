def solution():
    # Determine how long it took Jason to go from chief to master chief
    chief_to_masterchief = 1.25 * 8

    # Calculate the total number of years Jason spent in the military
    total_years = 18 + 8 + chief_to_masterchief + 10

    # Determine how old Jason was when he retired
    retirement_age = total_years + 1  # assuming he retired at age 1 year older than his exact number of years in the military

    result = retirement_age
    return result

print(solution())