def solution():
    """Every 2 years, the number of swans at Rita's pond doubles. Currently, there are 15 swans in the pond. How many swans will there be in ten years?"""
    # Define the current number of swans
    current_swans = 15

    # Calculate the number of doublings in ten years
    doublings = 10 // 2

    # Calculate the future number of swans
    future_swans = current_swans * (2 ** doublings)

    # Display the future number of swans
    result = future_swans
    return result

print(solution())