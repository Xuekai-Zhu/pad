def solution():
    jennifer_cans = 40  # Jennifer initially bought 40 cans
    mark_cans = 50  # Mark bought 50 cans

    # calculate how many additional cans Jennifer bought for every 5 cans Mark bought
    additional_cans = (mark_cans // 5) * 6

    # Calculate the total number of cans Jennifer bought
    total_cans = jennifer_cans + additional_cans
    result = total_cans
    return result

print(solution())