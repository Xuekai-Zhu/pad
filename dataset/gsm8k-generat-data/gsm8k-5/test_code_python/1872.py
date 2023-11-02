def solution():
    birds = 20  # There are 20 birds migrating
    distance_Jim_to_Disney = 50  # Distance between lake Jim and lake Disney is 50 miles
    distance_Disney_to_London = 60  # Distance between lake Disney and lake London is 60 miles

    # Calculate the total distance traveled by the birds in the two seasons
    total_distance = (birds * distance_Jim_to_Disney) + (birds * distance_Disney_to_London)
    result = total_distance
    return result

print(solution())