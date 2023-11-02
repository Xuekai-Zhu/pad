def solution():
    # Define initial snowflake count and incremental increase
    initial_count = 10
    incremental_increase = 4

    # Calculate time it takes to reach 58 snowflakes
    time_passed = (58 - initial_count) / incremental_increase * 5
    result = time_passed
    return result

print(solution())