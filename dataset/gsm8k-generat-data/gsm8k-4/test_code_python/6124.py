def solution():
    """One dress requires 5.5 yards of fabric. Amare needs to make 4 dresses for the wedding and she has 7 feet of fabric. How many feet of fabric does Amare still need for the dresses?"""
    # Define the number of dresses to make and the amount of fabric needed per dress
    NUM_DRESSES = 4
    FABRIC_PER_DRESS = 5.5

    # Convert the fabric required per dress from yards to feet
    FABRIC_PER_DRESS_FEET = FABRIC_PER_DRESS * 3

    # Calculate the total amount of fabric needed for all dresses
    total_fabric_needed = FABRIC_PER_DRESS_FEET * NUM_DRESSES

    # Calculate the remaining fabric after making the dresses
    remaining_fabric = 7 - total_fabric_needed

    # Return the result
    result = remaining_fabric
    return result

print(solution())