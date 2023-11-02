def solution():
    total_catches = 23

    # Calculate Derek's catches based on the given information
    derek_catches = (total_catches - 4) / 2

    # Calculate Tammy's catches based on the given information
    tammy_catches = (derek_catches / 3) + 16

    result = tammy_catches
    return result

print(solution())