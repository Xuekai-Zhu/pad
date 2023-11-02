def solution():
    # Calculate the total number of apples picked by Kaiden and Adriel in the first round
    initial_pickings = 400 + 400  # they each picked 400

    # Calculate the number of apples picked in the second round
    second_pickings = (3/4) * 400 + (3/4) * 400  # each picked 3/4 times as many as they picked earlier

    # Calculate the total number of apples picked
    total_apples_picked = initial_pickings + second_pickings + 600 + 600

    # Calculate the target number of apples to pick
    target_apples = total_apples_picked / 2  # they were picking together

    result = target_apples
    return result

print(solution())