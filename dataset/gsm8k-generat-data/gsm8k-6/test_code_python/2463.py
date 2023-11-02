def solution():
    # Calculate the number of athletes who left the camp in 4 hours
    athletes_left = 28 * 4

    # Calculate the number of athletes who arrived at the camp in 7 hours
    athletes_arrived = 15 * 7

    # Calculate the difference between the total number of athletes on the first and second night
    difference = 300 - athletes_left + athletes_arrived

    result = difference
    return result

print(solution())