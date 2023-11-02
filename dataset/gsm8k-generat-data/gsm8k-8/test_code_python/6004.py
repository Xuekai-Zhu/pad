def solution():
    # Define the number of jellybeans needed for a large and small drinking glass
    large_glass = 50
    small_glass = large_glass / 2

    # Calculate the total number of jellybeans needed for the 5 large glasses
    total_large = large_glass * 5

    # Calculate the total number of jellybeans needed for the 3 small glasses
    total_small = small_glass * 3

    # Calculate the total number of jellybeans needed for all the glasses
    total_jellybeans = total_large + total_small
    result = total_jellybeans
    return result

print(solution())