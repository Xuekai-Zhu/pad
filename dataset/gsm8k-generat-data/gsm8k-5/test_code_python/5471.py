def solution():
    diana_situps = 40  # Diana did 40 situps
    diana_rate = 4  # Diana's situp rate is 4 per minute
    hani_rate = diana_rate + 3  # Hani's situp rate is 3 more than Diana's

    # Calculate the total time Diana took to do her situps, using rate * time = distance
    diana_time = diana_situps / diana_rate

    # Calculate the total number of situps Hani did using her rate and the time it took Diana
    hani_situps = hani_rate * diana_time

    # Calculate the total number of situps they did together
    total_situps = diana_situps + hani_situps
    result = total_situps
    return result

print(solution())