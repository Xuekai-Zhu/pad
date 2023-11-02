def solution():
    num_hikes_camila = 7
    num_hikes_amanda = 8 * num_hikes_camila
    num_hikes_steven = num_hikes_amanda + 15
    hikes_per_week = 4

    # Calculate how many more hikes Camila needs to do to catch up to Steven
    hikes_to_catch_up = num_hikes_steven - num_hikes_camila

    # Calculate how many weeks it will take for Camila to catch up to Steven
    weeks_to_catch_up = hikes_to_catch_up / hikes_per_week

    result = weeks_to_catch_up
    return result

print(solution())