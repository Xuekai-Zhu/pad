def solution():
    total_US_states = 50  # total number of US states
    percent_collected = (40/total_US_states) * 100  # percentage of states' license plates collected
    earnings = percent_collected * 2  # $2 for each percentage point collected
    result = earnings
    return result

print(solution())