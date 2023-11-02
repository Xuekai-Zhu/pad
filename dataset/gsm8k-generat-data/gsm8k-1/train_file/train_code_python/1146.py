def solution():
    """In a city, the number of people living per cubic yard is 80. How many more people are in a city with 9000 cubic yards than a city with 6400 cubic yards?"""
    people_per_cubic_yard = 80
    volume_city1 = 6400
    volume_city2 = 9000
    people_city1 = volume_city1 * people_per_cubic_yard
    people_city2 = volume_city2 * people_per_cubic_yard
    difference = people_city2 - people_city1
    
    return difference

print(solution())