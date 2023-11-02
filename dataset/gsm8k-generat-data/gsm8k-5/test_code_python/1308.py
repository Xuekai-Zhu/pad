def solution():
    total_time = 52  # The entire show is 52 hours long
    monday_time = (1/2) * 24  # Jake spent half the day (12 hours) on Monday watching the show
    tuesday_time = 4  # Jake spent 4 hours on Tuesday watching the show
    wednesday_time = (1/4) * 24  # Jake spent a quarter of the day (6 hours) on Wednesday watching the show
    thursday_time = (1/2) * (monday_time + tuesday_time + wednesday_time)  # Jake spent half as much time on Thursday as he did in total throughout the previous few days

    time_watched_so_far = monday_time + tuesday_time + wednesday_time + thursday_time  # Total time Jake watched the show so far

    friday_time = total_time - time_watched_so_far  # Friday is when Jake finishes the show, so this is the time he watched it on that day

    result = friday_time
    return result

print(solution())