def solution():
    # Calculate the total capacity of all tables
    capacity_6 = 6 * 4  # 4 tables that seat 6 people each
    capacity_4 = 4 * 16  # 16 tables that seat 4 people each
    capacity_10 = 10 * 8  # 8 round tables that seat 10 people each
    total_capacity = capacity_6 + capacity_4 + capacity_10
    result = total_capacity
    return result

print(solution())