def solution():
    """James gets a fleet of gas transportation vans. He gets 6 vans. 2 of them are 8000 gallons. 1 of them is 30% less than that. The remaining trucks are 50% larger than the 2 trucks. How many gallons can he transport?"""
    # Define the number of vans James has and the size of the first two vans
    num_vans = 6
    size_van1 = 8000
    size_van2 = 8000

    # Calculate the size of the third van
    size_van3 = size_van1 * (1 - 0.3)

    # Calculate the combined size of the first three vans
    size_firstthree = size_van1 + size_van2 + size_van3

    # Calculate the total size of the remaining three vans
    size_remaining = size_firstthree * 0.5

    # Calculate the total size of all the vans
    total_size = size_firstthree + size_remaining * 3

    # Return the result
    result = total_size
    return result

print(solution())