def solution():
    # Define the length of each segment in minutes
    talking_segment_length = 10
    ad_break_length = 5

    # Calculate the length of all talking segments and ad breaks combined
    total_talk_and_ad = (3 * talking_segment_length) + (5 * ad_break_length)

    # Calculate the length of the entire show in minutes
    total_show_length = 3 * 60

    # Calculate the length of the songs by subtracting the total talk and ad time from the total show time
    song_length = total_show_length - total_talk_and_ad
    result = song_length
    return result

print(solution())