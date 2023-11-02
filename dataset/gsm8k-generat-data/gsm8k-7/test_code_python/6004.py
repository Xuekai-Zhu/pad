def solution():
    jellybeans_per_large = 50
    jellybeans_per_small = jellybeans_per_large / 2
    num_large_glasses = 5
    num_small_glasses = 3

    # Calculate the total number of jellybeans needed for all the large glasses
    total_large_jellybeans = num_large_glasses * jellybeans_per_large

    # Calculate the total number of jellybeans needed for all the small glasses
    total_small_jellybeans = num_small_glasses * jellybeans_per_small

    # Calculate the total number of jellybeans needed for all the glasses
    total_jellybeans = total_large_jellybeans + total_small_jellybeans
    result = total_jellybeans
    return result

print(solution())