def solution():
    # Define the fine and posted speed limit
    fine = 256
    posted_limit = 50

    # Calculate the amount above the posted speed limit that resulted in the fine
    amount_above_limit = fine / 16

    # Calculate the speed that resulted in the fine
    fined_speed = posted_limit + amount_above_limit
    result = fined_speed
    return result

print(solution())