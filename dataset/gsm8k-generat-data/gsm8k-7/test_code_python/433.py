def solution():
    large_price = 100
    small_price = 80
    num_large_paintings = 5
    num_small_paintings = 8

    # Calculate the total earnings from selling large paintings
    large_earnings = large_price * num_large_paintings

    # Calculate the total earnings from selling small paintings
    small_earnings = small_price * num_small_paintings

    # Calculate the total earnings from selling all paintings
    total_earnings = large_earnings + small_earnings
    result = total_earnings
    return result

print(solution())