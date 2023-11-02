def solution():
    # Calculate the total toilet paper production in March 2020
    increased_production = 3 * 7000  # the company ramped up its production three times more
    total_production = (31-1) * increased_production  # assuming March has 31 days and production only increased from 2nd to 31st March
    result = total_production
    return result

print(solution())