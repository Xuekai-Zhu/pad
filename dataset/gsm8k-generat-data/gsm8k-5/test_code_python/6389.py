def solution():
    original_vc_trash_cans = 24  # There were originally 24 trash cans in Veteran's Park
    cp_trash_cans = ((original_vc_trash_cans - 8) * 2)  # Central Park had 8 more than half the number of trash cans as in Veteran's Park
    cp_trash_cans_after_move = cp_trash_cans / 2  # Half of the Central Park trash cans were moved to Veteran's Park
    vc_trash_cans_after_move = original_vc_trash_cans + cp_trash_cans_after_move  # The number of trash cans in Veteran's Park after the move

    result = vc_trash_cans_after_move
    return result

print(solution())