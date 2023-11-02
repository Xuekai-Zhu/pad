def solution():
    # Convert Yolanda's 15 minutes delay to hours
    yolanda_delay = 15 / 60  # 15 minutes = 0.25 hours

    # Calculate how far Yolanda travels in the time her husband catches up to her
    yolanda_distance = 20 * (yolanda_delay + 1)  # Yolanda travels at 20 mph for (yolanda_delay + 1) hours

    # Calculate how long it takes for the husband to catch up to Yolanda
    catching_time = yolanda_distance / (40 - 20) * 60  # catching time = distance / relative speed, converted to minutes
    
    result = catching_time
    return result

print(solution())