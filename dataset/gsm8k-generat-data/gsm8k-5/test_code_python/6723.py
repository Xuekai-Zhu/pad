def solution():
    # Calculate the amount of growth from last haircut to current length
    growth = 36 - 6  # Bob's hair grew 30 inches

    # Calculate the number of months it took to grow that much
    months = growth / 0.5  # Hair grows at a rate of 0.5 inches per month

    # Calculate the number of years it took to grow that much
    years = months / 12

    result = years
    return result

print(solution())