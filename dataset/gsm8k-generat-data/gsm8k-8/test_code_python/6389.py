def solution():
    # Calculate the original number of trash cans in Central Park
    cp_trash_cans = 2 * (vp_trash_cans - 8)

    # Calculate the number of trash cans moved from Central Park
    moved_trash_cans = cp_trash_cans / 2

    # Calculate the new number of trash cans in Veteran's Park
    new_vp_trash_cans = vp_trash_cans + moved_trash_cans
    result = new_vp_trash_cans
    return result

print(solution())