def solution():
    num_shirts = 20
    num_shorts = 8

    num_folded_shirts = 12
    num_folded_shorts = 5

    # Calculate the remaining shirts to fold
    remaining_shirts = num_shirts - num_folded_shirts

    # Calculate the remaining shorts to fold
    remaining_shorts = num_shorts - num_folded_shorts

    # Calculate the total remaining pieces of clothing to fold
    remaining_clothes = remaining_shirts + remaining_shorts
    result = remaining_clothes
    return result

print(solution())