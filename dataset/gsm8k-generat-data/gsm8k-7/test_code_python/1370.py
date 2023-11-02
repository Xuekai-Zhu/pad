def solution():
    total_strands = 22
    hannah_rate = 8
    son_rate = 3

    # Calculate the total time it takes for Hannah to cut all the strands
    hannah_time = total_strands / hannah_rate

    # Calculate the total time it takes for Hannah's son to cut all the strands
    son_time = total_strands / son_rate

    # Take the maximum time of the two since they will be working together
    total_time = max(hannah_time, son_time)
    result = total_time
    return result

print(solution())