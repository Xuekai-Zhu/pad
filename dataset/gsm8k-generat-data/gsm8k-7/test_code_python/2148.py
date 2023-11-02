def solution():
    num_reality_shows = 5
    reality_show_length = 28
    cartoon_length = 10

    # Calculate the total length of time Missy spends watching reality shows
    total_reality_show_time = num_reality_shows * reality_show_length

    # Add the length of time Missy spends watching the cartoon
    total_time = total_reality_show_time + cartoon_length
    result = total_time
    return result

print(solution())