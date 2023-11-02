def solution():
    """Olaf is sailing across the ocean with 25 men, including himself. He needs 1/2 a gallon of water per day per man. The boat can go 200 miles per day and he needs to travel 4,000 miles. How many gallons of water does he need?"""
    # Define the number of men on the boat and the daily water requirement per man
    men = 25
    water_per_man_per_day = 0.5

    # Calculate the total water requirement for the journey
    total_water_requirement = (men * water_per_man_per_day * 4000) / 200

    # return the result
    result = total_water_requirement
    return result

print(solution())