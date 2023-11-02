def solution():
    """Olaf is sailing across the ocean with 25 men, including himself. He needs 1/2 a gallon of water per day per man. The boat can go 200 miles per day and he needs to travel 4,000 miles. How many gallons of water does he need?"""
    # Calculate the total number of days needed to travel 4,000 miles
    total_days = 4000 // 200

    # Calculate the total amount of water needed for 1 day for 25 men
    water_per_day = 0.5 * 25

    # Calculate the total amount of water needed for the entire trip
    total_water = total_days * water_per_day

    # Display the total amount of water needed
    result = total_water
    return result

print(solution())