def solution():
    
    people_per_cubic_yard = 80
    volume_city1 = 6400
    volume_city2 = 9000
    people_city1 = volume_city1 * people_per_cubic_yard
    people_city2 = volume_city2 * people_per_cubic_yard
    difference = people_city2 - people_city1
    
    return difference

print(solution())