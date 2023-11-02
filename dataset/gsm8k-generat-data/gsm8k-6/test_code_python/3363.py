def solution():
    # Let b, k, r, and w be the number of pairs of blue, black, red, and white socks respectively
    # We know that b = k + 3, r = w - 1, and 2r = b
    # Also, since there are 6 red socks in total, there are 3 pairs of red socks, i.e. r = 3

    r = 3
    w = r + 1
    b = 2 * r
    k = b - 3

    # Calculate the total number of socks
    total_socks = 2 * (b + k + r + w)  # multiply by 2 to count pairs of socks

    result = total_socks
    return result

print(solution())