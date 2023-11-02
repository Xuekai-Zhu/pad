def solution():
    """Olaf is sailing across the ocean with 25 men, including himself. He needs 1/2 a gallon of water per day per man. The boat can go 200 miles per day and he needs to travel 4,000 miles. How many gallons of water does he need?"""
    men = 25
    water_per_day_per_man = 0.5
    water_per_day = men * water_per_day_per_man
    distance_per_day = 200
    total_distance = 4000
    days = total_distance / distance_per_day
    total_water = days * water_per_day
    result = total_water
    return result

print(solution())