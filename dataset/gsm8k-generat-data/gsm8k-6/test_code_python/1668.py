def solution():
    # Calculate the total weight of rocks in the bucket
    total_weight = 60 / 4  # Jim makes $4 for every pound of rocks
    # Calculate the number of rocks in the bucket, assuming an average weight of 1.5 pounds per rock
    number_of_rocks = total_weight / 1.5
    result = number_of_rocks
    return result

print(solution())