def solution():
    # Calculate the number of hours Mark reads per day after increasing by 150%
    new_hours = 2 * 2.5  # 150% increase means 2.5 times the original number of hours

    # Calculate the number of pages Mark reads per day now
    new_pages = 100 * new_hours

    # Calculate the number of pages Mark reads per week
    pages_per_week = new_pages * 7
    result = pages_per_week
    return result

print(solution())