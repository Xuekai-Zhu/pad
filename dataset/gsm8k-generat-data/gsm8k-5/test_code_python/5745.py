def solution():
    standing_time = 10  # Barry stands on his head for 10 minutes at a time
    sitting_time = 5  # Barry sits for 5 minutes before standing again
    total_time = 120  # Barry has 2 hours (120 minutes) to take turns standing on his head

    # Calculate how many turns Barry can take standing on his head
    turns = (total_time // (standing_time + sitting_time))

    result = turns
    return result

print(solution())