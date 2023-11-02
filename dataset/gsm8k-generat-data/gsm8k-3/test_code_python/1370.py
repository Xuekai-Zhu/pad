def solution():
    """Hannah comes home from work to find her older son taped her younger son to a chair with 22 strands of duct tape. If Hannah can cut 8 strands per minute and her son can cut 3 strands per minute, how long will it take them to free her younger son?"""
    # Define the number of strands of duct tape holding the younger son
    duct_tape_strands = 22

    # Define the cutting rates of Hannah and her son
    hannah_rate = 8 # strands per minute
    son_rate = 3 # strands per minute

    # Calculate the time it takes for Hannah and her son to free the younger son
    total_rate = hannah_rate + son_rate
    time = duct_tape_strands / total_rate

    # Display the time it takes to free the younger son
    result = time
    return result

print(solution())