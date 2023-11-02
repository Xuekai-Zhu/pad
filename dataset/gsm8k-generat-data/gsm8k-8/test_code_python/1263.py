def solution():
    # Phil started with 50 quarters
    quarters = 50
    # Doubled his collection the next year
    quarters *= 2
    # Collected 3 quarters each month for the following year, which is 36 quarters
    quarters += 3 * 12
    # Collected 1 quarter every third month for the year after, which is 4 quarters
    quarters += 1 * 4
    # Lost a quarter of his collection, which is 37 quarters
    quarters -= 37
    result = quarters
    return result

print(solution())