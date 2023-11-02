def solution():
    members = 200  # Number of members on the forum
    q_per_hour = 3  # Number of questions posted per user per hour

    # Calculate the total number of questions asked in a day
    q_per_day = members * q_per_hour * 24

    # Calculate the average number of answers posted per member
    a_per_member = 3 * q_per_hour

    # Calculate the total number of answers posted in a day
    a_per_day = members * a_per_member * 24

    # Calculate the total number of questions and answers posted on the forum in a day
    total = q_per_day + a_per_day
    result = total
    return result

print(solution())