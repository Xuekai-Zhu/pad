def solution():
    mars_end_time = 12 * 60 + 10  # Convert end time of Mars visibility to minutes after 6:00AM
    jupiter_appear_time = mars_end_time + 2 * 60 + 41  # Calculate the time Jupiter appears in minutes after 6:00AM
    uranus_appear_time = jupiter_appear_time + 3 * 60 + 16  # Calculate the time Uranus appears in minutes after 6:00AM

    # Calculate the time elapsed from 6:00AM to when Uranus first appears
    elapsed_time = uranus_appear_time - 6 * 60
    result = elapsed_time
    return result

print(solution())