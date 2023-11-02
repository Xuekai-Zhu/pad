def solution():
    # Calculate the number of athletes who left the camp on Saturday morning
    left_camp = 4 * 28

    # Calculate the number of athletes who arrived at the camp on Saturday afternoon
    arrived_camp = 7 * 15

    # Calculate the total number of athletes who stayed overnight on Saturday
    stayed_camp = 300 - left_camp + arrived_camp

    # Calculate the difference in the total number of athletes from Friday night to Saturday night
    difference = stayed_camp - 300
    result = difference
    return result

print(solution())