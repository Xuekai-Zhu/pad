def solution():
    apple_rate = 3
    mac_rate = 4
    race_distance = 24
    time_taken_apple = race_distance / apple_rate
    time_taken_mac = race_distance / mac_rate
    time_difference = time_taken_mac - time_taken_apple
    result = time_difference
    return result

print(solution())