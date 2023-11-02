def solution():
    matt_time = 12
    patty_time = matt_time / 3
    rachel_time = (2 * patty_time) + 5

    # Convert all times to minutes for easier calculation
    matt_time *= 60
    patty_time *= 60
    rachel_time *= 60

    # Calculate the time it takes Rachel to paint the house
    total_time = matt_time + patty_time + rachel_time
    num_hours = total_time / 3600
    result = num_hours
    return result

print(solution())