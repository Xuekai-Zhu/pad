def solution():
    
    total_flyers = 200
    ryan_flyers = 42
    alyssa_flyers = 67
    scott_flyers = 51
    belinda_flyers = total_flyers - ryan_flyers - alyssa_flyers - scott_flyers
    belinda_percentage = (belinda_flyers / total_flyers) * 100
    result = belinda_percentage
    return result

print(solution())