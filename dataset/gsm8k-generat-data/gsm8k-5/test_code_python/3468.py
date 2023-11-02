def solution():
    pepe_height = 4.5  # Pepe is 4 feet 6 inches tall
    frank_height = pepe_height + 0.5  # Frank is half a foot taller than Pepe
    larry_height = frank_height + 1  # Larry is one foot taller than Frank
    ben_height = larry_height + 1  # Ben is one foot taller than Larry
    big_joe_height = ben_height + 1  # Big Joe is one foot taller than Ben

    # Convert Big Joe's height from inches to feet
    big_joe_height_feet = big_joe_height / 12
    result = big_joe_height_feet
    return result

print(solution())