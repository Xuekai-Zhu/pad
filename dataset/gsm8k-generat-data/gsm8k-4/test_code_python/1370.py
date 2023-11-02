def solution():
    """Hannah comes home from work to find her older son taped her younger son to a chair with 22 strands of duct tape. If Hannah can cut 8 strands per minute and her son can cut 3 strands per minute, how long will it take them to free her younger son?"""
    # Define the number of strands of duct tape
    tape_strands = 22

    # Define the cutting speeds of Hannah and her son
    hannah_speed = 8
    son_speed = 3

    # Initialize the time counter
    time = 0

    # While there are still strands of tape remaining
    while tape_strands > 0:
        # Increment the time counter
        time += 1

        # Cut as many strands as possible in one minute
        hannah_cut = min(hannah_speed, tape_strands)
        tape_strands -= hannah_cut

        # Cut as many strands as possible in one minute
        son_cut = min(son_speed, tape_strands)
        tape_strands -= son_cut

    # return the result
    result = time
    return result

print(solution())