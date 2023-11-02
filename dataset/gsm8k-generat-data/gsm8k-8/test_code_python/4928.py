def solution():
    # Define the current number of swans
    current_swans = 15

    # Define the number of doublings that will occur in ten years
    doublings = 10 // 2

    # Calculate the future number of swans
    future_swans = current_swans * (2 ** doublings)

    result = future_swans
    return result

print(solution())