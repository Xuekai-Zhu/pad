def solution():
    # Find the height of Frank
    frank_height = 4.5 + 0.5  # Frank is half a foot taller than Pepe

    # Find the height of Larry
    larry_height = frank_height + 1  # Larry is one foot taller than Frank

    # Find the height of Ben
    ben_height = larry_height + 1  # Ben is one foot taller than Larry

    # Find the height of Big Joe
    big_joe_height = ben_height + 1  # Big Joe is one foot taller than Ben

    # Convert the height of Big Joe from inches to feet
    big_joe_height_feet = big_joe_height / 12

    result = big_joe_height_feet
    return result

print(solution())