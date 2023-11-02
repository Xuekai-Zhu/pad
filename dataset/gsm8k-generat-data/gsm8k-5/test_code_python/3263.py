def solution():
    # Calculate the total number of candy canes Andy receives
    candy_canes = 2 + (3 * 4)  # Andy gets 2 from his parents and 3 each from 4 teachers

    # Calculate the number of candy canes he buys with his allowance
    allowance_candy_canes = candy_canes / 7

    # Calculate the total number of candy canes Andy eats
    total_candy_canes = candy_canes + allowance_candy_canes

    # Calculate the number of cavities he gets based on the ratio of candy canes to cavities
    cavities = total_candy_canes // 4

    result = cavities
    return result

print(solution())