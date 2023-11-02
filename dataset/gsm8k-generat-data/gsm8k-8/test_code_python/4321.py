def solution():
    # Define Arnold's number of jellybeans
    arnold_jellybeans = 5

    # Calculate Lee's number of jellybeans
    lee_jellybeans = arnold_jellybeans * 2

    # Calculate Tino's number of jellybeans
    tino_jellybeans = lee_jellybeans + 24
    result = tino_jellybeans
    return result

print(solution())