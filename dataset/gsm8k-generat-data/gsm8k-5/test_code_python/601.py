def solution():
    cheetah_speed = 60  # Cheetah runs at top speed of 60 mph
    gazelle_speed = 40  # Gazelle runs at top speed of 40 mph
    mph_to_fps = 1.5  # 1 mph is equivalent to 1.5 fps

    # Convert cheetah and gazelle speeds to fps
    cheetah_speed_fps = cheetah_speed * mph_to_fps
    gazelle_speed_fps = gazelle_speed * mph_to_fps

    initial_distance = 210  # The cheetah and gazelle start 210 feet apart

    # Calculate the relative speed between the cheetah and gazelle
    relative_speed_fps = cheetah_speed_fps - gazelle_speed_fps

    # Calculate the time it takes for the cheetah to catch up to the gazelle
    time = initial_distance / relative_speed_fps
    result = time
    return result

print(solution())