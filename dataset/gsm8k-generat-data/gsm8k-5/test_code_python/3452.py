def solution():
    recommended_screen_time = 2 * 60  # Convert 2 hours to minutes
    already_used_screen_time = 45  # The child already used the gadget for 45 minutes in the morning

    # Calculate the remaining screen time allowed for the child
    remaining_screen_time = recommended_screen_time - already_used_screen_time
    result = remaining_screen_time
    return result

print(solution())