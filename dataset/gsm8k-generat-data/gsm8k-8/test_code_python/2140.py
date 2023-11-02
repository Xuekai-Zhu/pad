def solution():
    # Calculate the total number of tablets taken in a day
    tablets_per_day = 24 / 6 * 2

    # Calculate the total amount of mg taken in a day
    mg_per_day = tablets_per_day * 375

    result = mg_per_day
    return result

print(solution())