def solution():
    """Amanda had 7 candy bars. She gave 3 to her sister. The next day, Amanda won some prize money and bought another 30 candy bars. She gave her sister 4 times as many candy bars as she did the first time. How many candy bars did Amanda keep for herself altogether?"""
    # Define the initial number of candy bars Amanda had
    starting_candy_bars = 7

    # Define the number of candy bars Amanda gave to her sister the first time
    first_gift = 3

    # Define the number of candy bars Amanda bought with her prize money
    additional_candy_bars = 30

    # Define the number of candy bars Amanda gave to her sister the second time
    second_gift = 4 * first_gift

    # Calculate the total number of candy bars Amanda has now
    total_candy_bars = starting_candy_bars + additional_candy_bars - first_gift - second_gift

    # Display the total number of candy bars Amanda kept for herself
    result = total_candy_bars
    return result

print(solution())