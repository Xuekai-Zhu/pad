def solution():
    num_wrestles = 20
    percent_beaten = 80

    # Calculate the number of people John beat
    num_beaten = num_wrestles * (percent_beaten / 100)

    # Calculate the number of people John lost
    num_lost = num_wrestles - num_beaten
    result = num_lost
    return result

print(solution())