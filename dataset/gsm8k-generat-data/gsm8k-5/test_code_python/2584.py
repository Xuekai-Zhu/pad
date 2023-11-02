def solution():
    total_flyers = 200  # Belinda made 200 flyers
    ryan_flyers = 42
    alyssa_flyers = 67
    scott_flyers = 51
    flyers_left = total_flyers - ryan_flyers - alyssa_flyers - scott_flyers  # Belinda passed out the remaining flyers
    belinda_percentage = (flyers_left / total_flyers) * 100
    result = belinda_percentage
    return result

print(solution())