def solution():
    # Calculate the total number of strawberries left in each bucket after taking out 20
    strawberries_per_bucket = (300 // 5) - 20  # divide 300 by 5 to get the original number per bucket, then subtract 20
    result = strawberries_per_bucket
    return result

print(solution())