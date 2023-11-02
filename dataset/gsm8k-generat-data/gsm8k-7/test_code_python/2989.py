def solution():
    num_stamps_tonya = 13
    num_matchbooks_jimmy = 5
    matches_per_book = 24
    exchange_rate = 12  # 1 stamp = 12 matches

    # Calculate the total number of matches Jimmy has
    total_matches_jimmy = num_matchbooks_jimmy * matches_per_book

    # Calculate the total number of stamps Tonya receives in exchange for the matchbooks
    num_stamps_received = total_matches_jimmy // exchange_rate

    # Calculate the number of stamps Tonya has left
    num_stamps_left = num_stamps_tonya - num_stamps_received
    result = num_stamps_left
    return result

print(solution())