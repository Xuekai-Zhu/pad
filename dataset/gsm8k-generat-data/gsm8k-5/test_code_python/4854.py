def solution():
    fine = 256  # Jed was fined $256
    limit = 50  # The posted speed limit was 50 mph

    # Calculate the speed Jed was traveling
    speed = (fine / 16) + limit
    result = speed
    return result

print(solution())