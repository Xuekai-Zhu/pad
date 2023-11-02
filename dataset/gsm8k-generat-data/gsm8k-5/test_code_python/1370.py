def solution():
    total_strands = 22  # Total number of duct tape strands used
    hannah_rate = 8  # Hannah can cut 8 strands per minute
    son_rate = 3  # Her son can cut 3 strands per minute

    # Calculate the time it takes for Hannah and her son to free the younger son
    time = total_strands / (hannah_rate + son_rate)
    result = time
    return result

print(solution())