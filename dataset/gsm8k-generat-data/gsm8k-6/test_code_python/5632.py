def solution():
    # Calculate the total watch time required to finish the show
    total_time = 90 * 20  # 90 episodes of 20 minutes each
    days_required = total_time / (2*60)  # Tom can watch for 2 hours a day
    result = days_required
    return result

print(solution())