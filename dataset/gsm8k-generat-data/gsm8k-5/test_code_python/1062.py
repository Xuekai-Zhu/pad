def solution():
    # Calculate the total number of sandwiches eaten
    sandwiches_eaten = 1 + 2 + 2 + 1 + 1  # Ruth ate 1, her brother ate 2, first cousin ate 2, two other cousins ate 1 each

    # Calculate the total number of sandwiches
    sandwiches_total = sandwiches_eaten + 3  # 3 left over

    result = sandwiches_total
    return result

print(solution())