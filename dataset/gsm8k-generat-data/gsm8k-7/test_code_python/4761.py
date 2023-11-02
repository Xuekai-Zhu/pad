def solution():
    num_jellybeans = 100
    num_kids = 22   # 24 kids - 2 sick kids
    jellybeans_per_kid = 3

    # Calculate the total number of jellybeans eaten
    total_jellybeans_eaten = num_kids * jellybeans_per_kid

    # Calculate the number of jellybeans left in the jar
    num_jellybeans_left = num_jellybeans - total_jellybeans_eaten
    result = num_jellybeans_left
    return result

print(solution())