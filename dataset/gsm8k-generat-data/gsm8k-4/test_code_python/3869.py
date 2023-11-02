def solution():
    """Tom hasn't been sleeping well lately. He figures he has been getting about 5 hours of sleep each weeknight and 6 hours each night on the weekend. If Tom would ideally like to get 8 hours of sleep each night on both weeknights and weekends, how many hours of sleep is Tom behind on from the last week?"""
    # Define the ideal number of hours of sleep per night
    ideal_hours = 8

    # Calculate the total number of hours of sleep Tom should have gotten
    total_ideal_hours = (5 * ideal_hours) + (2 * 6 * ideal_hours)

    # Calculate the actual number of hours of sleep Tom got
    actual_hours = (5 * 5) + (2 * 6)

    # Calculate the number of hours Tom is behind on sleep
    hours_behind = total_ideal_hours - actual_hours

    # return the result
    result = hours_behind
    return result

print(solution())