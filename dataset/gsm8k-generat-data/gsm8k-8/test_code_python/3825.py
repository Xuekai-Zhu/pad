def solution():
    # Define the initial number of jellybeans in the jar
    initial_jellybeans = 37

    # Remove 15 jellybeans
    jellybeans_after_15_removed = initial_jellybeans - 15

    # Add 5 jellybeans back in
    jellybeans_after_5_added = jellybeans_after_15_removed + 5

    # Remove 4 more jellybeans
    jellybeans_now = jellybeans_after_5_added - 4

    result = jellybeans_now
    return result

print(solution())