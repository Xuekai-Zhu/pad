def solution():
    """Central Park had 8 more than half of the number of trash cans as in Veteran's Park. Then one night, someone took half of the trash cans from Central Park and put them in Veteran's Park. If originally there were 24 trash cans in Veteran's Park, how many trash cans are now in Veteran's Park?"""
    # Define the number of trash cans in Veteran's Park
    veteran_trash_cans = 24

    # Calculate the number of trash cans in Central Park
    central_trash_cans = 2 * (veteran_trash_cans - 8)

    # Calculate the number of trash cans taken from Central Park
    central_taken = central_trash_cans / 2

    # Calculate the new number of trash cans in Veteran's Park
    veteran_new = veteran_trash_cans + central_taken

    # return the result
    result = veteran_new
    return result

print(solution())