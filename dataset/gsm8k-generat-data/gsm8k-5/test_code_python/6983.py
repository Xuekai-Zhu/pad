def solution():
    # Calculate the number of minutes the Ferris wheel is open
    minutes_open = (7-1) * 60  # 6 hours multiplied by 60 minutes per hour

    # Calculate the number of 20-minute cycles the Ferris wheel can complete during its operation
    cycles = minutes_open // 20

    # Calculate the total number of people who can ride the Ferris wheel during its operation
    total_riders = cycles * 70

    result = total_riders
    return result

print(solution())