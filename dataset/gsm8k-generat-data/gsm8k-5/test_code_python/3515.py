def solution():
    num_small_boxes = 2400
    num_medium_boxes = 1800
    time_hugo_small = 3
    time_hugo_medium = 6
    time_tom_both = 4

    # Calculate the time it would take Hugo to fold all boxes alone
    time_hugo_alone = (num_small_boxes * time_hugo_small) + (num_medium_boxes * time_hugo_medium)

    # Calculate the time it would take Tom to fold all boxes alone
    time_tom_alone = (num_small_boxes + num_medium_boxes) * time_tom_both

    # Calculate the time it would take both Hugo and Tom to fold all boxes together
    time_hugo_tom = max(num_small_boxes, num_medium_boxes) * time_tom_both

    # Determine the fastest time by comparing the three options
    fastest_time = min(time_hugo_alone, time_tom_alone, time_hugo_tom)
    result = fastest_time
    return result

print(solution())