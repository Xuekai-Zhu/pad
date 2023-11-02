def solution():
    rise_rate = 50  # Balloon rises at a rate of 50 feet per minute when lift chain is pulled
    descend_rate = 10  # Balloon slowly descends at a rate of 10 feet per minute when lift chain is released
    first_pull_time = 15  # Lift chain is pulled for 15 minutes
    release_time = 10  # Lift chain is released for 10 minutes
    second_pull_time = 15  # Lift chain is pulled for another 15 minutes

    # Calculate the highest elevation reached by the balloon
    total_rise = (rise_rate * first_pull_time) + (rise_rate * second_pull_time)
    total_descend = descend_rate * release_time
    highest_elevation = total_rise - total_descend
    result = highest_elevation
    return result

print(solution())