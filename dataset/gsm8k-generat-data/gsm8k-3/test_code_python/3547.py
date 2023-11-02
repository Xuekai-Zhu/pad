def solution():
    """James gets a fleet of gas transportation vans.  He gets 6 vans.  2 of them are 8000 gallons.  1 of them is 30% less than that.  The remaining trucks are 50% larger than the 2 trucks.  How many gallons can he transport?"""
    # Define the number of vans and their capacities
    num_vans = 6
    van1 = 8000
    van2 = 8000
    van3 = van1 * 0.7
    van4 = van5 = van6 = van2 * 1.5

    # Calculate the total capacity of all the vans
    total_capacity = van1 + van2 + van3 + van4 + van5 + van6

    # Display the total capacity
    result = total_capacity
    return result

print(solution())