def solution():
    # Define the number and value of Simon's red stamps
    simon_red_stamps = 30
    simon_red_stamps_value = simon_red_stamps * 0.5

    # Define the number and value of Peter's white stamps
    peter_white_stamps = 80
    peter_white_stamps_value = peter_white_stamps * 0.2

    # Calculate the difference in value between the two collections
    value_difference = simon_red_stamps_value - peter_white_stamps_value
    result = value_difference
    return result

print(solution())