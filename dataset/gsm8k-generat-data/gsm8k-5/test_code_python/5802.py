def solution():
    distance_monday = 9000  # Hannah ran 9 kilometers on Monday
    distance_wednesday = 4816  # Hannah ran 4816 meters on Wednesday
    distance_friday = 2095  # Hannah ran 2095 meters on Friday

    # Calculate the total distance Hannah ran on Wednesday and Friday
    distance_wed_fri = distance_wednesday + distance_friday

    # Calculate how many meters farther Hannah ran on Monday compared to Wednesday and Friday combined
    difference = distance_monday - distance_wed_fri
    result = difference
    return result

print(solution())