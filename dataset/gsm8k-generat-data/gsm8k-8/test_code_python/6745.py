def solution():
    # Calculate the original number of balloons each friend received
    original_per_friend = 250 / 5

    # Calculate the new number of balloons each friend has after giving away 11
    new_per_friend = original_per_friend - 11

    result = new_per_friend
    return result

print(solution())