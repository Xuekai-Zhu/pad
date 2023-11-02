def solution():
    # Calculate the original number of hours Jim reads per week and the number of pages he reads per hour
    original_hours = 600 / 40
    original_rate = 40

    # Calculate the new number of hours Jim reads per week
    new_hours = original_hours - 4

    # Calculate the new reading rate in pages per hour
    new_rate = original_rate * 1.5

    # Calculate the total number of pages Jim reads per week with the new reading rate and hours
    new_pages = new_rate * new_hours

    result = new_pages
    return result

print(solution())