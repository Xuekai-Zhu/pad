def solution():
    # Define the ratio of younger son's toys to elder son's toys
    younger_to_elder_ratio = 3/1

    # Calculate the total number of toys bought for both sons
    total_toys = younger_to_elder_ratio * 60 + 60

    # Calculate the number of toys bought for the younger son
    younger_toys = 3 * 60

    # Calculate the number of toys bought for the elder son
    elder_toys = 60

    result = total_toys
    return result

print(solution())