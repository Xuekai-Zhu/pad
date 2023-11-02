def solution():
    days_per_week = 5  # Tom runs 5 days a week
    time_per_day = 1.5  # Tom runs for 1.5 hours each day
    speed = 8  # Tom runs at a speed of 8 mph

    # Calculate the distance Tom runs each day
    distance_per_day = speed * time_per_day

    # Calculate the total distance Tom runs in a week
    total_distance = distance_per_day * days_per_week

    result = total_distance
    return result

print(solution())