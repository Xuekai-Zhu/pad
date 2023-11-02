def solution():
    """Olaf is sailing across the ocean with 25 men, including himself. He needs 1/2 a gallon of water per day per man. The boat can go 200 miles per day and he needs to travel 4,000 miles. How many gallons of water does he need?"""
    num_men = 25
    water_per_man_per_day = 0.5
    num_days = 4000 / 200
    total_water_needed = num_men * water_per_man_per_day * num_days
    result = total_water_needed
    return result

print(solution())