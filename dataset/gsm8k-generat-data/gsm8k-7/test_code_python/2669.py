def solution():
    num_tvs_in_store = 8
    num_tvs_online = 3 * num_tvs_in_store
    total_tvs = 42

    # Calculate the number of TVs Beatrice looked at on the auction site
    num_tvs_auction = total_tvs - num_tvs_in_store - num_tvs_online

    result = num_tvs_auction
    return result

print(solution())