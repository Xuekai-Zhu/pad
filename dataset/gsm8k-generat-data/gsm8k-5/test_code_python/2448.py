def solution():
    bottles_per_box = 50  # Each box contains 50 bottles of water
    liters_per_bottle = 12 * (3/4)  # Each bottle has a capacity of 12 liters filled up to 3/4
    total_liters = bottles_per_box * liters_per_bottle * 10  # There are 10 boxes of water bottles

    result = total_liters
    return result

print(solution())