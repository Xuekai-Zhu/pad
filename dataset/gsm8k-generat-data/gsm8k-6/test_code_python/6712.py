def solution():
    # Calculate the distance Candace can walk in the old shoes
    distance_old_shoes = 6 * 4  # Candace walks 6 miles per hour for 4 hours

    # Calculate the distance Candace can walk in the new shoes before getting a blister
    distance_before_blister = 2 * 2  # Candace walks for 2 hours before getting a blister

    # Calculate the distance Candace can walk with blisters in the new shoes
    distance_with_blisters = (6 - 2) * 2  # Each blister slows Candace down by 2 miles per hour

    # Calculate the total distance Candace can walk in the new shoes
    distance_new_shoes = distance_before_blister + distance_with_blisters

    result = distance_new_shoes
    return result

print(solution())