def solution():
    push_ups_per_10_seconds = 5
    breaks_in_seconds = 16  # two 8-second breaks
    seconds_in_minute = 60

    # Calculate the total push-ups Jackie can do in one minute
    push_ups_per_minute = ((seconds_in_minute - breaks_in_seconds) / 10) * push_ups_per_10_seconds
    result = push_ups_per_minute
    return result

print(solution())