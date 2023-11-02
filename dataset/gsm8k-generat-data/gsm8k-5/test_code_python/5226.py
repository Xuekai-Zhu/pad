def solution():
    # Calculate the capacity of the rectangular tables
    rectangular_capacity = 4 * 6 + 16 * 4  # 4 tables that seat 6 and 16 tables that seat 4

    # Calculate the capacity of the round tables
    round_capacity = 8 * 10  # 8 round tables that seat 10

    # Calculate the total capacity of all the tables
    total_capacity = rectangular_capacity + round_capacity
    result = total_capacity
    return result

print(solution())