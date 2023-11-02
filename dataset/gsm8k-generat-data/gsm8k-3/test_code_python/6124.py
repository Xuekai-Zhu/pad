def solution():
    """One dress requires 5.5 yards of fabric. Amare needs to make 4 dresses for the wedding and she has 7 feet of fabric. How many feet of fabric does Amare still need for the dresses?"""
    # Convert yards to feet
    YARDS_TO_FEET = 3
    fabric_needed_per_dress = 5.5 * YARDS_TO_FEET

    # Calculate the total fabric needed for all the dresses
    dresses = 4
    total_fabric_needed = fabric_needed_per_dress * dresses

    # Calculate the amount of fabric still needed
    fabric_on_hand = 7
    fabric_still_needed = total_fabric_needed - fabric_on_hand

    # Display the amount of fabric still needed
    result = fabric_still_needed
    return result

print(solution())