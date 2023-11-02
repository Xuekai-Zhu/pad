def solution():
    # Calculate the total length of the highway built so far
    total_built = 50 + 3*50  # first day: 50 miles, second day: 3 times this amount

    # Calculate the remaining length of the highway that needs to be built
    remaining_length = 650 - 200 - total_built  # current length: 200 miles, total built: from first and second day

    result = remaining_length
    return result

print(solution())