def solution():
    """Belinda’s dog is missing, so she made 200 flyers to distribute around town with the help of her friends. Ryan passed out 42 flyers, Alyssa passed out 67, Scott passed out 51 and Belinda passed out the rest. What percentage of the flyers did Belinda pass out?"""
    total_flyers = 200
    ryan_flyers = 42
    alyssa_flyers = 67
    scott_flyers = 51
    belinda_flyers = total_flyers - ryan_flyers - alyssa_flyers - scott_flyers
    belinda_percentage = (belinda_flyers / total_flyers) * 100
    result = belinda_percentage
    return result

print(solution())