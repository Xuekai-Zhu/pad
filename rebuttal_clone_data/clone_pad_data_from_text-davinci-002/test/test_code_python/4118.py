def solution():
    superhero_miles = 10
    superhero_minutes = 4
    superhero_time = superhero_minutes / 60
    superhero_speed = superhero_miles / superhero_time
    villain_speed = 100
    difference_in_speed = superhero_speed - villain_speed
    difference_in_distance = difference_in_speed * 1
    result = difference_in_distance
    return result

print(solution())