def solution():
    """Central Park had 8 more than half of the number of trash cans as in Veteran's Park.  Then one night, someone took half of the trash cans from Central Park and put them in Veteran's Park.  If originally there were 24 trash cans in Veteran's Park, how many trash cans are now in Veteran's Park?"""
    # Define the original number of trash cans in Veteran's Park
    original_veterans_cans = 24

    # Calculate the original number of cans in Central Park
    original_central_cans = 2 * (original_veterans_cans - 8)

    # Calculate the number of cans moved from Central Park to Veteran's Park
    cans_moved = original_central_cans // 2

    # Calculate the new number of cans in Veteran's Park
    new_veterans_cans = original_veterans_cans + cans_moved

    # Display the new number of cans in Veteran's Park
    result = new_veterans_cans
    return result

print(solution())