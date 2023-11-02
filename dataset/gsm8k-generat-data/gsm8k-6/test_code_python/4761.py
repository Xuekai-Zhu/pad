def solution():
    # Calculate the number of kids who attended kindergarten that day
    kids_attended = 24 - 2  # 2 children called in sick and stayed home

    # Calculate the total number of jellybeans eaten by the kids
    jellybeans_eaten = 3 * kids_attended

    # Calculate the number of jellybeans still left in the jar
    jellybeans_remaining = 100 - jellybeans_eaten
    result = jellybeans_remaining
    return result

print(solution())