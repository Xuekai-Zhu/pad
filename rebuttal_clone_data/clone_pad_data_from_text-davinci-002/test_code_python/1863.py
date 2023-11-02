def solution():
    kilometers_from_red_deer_to_edmonton = 220
    kilometers_from_red_deer_to_calgary = 110
    kilometers_per_hour = 110
    total_kilometers = kilometers_from_red_deer_to_edmonton + kilometers_from_red_deer_to_calgary
    hours_traveled = total_kilometers / kilometers_per_hour
    result = hours_traveled
    return result

print(solution())