def solution():
    distance_per_day = 10 + 12  # Alice walks 10 miles through a grass field and 12 miles through a forest each day
    number_of_days = 5  # Alice walks to school Monday to Friday
    total_distance = distance_per_day * number_of_days  # Alice walks the same distance each day, so multiply by number of days
    result = total_distance
    return result

print(solution())