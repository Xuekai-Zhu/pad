def solution():
    # Find how many seconds Bill put the french fries in for
    cooking_time = 45

    # Convert recommended time to seconds
    recommended_time = 5 * 60

    # Find how many seconds remained
    remaining_time = recommended_time - cooking_time
    result = remaining_time
    return result

print(solution())