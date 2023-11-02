def solution():
    total_friends = 100
    keep_percentage = 0.4
    contacted_percentage = 0.6  # 100% - 40% = 60%, and then 60% * 0.5 = 30% responded

    # Calculate the number of friends Mark keeps
    num_kept = int(total_friends * keep_percentage)

    # Calculate the number of friends Mark contacts
    num_contacted = total_friends - num_kept

    # Calculate the number of friends who respond to Mark's message
    num_responded = int(num_contacted * contacted_percentage)

    # Calculate the number of friends Mark removes
    num_removed = num_contacted - num_responded

    # Calculate the number of friends Mark keeps after removal
    num_remaining = num_kept + num_responded

    result = num_remaining
    return result

print(solution())