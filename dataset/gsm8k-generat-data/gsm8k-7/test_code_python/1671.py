def solution():
    initial_width = 50
    final_width = 80
    width_increase_per_ten_meters = 2
    rowing_speed = 5  # meters per second

    # Calculate the total width that needs to be crossed
    total_width = final_width - initial_width

    # Calculate how many intervals of 10 meters are needed to cover the total width
    num_intervals = total_width // width_increase_per_ten_meters

    # Calculate the total distance that needs to be rowed
    total_distance = (initial_width + (num_intervals * width_increase_per_ten_meters)) / 2

    # Calculate the time it will take to row the total distance
    time = total_distance / rowing_speed
    result = time
    return result

print(solution())