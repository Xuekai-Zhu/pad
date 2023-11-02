def solution():
    football_field_length = 2000
    track_length = 10000
    time_to_run_field = 2
    ratio = track_length / football_field_length
    time_to_run_track = ratio * time_to_run_field
    result = time_to_run_track
    return result

print(solution())