def solution():
    bones_at_start = 10
    months_passed = 5
    bones_available = 8

    # Calculate the total number of bones Barkley has buried
    bones_buried = (bones_at_start * months_passed) - bones_available
    result = bones_buried
    return result

print(solution())