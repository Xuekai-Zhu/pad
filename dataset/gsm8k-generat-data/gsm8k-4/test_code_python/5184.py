def solution():
    """One pair of pants requires 8.5 feet of fabric. Nguyen needs to make 7 pairs of pants for the wedding. He has 3.5 yards of fabric. How many feet of fabric does Nguyen still need for the pants?"""
    # Define the number of pairs of pants and the fabric requirement per pair
    NUM_PANTS = 7
    FABRIC_REQ_PER_PANT = 8.5

    # Convert the available fabric from yards to feet
    available_fabric_yards = 3.5
    available_fabric_feet = available_fabric_yards * 3

    # Calculate the total fabric requirement for all the pants
    total_fabric_req = NUM_PANTS * FABRIC_REQ_PER_PANT

    # Calculate the remaining fabric needed
    fabric_needed = total_fabric_req - available_fabric_feet

    # return the result
    result = fabric_needed
    return result

print(solution())